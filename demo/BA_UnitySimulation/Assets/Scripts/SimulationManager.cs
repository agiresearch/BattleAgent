using System.Collections;
using System.Collections.Generic;
using Unity.Burst.Intrinsics;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UIElements;
using static UnityEditor.Experimental.AssetDatabaseExperimental.AssetDatabaseCounters;

public class SimulationManager : MonoBehaviour
{

    [SerializeField] private Transform armyEParent;
    [SerializeField] private Transform armyFParent;
    [SerializeField] private Transform armyETarget;
    [SerializeField] private Transform armyFTarget;

    [SerializeField] private Transform pixelArtsParent;


    //[SerializeField] private List<NavigateSoldier> armyEAgents;
    //[SerializeField] private List<NavigateSoldier> armyFAgents;

    private List<NavigateSoldier> armyEAgents = new List<NavigateSoldier>();
    private List<NavigateSoldier> armyFAgents = new List<NavigateSoldier>();

    private List<GameObject> pixelArts = new List<GameObject>();

    // Start is called before the first frame update
    void Start()
    {
        // Get all agents in Army E
        InitializeTeamAgents(armyEParent, armyEAgents);

        // Get all agents in Army F
        InitializeTeamAgents(armyFParent, armyFAgents);

        // Get all pixel arts animations
        InitializePixelArts();

        // Begin the battle sequence
        StartCoroutine(ManageBattleSequence());
    }

    // Update is called once per frame
    void Update()
    {
        // Set the destination of all agents in Army E
        //MoveAllTeamAgents(armyEAgents, armyETarget.position);

        // Set the destination of all agents in Army F
        //MoveAllTeamAgents(armyFAgents, armyFTarget.position);
    }

    private IEnumerator ManageBattleSequence()
    {
        yield return new WaitForSeconds(1.0f);


        Debug.Log("1. Army E gathers at [-0.2, 1.0]");
        MoveAllTeamAgents(armyEAgents, new Vector3(-0.2f, 1.0f));
        yield return new WaitUntil(() => AllAgentsReachedDestination(armyEAgents));

        yield return new WaitForSeconds(1.0f);


        Debug.Log("2. Army F gathers at [2.6, -1.2]");
        MoveAllTeamAgents(armyFAgents, new Vector3(2.6f, -1.2f));
        yield return new WaitUntil(() => AllAgentsReachedDestination(armyFAgents));

        yield return new WaitForSeconds(1.0f);


        Debug.Log("3. ArmyE takes action");
        var (armyESubAgents1, armyESubAgents2) = SplitAgents(armyEAgents, 4);
        MoveAllTeamAgents(armyESubAgents1, new Vector3(1.6f, -1.4f));
        yield return new WaitUntil(() => AllAgentsReachedDestination(armyESubAgents1));
        yield return PlayPixelArtAnimation(pixelArts[3], new Vector3(1.6f, -1.4f), Vector3.right, speed: 0.5f, animLoops: 3);
        armyFAgents[armyFAgents.Count - 1].gameObject.SetActive(false);
        armyFAgents[armyFAgents.Count - 2].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);


