using UnityEngine;
using System.Collections;

namespace SmallScaleInteractive._2DCharacter
{
    public class PlayerController : MonoBehaviour
    {
        private Rigidbody2D rb;

        private Animator animator;

        public float movementSpeed = 5f;
        public float crouchSpeedFactor = 0.5f;
        public bool isCrouching = false;
        public bool canMove = true; // Controls whether the player can move
        public float attackMoveLockDuration = 0.8f; // Time in seconds to lock movement during an attack
        public bool isGrounded = false; //the player starts in the air
        public bool isCurrentlyJumping = false;
        public int jumpCount = 0;
        public float jumpForce = 7f;
        public float jumpDelay = 0.4f; // Delay for jump to allow animation sync
        public float jumpCooldown = 0.2f; // Cooldown period after a jump
       
        public bool isWallHanging = false;
        public float wallSlideSpeed = 1f;  // Reduced speed for sliding down the wall
        public Vector2 wallJumpForce = new Vector2(5f, 7f);  // Force applied for wall jumps
        private Vector3 lastWallContactPoint;  // Store the last contact point with a wall
        public float wallClimbSpeed = 2f;
        public bool isClimbingLedge = false;
        public Transform leftLedgeDetector;
        public Transform rightLedgeDetector;
        public bool isAirSlamming = false;
        public float airSlamForce = 20f;  // The force applied downwards during an Air Slam

        public float airDashForce = 10f;  // The force applied horizontally during an Air Dash
        public bool isAirDashing = false;  // To check if the Air Dash is currently active
        public float dashCooldown = 1.0f;
        private float lastDashTime = 0;

        public EdgeCollider2D edgeCollider; // Reference to the edge collider

        public GameObject aoEPrefab;

        void Start()
        {
            animator = GetComponent<Animator>();
            rb = GetComponent<Rigidbody2D>();
            edgeCollider = GetComponent<EdgeCollider2D>();
        }

        void Update()
        {
            if (canMove && !isClimbingLedge)
            {
                HandleMovement();
                HandleCrouching();
                HandleAttacking();
                HandleJumping();
                HandleAirDash();
                HandleGroundDash();
                HandleSliding();

                // Special abilities handling
                HandleSpecialAbility1();
                HandleSpecialAbility2();

                // Damage and death handling
                HandleTakingDamage();
                HandleTemporaryDeath();
                CheckForLedges();



                if (isWallHanging)
                {
                    jumpCount = 0; // Reset double jump count to allow ground mechanics to handle further jumps
                }
                if (rb.velocity.y < 0) //if running off a cliff for example
                {
                    isGrounded = false;
                    isCurrentlyJumping = true;
                }
            }
        }

        private void HandleMovement()
        {
            if (!canMove)
                return;

            // Directly check for left or right key presses
            bool isPressingLeft = Input.GetKey(KeyCode.A);
            bool isPressingRight = Input.GetKey(KeyCode.D);
            bool isMoving = isPressingLeft || isPressingRight;

            // Determine the speed based on whether the player is crouching
            float speed = isCrouching ? movementSpeed * crouchSpeedFactor : movementSpeed;

            // Set the direction based directly on input keys
            if (isPressingRight)
            {
                animator.SetInteger("Direction", 0); // Assume 0 is for moving right (east)
                rb.velocity = new Vector2(speed, rb.velocity.y);
            }
            else if (isPressingLeft)
            {
                animator.SetInteger("Direction", 1); // Assume 1 is for moving left (west)
                rb.velocity = new Vector2(-speed, rb.velocity.y);
            }
            else
            {
                rb.velocity = new Vector2(0, rb.velocity.y); // No horizontal movement
            }

            // Update the animator's walking state
            animator.SetBool("isWalking", isMoving);

            // Handle falling and crouching animations
            if (!isGrounded && rb.velocity.y < 0)
            {
                animator.SetBool("isSliding", false);
                animator.SetBool("isFalling", true);
            }

            animator.SetBool("isCrouchingWalking", isCrouching && isMoving);
        }




