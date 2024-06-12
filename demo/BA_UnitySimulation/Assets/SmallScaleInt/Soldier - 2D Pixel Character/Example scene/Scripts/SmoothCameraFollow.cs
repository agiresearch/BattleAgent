using UnityEngine;

namespace SmallScaleInteractive._2DCharacter
{
    public class SmoothCameraFollow : MonoBehaviour
    {
        public Transform target; // The target the camera should follow
        public float smoothTime = 0.3f; // Time it takes to smooth the position
        public Vector3 offset; // Offset from the target

        private Vector3 velocity = Vector3.zero; // Velocity, used by SmoothDamp

        void LateUpdate()
        {
            if (target == null) return;

            // Calculate the position the camera is trying to reach
            Vector3 targetPosition = target.position + offset;

            // Smoothly move the camera towards that position
            Vector3 newPosition = Vector3.SmoothDamp(transform.position, targetPosition, ref velocity, smoothTime);

            // Assign the new position to the camera. Force z position to maintain a fixed offset
            transform.position = new Vector3(newPosition.x, newPosition.y, offset.z);
        }
    }
}
