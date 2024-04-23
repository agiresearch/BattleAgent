import math


def vision_decoder(visionRequest_agent, shuffled_agent_list, extCallType = None):
    # Decode the vision information of the agent
    mutual_position_dict = AgentInfoCollector(shuffled_agent_list, visionRequest_agent)
    vision_info = mutual_position_dict
    return vision_info
    
    
def AgentInfoCollector(shuffled_agent_list, request_agent, threshold_distance = 100000):
    def calculate_distance_and_bearing(from_position, to_position):
        # Calculate the Euclidean distance and round to one decimal place
        distance = round(math.sqrt((to_position[0] - from_position[0]) ** 2 + (to_position[1] - from_position[1]) ** 2), 1)
        angle = math.atan2(to_position[1] - from_position[1], to_position[0] - from_position[0])
        bearing = round(math.degrees(angle), 1)
        return distance, bearing
    
    request_agent_position = request_agent.profile.position
    request_agent_id = request_agent.hierarchy.id
    results = {'self': {"id": request_agent_id, "position": request_agent_position}, 'friendly': [], 'enemy': []}

    for agent in shuffled_agent_list:
        if agent.hierarchy.id == request_agent.hierarchy.id:
            continue

        distance, bearing = calculate_distance_and_bearing(request_agent_position, agent.profile.position)
        remaining_num = agent.profile.remaining_num_of_troops
        current_action =  agent.profile.current_action
        
        agent_info = {'agent_id': agent.hierarchy.id, 'distance': distance, 'bearing': bearing, "remaining number": remaining_num, "current action": current_action}

        # vision filter 
        vision_enable_flag = vision_filter(agent)
        if not vision_enable_flag:
            continue
        
        if agent.profile.identity == request_agent.profile.identity:
            results['friendly'].append(agent_info)
        else:
            results['enemy'].append(agent_info)
            
    # Filter out agents beyond specified distance
    results['friendly'] = [agent_info for agent_info in results['friendly'] if agent_info['distance'] <= threshold_distance]
    results['enemy'] = [agent_info for agent_info in results['enemy'] if agent_info['distance'] <= threshold_distance]

    return results


def vision_filter(agent):
    vision_enable_flag = True
    """_summary_

    Args:
        agent (_type_): _description_

    Returns:
        bool: whether the agent is visible to the agent
    """
    if agent.mergedOrPruned:
        return False
    
    if agent.profile.current_stage in ["Crushing Defeat", "fleeing Off the Map"]:
        return False
    
    if agent.profile.remaining_num_of_troops <= 0:
        return False

    return vision_enable_flag