        private void HandleCrouching()
        {
            if (Input.GetKeyDown(KeyCode.C))
            {
                isCrouching = true;
                animator.SetBool("isCrouching", isCrouching);
            }
            else if (Input.GetKeyUp(KeyCode.C))
            {
                isCrouching = false;
                animator.SetBool("isCrouching", isCrouching);
            }
        }

        private void HandleAttacking()
        {
            if (Input.GetMouseButtonDown(0) && isGrounded) // Left mouse button for attack
            {
                bool wasMovingWhenAttacked = Mathf.Abs(rb.velocity.x) > 0;
                float attackDirection = Mathf.Sign(rb.velocity.x); // Get the direction of the attack based on velocity

                // Trigger appropriate animations based on whether the player was moving when they attacked
                if (wasMovingWhenAttacked)
                {
                    animator.SetTrigger("isRunAttack");
                    StartCoroutine(ApplyRunningAttackForce(attackDirection));
                }
                else
                {
                    animator.SetTrigger("isAttack1");
                    StartCoroutine(AttackMoveLock(attackMoveLockDuration));
                }
            }
        }

        IEnumerator ApplyRunningAttackForce(float direction)
        {
            float initialForce = 2f; // Set this to your desired force to keep the player moving in the attack direction
            rb.AddForce(new Vector2(direction * initialForce, 0), ForceMode2D.Impulse);
            yield return StartCoroutine(AttackMoveLock(0.5f)); //locks movement for 0.5 seconds, adjust as necessary
        }



        IEnumerator AttackMoveLock(float duration)
        {
            canMove = false;
            yield return new WaitForSeconds(duration);
            canMove = true;
        }

        //Jump logic:
        private void HandleJumping()
        {
            if (canMove)
            {
                if (Input.GetKeyDown(KeyCode.Space))
                {
                    if (isWallHanging)
                    {
                        JumpOffWall();
                    }
                    else if (isGrounded || jumpCount < 2) // Handles normal and double jump
                    {
                        StartCoroutine(PerformJump());
                    }
                }
                else if (!isGrounded && !isWallHanging && Input.GetKeyDown(KeyCode.S)) // Check if in air and S key is pressed
                {
                    StartAirSlam();
                }
            }
        }

        private void JumpOffWall()
        {
            float directionMultiplier = transform.position.x > lastWallContactPoint.x ? -1 : 1;
            animator.SetTrigger("isWallJump");
            Vector2 jumpForce = new Vector2(wallJumpForce.x * directionMultiplier, wallJumpForce.y);
            rb.AddForce(jumpForce, ForceMode2D.Impulse);
            isWallHanging = false;
            isGrounded = false;
            isCurrentlyJumping = true;
            jumpCount++;
        }







        IEnumerator PerformJump()
        {
            if (jumpCount == 0 && isGrounded)
            {
                bool isMoving = animator.GetBool("isWalking");
                animator.SetTrigger(isMoving ? "isJumpRunStart" : "isJumpStart");
                yield return new WaitForSeconds(0.1f);  // Apply delay only for the first jump
                rb.AddForce(new Vector2(0, jumpForce), ForceMode2D.Impulse);
                isGrounded = false;
                isCurrentlyJumping = true;
                jumpCount++;
            }
            else // Double jump
            {
                // First, cancel out any existing downward velocity
                if (rb.velocity.y < 0)
                {
                    rb.velocity = new Vector2(rb.velocity.x, 0);  // Reset vertical velocity
                }

                // Trigger the double jump animation
                animator.SetTrigger("isDoubleJump");

                // Then, apply the double jump force
                rb.AddForce(new Vector2(0, jumpForce), ForceMode2D.Impulse);
                isGrounded = false;
                isCurrentlyJumping = true;
                jumpCount++;
            }
        }


