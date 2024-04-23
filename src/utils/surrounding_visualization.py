import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as mcolors 
import matplotlib.cm as cm

def polar_to_cartesian(distance, bearing):
    radians = np.deg2rad(bearing)
    x = distance * np.cos(radians)
    y = distance * np.sin(radians)
    return x, y

def plot_tactical_positions(data, img_save_path = "logs", img_name = "tactical_positions_plot", img_format = "png"):
    """
    Plots tactical positions of self, friendly, and enemy units based on the provided data structure.
    
    Parameters:
    - data (dict): A dictionary containing the positions and statuses of self, friendly, and enemy units.
    """
    # Extract positions and convert polar coordinates to cartesian
    self_position = np.array(data['self']['position'])
    friendly_positions = np.array([[f['distance'], f['bearing']] for f in data['friendly']])
    enemy_positions = np.array([[e['distance'], e['bearing']] for e in data['enemy']])
    
    friendly_cartesian_positions = np.array([polar_to_cartesian(d, b) for d, b in friendly_positions])
    enemy_cartesian_positions = np.array([polar_to_cartesian(d, b) for d, b in enemy_positions])
    
    # Plotting
    plt.figure(figsize=(10, 10))
    plt.plot(self_position[0], self_position[1], 'bo', markersize=10, label='Self Position')
    if len(friendly_cartesian_positions) > 0:
        plt.plot(friendly_cartesian_positions[:, 0], friendly_cartesian_positions[:, 1], 'go', label='Friendly Positions')
        for i, (x, y) in enumerate(friendly_cartesian_positions, start=1):
            # plt.text(x, y, f'Friendly {i}', horizontalalignment='right')
            plt.text(x, y, f'', horizontalalignment='right')
    if len(enemy_cartesian_positions) > 0:
        plt.plot(enemy_cartesian_positions[:, 0], enemy_cartesian_positions[:, 1], 'ro', label='Enemy Positions')
        for i, (x, y) in enumerate(enemy_cartesian_positions, start=1):
            plt.text(x, y, f'', horizontalalignment='right')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Tactical Positioning with Friendly and Enemy Forces')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')


    if not os.path.exists(img_save_path):
        os.makedirs(img_save_path)

    file_name = f"{img_name}.{img_format}"
    file_path = os.path.join(img_save_path, file_name)

    plt.savefig(file_path)
    plt.close() 

    return 

if __name__ == '__main__':
    test_data = {'self': {'id': 'ARMY-74fe6080', 'position': [0, 15]}, 'friendly': [{'agent_id': 'ARMY-7daf4081', 'distance': 22.4, 'bearing': 26.6, 'remaining number': 240, 'current action': 'Reposition Forces Moving to higher ground to gain a strategic advantage for deploying longbows.'}, {'agent_id': 'ARMY-10f1179a', 'distance': 18.0, 'bearing': 56.3, 'remaining number': 200, 'current action': 'Conduct Reconnaissance'}, {'agent_id': 'ARMY-c19b8322', 'distance': 11.2, 'bearing': 26.6, 'remaining number': 900, 'current action': 'Reposition Forces Moving to a more advantageous position to counter enemy flanking maneuvers.'}, {'agent_id': 'ARMY-a149079a', 'distance': 10.0, 'bearing': -90.0, 'remaining number': 0, 'current action': 'Fortify Position Continuing to strengthen defenses at current location to resist enemy attacks and provide support to friendly units.'}, {'agent_id': 'ARMY-1ae0d8c9', 'distance': 0.0, 'bearing': 0.0, 'remaining number': 180, 'current action': 'Deploy Longbows'}, {'agent_id': 'ARMY-4c500870', 'distance': 25.0, 'bearing': 36.9, 'remaining number': 50, 'current action': 'Construct Defenses'}, {'agent_id': 'ARMY-52bc122e', 'distance': 5.0, 'bearing': 90.0, 'remaining number': 2500, 'current action': 'Deploy Longbows Continuing to deploy longbowmen to harass enemy flanking maneuvers and protect against cavalry charges.'}, {'agent_id': 'ARMY-c9f5bbcf', 'distance': 20.6, 'bearing': 14.0, 'remaining number': 100, 'current action': 'Reposition Forces Repositioning to a location that provides a strategic advantage for an ambush using longbows, supporting friendly units against enemy flanking maneuvers and cavalry charge.'}, {'agent_id': 'ARMY-1af943c9', 'distance': 25.0, 'bearing': 36.9, 'remaining number': 50, 'current action': 'Support Friendly Units'}, {'agent_id': 'ARMY-a7d4cfab', 'distance': 25.0, 'bearing': 36.9, 'remaining number': 100, 'current action': 'Deploy Longbows'}, {'agent_id': 'ARMY-fc5f1de3', 'distance': 25.0, 'bearing': 36.9, 'remaining number': 0, 'current action': 'Reposition Forces Moving to higher ground to gain a strategic advantage for deploying longbows and constructing defenses.'}, {'agent_id': 'ARMY-3fccb570', 'distance': 5.0, 'bearing': 90.0, 'remaining number': 1050, 'current action': 'Reposition Forces'}, {'agent_id': 'ARMY-6c871d86', 'distance': 33.5, 'bearing': 26.6, 'remaining number': 100, 'current action': 'Conduct Reconnaissance Gathering intelligence on enemy movements and positions, avoiding direct engagement, and providing strategic information to the main force.'}, {'agent_id': 'ARMY-650377bd', 'distance': 10.0, 'bearing': -90.0, 
    'remaining number': 200, 'current action': 'Support Friendly Units'}, {'agent_id': 'ARMY-a3fe287d', 'distance': 10.0, 'bearing': -90.0, 'remaining number': 300, 'current action': 'Deploy Longbows'}, {'agent_id': 'ARMY-e733a690', 'distance': 0.0, 'bearing': 0.0, 'remaining number': 120, 'current action': 'Deploy Longbows Deploying longbowmen to a strategic position to counter enemy cavalry charge and disrupt flanking maneuvers.'}, {'agent_id': 'ARMY-e9626295', 'distance': 10.0, 'bearing': -90.0, 'remaining number': 200, 'current action': 'Support Friendly Units'}], 'enemy': [{'agent_id': 'ARMY-83cce6ba', 'distance': 119.3, 'bearing': -33.0, 'remaining number': 12889, 'current action': 'Execute Flanking Maneuvers Using the cover of ForestF to approach and engage enemy longbowmen in close combat, minimizing exposure to long-range fire.'}, {'agent_id': 'ARMY-bbcd6024', 'distance': 119.3, 'bearing': -33.0, 'remaining number': 10800, 'current action': 'Charge Cavalry'}]}
    plot_tactical_positions(test_data)