        Debug.Log("4. ArmyF takes action");
        MoveAllTeamAgents(armyFAgents, new Vector3(2.2f, -1.3f));
        yield return new WaitUntil(() => AllAgentsReachedDestination(armyFAgents));
        yield return PlayPixelArtAnimation(pixelArts[12], new Vector3(2.2f, -1.3f), Vector3.right, speed: 0.5f, animLoops: 3);
        armyESubAgents1[armyESubAgents1.Count - 1].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);


        Debug.Log("5. ArmyF takes action");
        var (armyFSubAgents1, armyFSubAgents2) = SplitAgents(armyFAgents, 6);
        MoveAllTeamAgents(armyFSubAgents1, new Vector3(1.4f, 0.8f));
        yield return new WaitUntil(() => AllAgentsReachedDestination(armyFSubAgents1));
        yield return PlayPixelArtAnimation(pixelArts[32], new Vector3(1.4f, 0.8f) - new Vector3(1.2f, -0.5f), new Vector3(1.4f, 0.8f) - new Vector3(-0.2f, 1.0f), speed: 0.5f, animLoops: 3);
        armyESubAgents2[armyESubAgents2.Count - 1].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);


        Debug.Log("6. ArmyE takes action");
        var (armyESubAgents3, armyESubAgents4) = SplitAgents(armyESubAgents2, 5);
        MoveAllTeamAgents(armyESubAgents3, new Vector3(0.5f, 0.6f));
        yield return new WaitUntil(() => AllAgentsReachedDestination(armyESubAgents3));
        yield return PlayPixelArtAnimation(pixelArts[23], new Vector3(0.5f, 0.6f), new Vector3(1.4f, 0.8f) - new Vector3(0.5f, 0.6f), speed: 0.5f, animLoops: 3);
        armyFSubAgents1[armyFSubAgents1.Count - 1].gameObject.SetActive(false);
        armyFSubAgents1[armyFSubAgents1.Count - 2].gameObject.SetActive(false);


        yield return new WaitForSeconds(1.0f);

        Debug.Log("7. ArmyE takes action");
        MoveAllTeamAgents(armyESubAgents1, new Vector3(0.9f, -0.6f));
        yield return new WaitUntil(() => AllAgentsReachedDestination(armyESubAgents1));
        yield return PlayPixelArtAnimation(pixelArts[25], new Vector3(0.9f, -0.6f), Vector3.right, speed: 0.8f, animLoops: 8);


        yield return new WaitForSeconds(1.0f);


        Debug.Log("8. ArmyF takes action");
        var (armyFSubAgents3, armyFSubAgents4) = SplitAgents(armyFSubAgents2, 6);
        MoveAllTeamAgents(armyFSubAgents3, new Vector3(1.5f, -0.6f));
        MoveAllTeamAgents(armyFSubAgents4, new Vector3(2f, 0.25f));
        MoveAllTeamAgents(armyFSubAgents1, new Vector3(2f, 0.25f));

        yield return new WaitUntil(() => AllAgentsReachedDestination(armyFAgents));
        yield return PlayPixelArtAnimation(pixelArts[18], new Vector3(1.5f, -0.6f), new Vector3(1.5f, -0.6f) - new Vector3(0.9f, -0.6f), speed: 0.6f, animLoops: 4);
        armyESubAgents1[armyESubAgents1.Count - 2].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);

        Debug.Log("9. ArmyF takes action");
        yield return PlayPixelArtAnimation(pixelArts[30], new Vector3(2f, 0.25f) - new Vector3(1.2f, -0.5f), new Vector3(2f, 0.25f) - new Vector3(0.5f, 0.6f), speed: 0.5f, animLoops: 4);
        armyESubAgents3[armyESubAgents3.Count - 1].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);


        Debug.Log("10. ArmyE takes action");
        MoveAllTeamAgents(armyESubAgents1, new Vector3(0.7f, -0.5f));
        MoveAllTeamAgents(armyESubAgents3, new Vector3(0.7f, -0.5f));
        MoveAllTeamAgents(armyESubAgents4, new Vector3(0.4f, 0.15f));

        yield return new WaitUntil(() => AllAgentsReachedDestination(armyEAgents));

        yield return PlayPixelArtAnimation(pixelArts[29], new Vector3(0.4f, 0.15f) - new Vector3(-1.2f, -0.5f), new Vector3(2f, 0.25f) - new Vector3(0.4f, 0.15f), speed: 0.5f, animLoops: 4);
        armyFSubAgents4[armyFSubAgents4.Count - 3].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);

        Debug.Log("11. ArmyE takes action");

        yield return PlayPixelArtAnimation(pixelArts[13], new Vector3(0.7f, -0.5f), new Vector3(1.5f, -0.6f) - new Vector3(0.7f, -0.5f), speed: 0.6f, animLoops: 4);
        armyFSubAgents3[armyFSubAgents3.Count - 3].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);


        Debug.Log("ArmyF takes action");
        MoveAllTeamAgents(armyFSubAgents3, new Vector3(1.25f, -0.5f));
        MoveAllTeamAgents(armyFSubAgents4, new Vector3(1.9f, 0.35f));
        MoveAllTeamAgents(armyFSubAgents1, new Vector3(1.9f, 0.35f));

        yield return new WaitUntil(() => AllAgentsReachedDestination(armyFAgents));
        yield return PlayTwoPixelArtAnimations(pixelArts[5], new Vector3(0.7f, -0.5f), pixelArts[16], new Vector3(1.25f, -0.5f), speed1: 0.4f, animLoops1: 6, speed2: 0.4f, animLoops2: 8);
        armyESubAgents1[armyESubAgents1.Count - 3].gameObject.SetActive(false);
        armyFSubAgents3[armyFSubAgents3.Count - 4].gameObject.SetActive(false);

        yield return new WaitForSeconds(1.0f);


        yield return new WaitForSeconds(1.0f);
        yield return PlayTwoPixelArtAnimations(pixelArts[27], new Vector3(0.4f, 0.15f), pixelArts[30], new Vector3(1.9f, 0.35f) - new Vector3(1.2f, -0.0f), 
            direction1: new Vector3(1.9f, 0.35f) - new Vector3(0.4f, 0.15f), direction2: new Vector3(1.9f, 0.35f) - new Vector3(0.4f, 0.15f), speed1: 0.4f, animLoops1: 5, speed2: 0.4f, animLoops2: 6);
        armyESubAgents4[armyESubAgents4.Count - 2].gameObject.SetActive(false);
        armyESubAgents4[armyESubAgents4.Count - 3].gameObject.SetActive(false);
        yield return new WaitForSeconds(1.0f);

    }

    private void InitializePixelArts()
    {
        foreach (Transform child in pixelArtsParent)
        {
            pixelArts.Add(child.gameObject);
        }
    }

    private void InitializeTeamAgents(Transform parent, List<NavigateSoldier> teamAgents)
    {
        foreach (Transform child in parent)
        {
            NavigateSoldier agent = child.GetComponent<NavigateSoldier>();
            if (agent != null)
            {
                teamAgents.Add(agent);
            }
        }
    }

    private void MoveAllTeamAgents(List<NavigateSoldier> teamAgents, Vector3 destination)
    {
        foreach (NavigateSoldier agent in teamAgents)
        {
            if (agent.gameObject.activeSelf)
            {
                agent.SetSoldierDestination(destination);
            }
        }
    }

    private bool AllAgentsReachedDestination(List<NavigateSoldier> teamAgents)
    {

        foreach (NavigateSoldier agent in teamAgents)
        {
            if (agent.gameObject.activeSelf)
            {
                if (!agent.HasReachedDestination())
                {
                    return false;
                }

            }
        }
        return true;
    }

    private IEnumerator PlayPixelArtAnimation(GameObject pixelArt, Vector3 position, Vector3 direction = default(Vector3), float speed = 1f, int animLoops = 1)
    {
        // Calculate the direction vector from position to targetPosition
        if (direction == Vector3.zero)
        {
            direction = Vector3.right; // Default direction is to the right (0 degrees)
        }
        direction.z = 0; 

        // Calculate the angle in degrees
        float angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg;

        // Make a clone of an existing pixelart animation
        GameObject clone = Instantiate(pixelArt, position, Quaternion.Euler(0, 0, angle));
        clone.SetActive(true);
        Animator animator = clone.GetComponent<Animator>();
        animator.speed = speed;

        if (animator != null && animator.runtimeAnimatorController != null)
        {
            // Get the default animation clip
            AnimationClip[] clips = animator.runtimeAnimatorController.animationClips;

            if (clips.Length > 0)
            {
                // Wait for the animation to finish
                yield return new WaitForSeconds(clips[0].length / animator.speed * animLoops);
            }
        }
        
        Destroy(clone);
    }

    private IEnumerator PlayTwoPixelArtAnimations(GameObject pixelArt1, Vector3 position1, GameObject pixelArt2, Vector3 position2, Vector3 direction1 = default(Vector3), float speed1 = 1f, int animLoops1 = 1, Vector3 direction2 = default(Vector3), float speed2 = 1f, int animLoops2 = 1)
    {
        if (direction1 == Vector3.zero)
        {
            direction1 = Vector3.right;
        }
        direction1.z = 0;
        float angle1 = Mathf.Atan2(direction1.y, direction1.x) * Mathf.Rad2Deg;

        GameObject clone1 = Instantiate(pixelArt1, position1, Quaternion.Euler(0, 0, angle1));
        clone1.SetActive(true);
        Animator animator1 = clone1.GetComponent<Animator>();
        animator1.speed = speed1;

        if (direction2 == Vector3.zero)
        {
            direction2 = Vector3.right;
        }
        direction2.z = 0;
        float angle2 = Mathf.Atan2(direction2.y, direction2.x) * Mathf.Rad2Deg;

        GameObject clone2 = Instantiate(pixelArt2, position2, Quaternion.Euler(0, 0, angle2));
        clone2.SetActive(true);
        Animator animator2 = clone2.GetComponent<Animator>();
        animator1.speed = speed2;

        if (animator1 != null && animator1.runtimeAnimatorController != null && animator2 != null && animator2.runtimeAnimatorController != null)
        {
            // Get the default animation clip
            AnimationClip[] clips1 = animator1.runtimeAnimatorController.animationClips;
            AnimationClip[] clips2 = animator2.runtimeAnimatorController.animationClips;

            if (clips1.Length > 0 && clips2.Length > 0)
            {
                // Wait for the animation to finish
                yield return new WaitForSeconds(Mathf.Min(clips1[0].length / animator1.speed * animLoops1, clips2[0].length / animator2.speed * animLoops2));
            }
        }

        Destroy(clone1);
        Destroy(clone2);
    }


    private (List<NavigateSoldier>, List<NavigateSoldier>) SplitAgents(List<NavigateSoldier> ParentAgents, int Count)
    {
        var SubAgents = new List<NavigateSoldier>();
        var RemainingAgents = new List<NavigateSoldier>();
        var agentID = 0;
        foreach (var agent in ParentAgents)
        {
            if (agentID < Count)
            {
                SubAgents.Add(agent);
            }
            else
            {
                RemainingAgents.Add(agent);
            }
            agentID++;

        }
        return (SubAgents, RemainingAgents);
    }
}