        private void OnCollisionEnter2D(Collision2D collision)
        {

            if (collision.otherCollider == edgeCollider) // This checks if the collider on this GameObject that was hit is the edge collider
            {
                if (collision.gameObject.CompareTag("Wall") && !isGrounded && !isAirSlamming)
                {
                    isWallHanging = true;
                    isCurrentlyJumping = false;
                    lastWallContactPoint = collision.contacts[0].point;
                    rb.gravityScale = 0; // Neutralize gravity while wall hanging
                    animator.SetBool("isWallHang", true); // Set wall hanging animation state

                    if (isAirDashing)
                    {
                        isAirDashing = false;
                        canMove = true; // Enable movement after stopping the dash
                    }
                }
            }

            if (collision.gameObject.CompareTag("Ground"))
            {
                // Handle ground-related collision logic
                HandleGroundCollision();
            }
        }

        void HandleGroundCollision()
        {
            isGrounded = true;
            jumpCount = 0;
            isWallHanging = false;
            rb.gravityScale = 1;
            isCurrentlyJumping = false;

            bool isMoving = Mathf.Abs(rb.velocity.x) > 0;
            if (isAirSlamming && isGrounded)
            {
                animator.SetTrigger("isAirSlamLand");
                isAirSlamming = false;
                        // Instantiate the AoE prefab and start the destruction coroutine
                GameObject aoEInstance = Instantiate(aoEPrefab, transform.position, Quaternion.identity);
                StartCoroutine(DestroyAfterDelay(aoEInstance, 0.2f));  // Destroy after 0.5 seconds

                animator.SetBool("isAirSlam", false);
            }
            else
            {
                animator.SetTrigger(isMoving ? "isLandingRunning" : "isLanding");
            }

            if (isAirDashing)
            {
                isAirDashing = false;
            }
            canMove = true;
            animator.SetBool("isJumpMid", false);
            animator.SetBool("isFalling", false);
        }

        //Helper method to destroy AoE prefab
        IEnumerator DestroyAfterDelay(GameObject objectToDestroy, float delay)
        {
            yield return new WaitForSeconds(delay);
            Destroy(objectToDestroy);
        }

        private void OnCollisionExit2D(Collision2D collision)
        {
            if (collision.gameObject.CompareTag("Wall"))
            {
                isWallHanging = false;
                rb.gravityScale = 1; // Restore normal gravity
                animator.SetBool("isWallHang", false);
                animator.SetBool("isWallSlide", false);
            }
        }

        //AirSlam
        private void StartAirSlam()
        {
            if (!isAirSlamming) // Check if Air Slam is not already active
            {
                StartCoroutine(PerformAirSlam());
            }
        }

        IEnumerator PerformAirSlam()
        {
            isAirSlamming = true;
            animator.SetBool("isAirSlam", true);
            canMove = false;
            yield return new WaitForSeconds(0.5f); // Wait for 0.2 seconds to let the animation initiate

            // Apply the downward force after the delay
            rb.velocity = new Vector2(0, -airSlamForce); // Stop horizontal movement and apply strong downward force
        }

        //Dashing:
        void HandleAirDash()
        {
            if (Input.GetMouseButtonDown(1) && !isGrounded && !isWallHanging)  // Right mouse button for air dash
            {
                if (canMove && !isAirDashing && Time.time >= lastDashTime + dashCooldown)  // Ensure player can move, isn't already dashing, and cooldown has passed
                {
                    float horizontalInput = Input.GetAxisRaw("Horizontal");  // Get the current horizontal input
                    StartCoroutine(PerformAirDash(horizontalInput));
                    lastDashTime = Time.time;  // Update the last dash time to current time
                }
            }
        }


