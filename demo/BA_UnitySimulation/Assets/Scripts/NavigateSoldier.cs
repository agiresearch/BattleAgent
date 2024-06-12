using NavMeshPlus.Extensions;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class NavigateSoldier : MonoBehaviour
{
    //[SerializeField] Transform target;
    NavMeshAgent navMeshAgent;

    // Start is called before the first frame update
    void Start()
    {
        navMeshAgent = GetComponent<NavMeshAgent>();
        navMeshAgent.updateRotation = false;
        navMeshAgent.updateUpAxis = false;
        if (navMeshAgent == null)
        {
            Debug.LogError("NavMeshAgent component at Start function is null on " + gameObject.name);
        }
    }

    // Update is called once per frame
    void Update()
    {
        // SetSoldierDestination(target.position);
    }

    public void SetSoldierDestination(Vector3 destination)
    {
        if (navMeshAgent != null)
        {
            navMeshAgent.SetDestination(destination);
        }
    }

    public bool HasReachedDestination()
    {

        navMeshAgent = GetComponent<NavMeshAgent>();
        if (navMeshAgent == null)
        {
            Debug.LogError("NavMeshAgent component is null on " + gameObject.name);
            return false;
        }

        // Check if the agent has reached its destination
        return !navMeshAgent.pathPending &&
               navMeshAgent.remainingDistance <= navMeshAgent.stoppingDistance * 2.5f && //navMeshAgent.velocity <= 0.05
               navMeshAgent.pathStatus == NavMeshPathStatus.PathComplete;
    }
}
