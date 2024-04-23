import uuid


def ceasefire_decision_maker(root_agent):
    def traverse(agent, level=1):
        if not agent:
            return None

        total_agents = 1
        command_structure_impact = 0  
        morale_collapse_impact = 0  
        heavy_casualties_count = 0
        total_troops = agent.profile.remaining_num_of_troops

        if agent.profile.current_stage == 'Crushing Defeat':
            morale_collapse_impact += 1 / level

        if agent.profile.current_stage != 'In Battle':
            command_structure_impact += 1 / level

        if agent.profile.remaining_num_of_troops < 50:
            heavy_casualties_count += 1

        for sub_agent in agent.hierarchy.sub_agents:
            child_results = traverse(sub_agent, level + 1)
            if child_results:
                total_agents += child_results['total_agents']
                command_structure_impact += child_results['command_structure_impact']
                morale_collapse_impact += child_results['morale_collapse_impact']
                heavy_casualties_count += child_results['heavy_casualties_count']
                total_troops += child_results['total_troops']

        heavy_casualties = heavy_casualties_count / total_agents if total_agents > 0 else 0

        return {
            'total_agents': total_agents,
            'command_structure_impact': command_structure_impact,
            'morale_collapse_impact': morale_collapse_impact,
            'heavy_casualties_count': heavy_casualties,
            'total_troops': total_troops
        }

    results = traverse(root_agent)
    decision = None
    if results['command_structure_impact'] > 0.8:
        decision = 'Breakdown of Command Structure'
    elif results['morale_collapse_impact'] > 0.8:
        decision = 'Morale Collapse'
    elif results['heavy_casualties_count'] > 0.8:
        decision = 'Heavy Casualties among High-Ranking Soldiers'

    # return decision
    return results, decision