        IEnumerator PerformAirDash(float directionInput)
        {
            isAirDashing = true;
            canMove = false;  // Lock other movement controls during the dash
            float originalGravityScale = rb.gravityScale;
            rb.gravityScale = 0;

            float dashDirectionX = 0;
            float dashDirectionY = 0;

            // Check if 'W' is held down for upward dash
            if (Input.GetKey(KeyCode.W))
            {
                dashDirectionY = 1;  // Add upward force if 'W' is held
                animator.SetTrigger("isAirDashUpward");  // Trigger the upward dash animation
            }

            // Check horizontal direction only if not performing an exclusive upward dash
            if (dashDirectionY == 0)
            {
                if (directionInput < 0)
                {
                    dashDirectionX = -1;  // Dash left if 'A' is pressed
                    animator.SetTrigger("isAirDashAttack"); // Trigger the horizontal dash animation
                }
                else if (directionInput > 0)
                {
                    dashDirectionX = 1;   // Dash right if 'D' is pressed
                    animator.SetTrigger("isAirDashAttack");  // Trigger the horizontal dash animation
                }
            }
            else
            {
                // If performing an upward dash, consider horizontal direction for diagonal movement
                if (directionInput < 0)
                {
                    dashDirectionX = -1;  // Add leftward force for diagonal upward left dash
                }
                else if (directionInput > 0)
                {
                    dashDirectionX = 1;   // Add rightward force for diagonal upward right dash
                }
            }

            // Apply the dash force in the calculated direction if a direction was actually set
            if (dashDirectionX != 0 || dashDirectionY != 0)
            {
                rb.velocity = new Vector2(dashDirectionX * airDashForce, dashDirectionY * airDashForce);
                yield return new WaitForSeconds(0.7f);  // Duration of the dash effect
            }

            rb.gravityScale = originalGravityScale;  // Restore original gravity scale
            canMove = true;
            isAirDashing = false;
        }

        //Ground dash:
        void HandleGroundDash()
        {
            if (Input.GetMouseButtonDown(1) && isGrounded)  // Right mouse button for ground dash
            {
                float horizontalInput = Input.GetAxisRaw("Horizontal");  // Get the current horizontal input
                if (horizontalInput != 0 && canMove)  // Ensure the player can move and there's horizontal input
                {
                    StartCoroutine(PerformGroundDash(horizontalInput));
                }
            }
        }
        IEnumerator PerformGroundDash(float directionInput)
        {
            if (Input.GetMouseButtonDown(1) && isGrounded && Time.time >= lastDashTime + dashCooldown)  // Right mouse button for ground dash and check cooldown
            {
                if (directionInput != 0 && canMove)  // Ensure the player can move and there's horizontal input
                {
                    isAirDashing = true;  // Mark the dashing state
                    canMove = false;  // Lock other movement controls during the dash
                    float dashDirectionX = directionInput < 0 ? -1 : 1;

                    // Trigger the ground dash animation
                    animator.SetTrigger("isDashForward");

                    // Apply a force for the dash
                    rb.AddForce(new Vector2(dashDirectionX * airDashForce, 0), ForceMode2D.Impulse);

                    yield return new WaitForSeconds(0.5f);  // Duration of the dash effect

                    // Restore controls and state after the dash
                    canMove = true;
                    isAirDashing = false;

                    lastDashTime = Time.time;  // Update the last dash time to current time
                }
            }
        }







        void FixedUpdate()
        {
            // Check for wall climbing and jumping animations
            if (!isGrounded && isCurrentlyJumping)
            {
                if (rb.velocity.y > 0)
                {
                    animator.SetBool("isFalling", false);
                    animator.SetBool("isJumpMid", true);
                }
                else if (rb.velocity.y <= 0)
                {
                    animator.SetBool("isJumpMid", false);
                    animator.SetBool("isFalling", true);
                }
            }
            else if (!isGrounded && !isCurrentlyJumping && !isWallHanging && !isCrouching) //fail-safe logic
            {
                isGrounded = true;
                animator.SetBool("isFalling", false);
            }

            if (isGrounded && !isCurrentlyJumping)
            {
                animator.SetBool("isFalling", false);
                animator.SetBool("isJumpMid", false);
            }

            // Handle wall hanging mechanics and animations
            if (isWallHanging && !isAirSlamming)
            {
                float moveVertical = Input.GetAxisRaw("Vertical");

                // Handling vertical movement on the wall
                if (moveVertical > 0)
                {
                    rb.velocity = new Vector2(rb.velocity.x, wallClimbSpeed);
                    animator.SetBool("isClimbing", true);
                }
                else if (moveVertical < 0)
                {
                    rb.velocity = new Vector2(rb.velocity.x, -wallSlideSpeed);
                    animator.SetBool("isWallSlide", true);
                }
                else
                {
                    rb.velocity = new Vector2(rb.velocity.x, 0);
                    animator.SetBool("isWallSlide", false);
                    animator.SetBool("isClimbing", false);
                }
            }
            else
            {
                animator.SetBool("isClimbing", false);  // Ensure climbing is turned off when not wall hanging
                animator.SetBool("isWallSlide", false); // Ensure wall slide is turned off when not wall hanging
            }
        }




        void HandleSliding()
        {
            if (Input.GetKeyDown(KeyCode.LeftShift) && isGrounded && !isCrouching)
            {
                animator.SetBool("isSliding", true);
                animator.SetTrigger("isSlideStart");
            }
            if (Input.GetKeyUp(KeyCode.LeftShift))
            {
                animator.SetTrigger("isSlideEnd");
                animator.SetBool("isSliding", false);
            }
        }

        //Abilities:
        private void HandleSpecialAbility1()
        {
            if (Input.GetKeyDown(KeyCode.Alpha1) && isGrounded) // Check if '1' key is pressed
            {
                StartCoroutine(AttackMoveLock(attackMoveLockDuration));
                animator.SetTrigger("isUsingSpecialAbility1"); // Trigger special ability 1 animation
            }
        }

        private void HandleSpecialAbility2()
        {
            if (Input.GetKeyDown(KeyCode.Alpha2) && isGrounded) // Check if '2' key is pressed
            {
                StartCoroutine(AttackMoveLock(attackMoveLockDuration));
                animator.SetTrigger("isUsingSpecialAbility2"); // Trigger special ability 2 animation
            }
        }

        private void HandleTakingDamage()
        {
            if (Input.GetKeyDown(KeyCode.F) && isGrounded) // Check if 'F' key is pressed
            {
                StartCoroutine(AttackMoveLock(attackMoveLockDuration));
                animator.SetTrigger("isTakingDamage"); // Trigger taking damage animation
            }
        }

        private void HandleTemporaryDeath()
        {
            if (Input.GetKeyDown(KeyCode.V) && isGrounded) // Check if 'V' key is pressed
            {
                StartCoroutine(AttackMoveLock(attackMoveLockDuration));
                StartCoroutine(TemporaryDeath());
            }
        }

        IEnumerator TemporaryDeath()
        {
            animator.SetBool("isDead", true); // Trigger the death animation/state
            yield return new WaitForSeconds(1); // Wait for 1 second
            animator.SetBool("isDead", false); // Reset the death state
        }


        void CheckForLedges()
        {
            //NOTE: create a "Ledge" layer and set all "Ledge" objects to that layer instead of using the "Default" layer. 
            int ledgeLayer = LayerMask.GetMask("Default"); 
            float rayLength = 0.22f;
            float angleDegrees = 45;  // Adjust the angle for diagonal rays

            // Calculate direction vectors for diagonal rays
            Vector2 leftUp = Quaternion.Euler(0, 0, angleDegrees) * Vector2.left;
            Vector2 leftDown = Quaternion.Euler(0, 0, -angleDegrees) * Vector2.left;
            Vector2 rightUp = Quaternion.Euler(0, 0, -angleDegrees) * Vector2.right;
            Vector2 rightDown = Quaternion.Euler(0, 0, angleDegrees) * Vector2.right;

            // Perform raycasts in diagonal directions
            RaycastHit2D hitLeftUp = Physics2D.Raycast(leftLedgeDetector.position, leftUp, rayLength, ledgeLayer);
            RaycastHit2D hitLeftDown = Physics2D.Raycast(leftLedgeDetector.position, leftDown, rayLength, ledgeLayer);
            RaycastHit2D hitRightUp = Physics2D.Raycast(rightLedgeDetector.position, rightUp, rayLength, ledgeLayer);
            RaycastHit2D hitRightDown = Physics2D.Raycast(rightLedgeDetector.position, rightDown, rayLength, ledgeLayer);

            // Debug lines for visualizing raycasts in the Scene view
            Debug.DrawLine(leftLedgeDetector.position, leftLedgeDetector.position + (Vector3)leftUp * rayLength, Color.red);
            Debug.DrawLine(leftLedgeDetector.position, leftLedgeDetector.position + (Vector3)leftDown * rayLength, Color.blue);
            Debug.DrawLine(rightLedgeDetector.position, rightLedgeDetector.position + (Vector3)rightUp * rayLength, Color.red);
            Debug.DrawLine(rightLedgeDetector.position, rightLedgeDetector.position + (Vector3)rightDown * rayLength, Color.blue);

            // Check for hits and handle ledge climbing
            if (hitLeftUp.collider != null && hitLeftUp.collider.CompareTag("Ledge"))
            {
                HandleLedgeClimb(hitLeftUp, 1);  // 1 for left
            }
            else if (hitLeftDown.collider != null && hitLeftDown.collider.CompareTag("Ledge"))
            {
                HandleLedgeClimb(hitLeftDown, 1);  // 1 for left
            }
            if (hitRightUp.collider != null && hitRightUp.collider.CompareTag("Ledge"))
            {
                HandleLedgeClimb(hitRightUp, 0);  // 0 for right
            }
            else if (hitRightDown.collider != null && hitRightDown.collider.CompareTag("Ledge"))
            {
                HandleLedgeClimb(hitRightDown, 0);  // 0 for right
            }
        }


        void HandleLedgeClimb(RaycastHit2D hit, int direction)
        {
            StartCoroutine(ClimbOntoLedge(hit.collider.bounds, direction));
        }

        IEnumerator ClimbOntoLedge(Bounds ledgeBounds, int direction)
        {
            animator.SetTrigger("isLedgeClimbing");  // Trigger climbing animation
            animator.SetInteger("Direction", direction);  // Set direction in the animator
            animator.SetBool("isWalking", false);

            isClimbingLedge = true;
            canMove = false;  // Disable movement

            // Save the original gravity scale and velocity
            float originalGravityScale = rb.gravityScale;
            Vector2 originalVelocity = rb.velocity;

            // Deactivate colliders
            EdgeCollider2D edgeCollider = GetComponent<EdgeCollider2D>();
            CapsuleCollider2D capsuleCollider = GetComponent<CapsuleCollider2D>();
            if (edgeCollider != null) edgeCollider.enabled = false;
            if (capsuleCollider != null) capsuleCollider.enabled = false;

            // Freeze all movement and gravity
            rb.gravityScale = 0;
            rb.velocity = Vector2.zero;  // Instantly stop any movement

            yield return new WaitForSeconds(0.66f); // Adjust time based on your animation

            // Calculate the new position to make sure the character ends up on top of the ledge
            float newYPosition = ledgeBounds.max.y + (0.65f / 2); // Character height
            float newXPosition = transform.position.x + (direction == 0 ? 0.3f : -0.3f); // Adjust sideways position if needed

            transform.position = new Vector3(newXPosition, newYPosition, transform.position.z);
            animator.SetBool("isWalking", false);
            rb.velocity = Vector2.zero;

            // Reactivate colliders 
            if (edgeCollider != null) edgeCollider.enabled = true;
            if (capsuleCollider != null) capsuleCollider.enabled = true;
                        // Restore the original settings
            rb.gravityScale = 1;

            canMove = true;  // Re-enable movement
            yield return new WaitForSeconds(0.6f);  // Additional wait time
            isClimbingLedge = false;  // Reset climbing flag
        }





    }
}