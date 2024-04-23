from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *


battle_end_conditions = {
    "Morale Collapse": {
        "description": "Collapse of morale, accompanied by desertion or surrender of soldiers.",
        "indicator": "rapid decrease in soldier morale and increase in desertion rates",
        "impact": "critical weakening of fighting capacity",
        "measurement": "monitoring morale levels and desertion incidents"
    },
    "Breakdown of Command Structure": {
        "description": "Disintegration of the command structure.",
        "indicator": "loss of effective communication and command control",
        "impact": "disruption in strategic and tactical operations",
        "measurement": "assessment of command chain integrity and operational efficiency"
    },
    "Important Geographic Locations": {
        "description": "Loss of key defensive lines or crucial geographical positions.",
        "indicator": "enemy occupation or uncontested control of strategic locations",
        "impact": "compromised defense and potential territorial losses",
        "measurement": "surveillance of key locations and defense line status"
    },
    "Heavy Casualties among High-Ranking Soldiers": {
        "description": "Significant casualties among high-ranking soldiers.",
        "indicator": "high rate of casualties among officers and leadership",
        "impact": "loss of leadership and potential decline in operational effectiveness",
        "measurement": "casualty reports and status updates of high-ranking personnel"
    }
}

action_list = NamedBlock(
    refname="action_list",
    name="Military Strategy Action List",
    content=Collection(
        NamedVariable(
            refname="Espionage",
            name="Information Gathering in Espionage",
            content="""
Required action input: "null"
Action effects: 
(1) Simplify information gathering to get closest enemy info at a certain speed
(2) Details include number of enemies, weapons, and after a set time, refined details from vision decoder
(3) Helps in formulating a strategic approach based on enemy's strength and capabilities
""",
        ),
        NamedVariable(
            refname="Deploy",
            name="Strategic Squad Deployment",
            content="""
Required action input: Details of each squad (number of people, mission, direction)
Action effects: 
(1) Agent splits into several squads based on the mission's requirements
(2) Each squad is assigned specific tasks and directions for optimal positioning and effectiveness
action format:
1.Squad Composition: Determine the type and number of troops in each squad.
2.Mission Assignment: Assign specific tasks and objectives to each squad.
3.Directional Deployment: Allocate directional movement to squads, choosing from East, South, West, North, Northeast, Southeast, Southwest, Northwest.
4.Movement Strategy: Specify the distance each squad should move to achieve optimal positioning for their assigned tasks.
""",
        ),
        NamedVariable(
            refname="Pre-battle_Defense_Strategy",
            name="Preparing Defensive Measures",
            content="""
Required action input: "null"
Action effects: 
(1) Involves setting up defensive measures like traps, and deciding on strategies
(2) Prepares the troops for potential enemy attacks and strengthens defensive positions
""",
        ),
        NamedVariable(
            refname="War_Confirmation",
            name="Decision Making at War's Brink",
            content="""
Required action input: "null"
Action effects: 
(1) Decision-making process when within battle range
(2) Based on known information, decide whether to attack or retreat
""",
        ),
        NamedVariable(
            refname="Declare_Battle",
            name="Official Battle Commencement",
            content="""
Required action input: "null"
Action effects: 
(1) Official start of the battle against the enemy
(2) Signals troops to begin the attack based on the strategy
""",
        ),
        NamedVariable(
            refname="Attack",
            name="Executing the Attack",
            content="""
Required action input: "null"
Action effects: 
(1) Execution of the battle plan using designated weapons and manpower
(2) Engages the enemy in combat with the goal of overpowering them
""",
        ),
        NamedVariable(
            refname="Retreat_After_Defeat",
            name="Strategic Withdrawal Post-Defeat",
            content="""
Required action input: "null"
Action effects: 
(1) If the battle is unfavorable, retreat and regroup or stay put if no visibility of allies
(2) Aims to minimize losses and re-strategize for future engagements
""",
        ),
        
    NamedVariable(
    refname="General_Retreat",
    name="General Retreat Procedure",
    content="""
Required action input: "null"
Action effects: 
(1) After thorough assessment, initiate a general retreat based on the situational needs.
(2) Coordinate the retreat process across all fronts, ensuring safe withdrawal from enemy engagement.
(3) Implement protective measures to safeguard retreating troops, minimizing losses during withdrawal.
(4) Designate strategic rendezvous points for regrouping and reassessing the situation post-retreat.
""",
)
        # Additional actions can be added here following the same structure
    ),
)




# number of action_property_definition: 53
action_property_definition = {
    "Wait without Action": {
        "publicity": "public",
        "input": {
            "initiator": "commanding_officer",
            "location": "current_position",
            "recipient": "own_units"
        },
        "prompt": "hold position",
        "require_response": False
    },
    "Reposition Forces": {
        "publicity": "public",
        "input": {
            "initiator": "field_commander",
            "location": "map_coordinates",
            "recipient": "military_units"
        },
        "prompt": "relocate to",
        "require_response": False
    },
    "Initiate Skirmish": {
        "publicity": "public",
        "input": {
            "initiator": "squad_leader",
            "location": "engagement_area",
            "recipient": "enemy_unit"
        },
        "prompt": "attack",
        "require_response": False
    },
    "Deploy Longbows": {
        "publicity": "public",
        "input": {
            "initiator": "archery_commander",
            "location": "target_zone",
            "recipient": "opposing_forces"
        },
        "prompt": "deploy at",
        "require_response": False
    },
    "Charge Cavalry": {
        "publicity": "public",
        "input": {
            "initiator": "cavalry_captain",
            "location": "enemy_flank",
            "recipient": "enemy_troops"
        },
        "prompt": "advance into",
        "require_response": False
    },
    "Ambush Enemy": {
        "publicity": "non-public",
        "input": {
            "initiator": "special_operations_leader",
            "location": "enemy_path",
            "recipient": "unsuspecting_enemy"
        },
        "prompt": "ambush at",
        "require_response": False
    },
    "Construct Defenses": {
        "publicity": "public",
        "input": {
            "initiator": "engineering_corps",
            "location": "designated_site",
            "recipient": "defensive_positions"
        },
        "prompt": "build defenses at",
        "require_response": False
    },
    #PART 2
    "Rally Troops": {
        "publicity": "public",
        "input": {
            "initiator": "unit_commander",
            "location": "troop_gathering_point",
            "recipient": "own_troops"
        },
        "prompt": "rally at",
        "require_response": False
    },
    "Retreat and Regroup": {
        "publicity": "public",
        "input": {
            "initiator": "battalion_leader",
            "location": "safe_zone",
            "recipient": "engaged_units"
        },
        "prompt": "withdraw to",
        "require_response": False
    },
    "Launch Full Assault": {
        "publicity": "public",
        "input": {
            "initiator": "general",
            "location": "enemy_stronghold",
            "recipient": "enemy_defenses"
        },
        "prompt": "assault",
        "require_response": False
    },
    "Fortify Position": {
        "publicity": "public",
        "input": {
            "initiator": "defense_coordinator",
            "location": "occupied_territory",
            "recipient": "strategic_points"
        },
        "prompt": "fortify",
        "require_response": False
    },
    "Employ Artillery": {
        "publicity": "public",
        "input": {
            "initiator": "artillery_commander",
            "location": "targeted_sector",
            "recipient": "enemy_positions"
        },
        "prompt": "deploy artillery on",
        "require_response": False
    },
    "Archery Duel": {
        "publicity": "public",
        "input": {
            "initiator": "archer_squad_leader",
            "location": "battlefield",
            "recipient": "enemy_archers"
        },
        "prompt": "engage in archery duel with",
        "require_response": False
    },
    "Cavalry Charge": {
        "publicity": "public",
        "input": {
            "initiator": "cavalry_commander",
            "location": "enemy_frontline",
            "recipient": "enemy_infantry"
        },
        "prompt": "execute charge towards",
        "require_response": False
    },
    # PART 3
    "Prepare Defenses": {
        "publicity": "public",
        "input": {
            "initiator": "defensive_strategy_leader",
            "location": "vulnerable_site",
            "recipient": "defense_structures"
        },
        "prompt": "prepare defenses at",
        "require_response": False
    },
    "Set Traps": {
        "publicity": "non-public",
        "input": {
            "initiator": "trap_specialist",
            "location": "enemy_travel_routes",
            "recipient": "enemy_patrols"
        },
        "prompt": "set traps along",
        "require_response": False
    },
    "Siege Tactics": {
        "publicity": "public",
        "input": {
            "initiator": "siege_master",
            "location": "enemy_fortress",
            "recipient": "fortified_walls"
        },
        "prompt": "apply siege tactics on",
        "require_response": False
    },
    "Use of Gunpowder Weapons": {
        "publicity": "public",
        "input": {
            "initiator": "gunpowder_unit_commander",
            "location": "targeted_sector",
            "recipient": "enemy_battalions"
        },
        "prompt": "use gunpowder weapons on",
        "require_response": False
    },
    "Hand-to-Hand Combat": {
        "publicity": "public",
        "input": {
            "initiator": "combat_unit_leader",
            "location": "close_combat_zone",
            "recipient": "enemy_soldiers"
        },
        "prompt": "engage in hand-to-hand combat in",
        "require_response": False
    },
    "Tactical Retreat": {
        "publicity": "public",
        "input": {
            "initiator": "unit_commander",
            "location": "fallback_position",
            "recipient": "own_forces"
        },
        "prompt": "execute tactical retreat to",
        "require_response": False
    },
    "Counterattack": {
        "publicity": "public",
        "input": {
            "initiator": "counterattack_leader",
            "location": "enemy_weak_spot",
            "recipient": "advancing_enemy"
        },
        "prompt": "launch counterattack on",
        "require_response": False
    },

    "Conduct Reconnaissance": {
        "publicity": "non-public",
        "input": {
            "initiator": "scout_leader",
            "location": "enemy_formation",
            "recipient": "enemy_movements"
        },
        "prompt": "conduct reconnaissance of",
        "require_response": True
    },
    #PART 5
        "Create Decoy Units": {
        "publicity": "non-public",
        "input": {
            "initiator": "deception_strategy_leader",
            "location": "key_strategic_points",
            "recipient": "decoy_targets"
        },
        "prompt": "create decoys near",
        "require_response": False
    },
    "Fortify Rear Guard": {
        "publicity": "public",
        "input": {
            "initiator": "rear_guard_commander",
            "location": "retreat_paths",
            "recipient": "defensive_positions"
        },
        "prompt": "fortify along",
        "require_response": False
    },
    "Direct Artillery Fire": {
        "publicity": "public",
        "input": {
            "initiator": "artillery_director",
            "location": "enemy_formations",
            "recipient": "targeted_enemy_units"
        },
        "prompt": "direct fire at",
        "require_response": False
    },
    "Conduct Feigned Retreats": {
        "publicity": "public",
        "input": {
            "initiator": "tactical_retreat_commander",
            "location": "enemy_trap",
            "recipient": "pursuing_enemy"
        },
        "prompt": "conduct retreat into",
        "require_response": False
    },
    "Employ Scorched Earth Tactics": {
        "publicity": "public",
        "input": {
            "initiator": "scorched_earth_strategy_leader",
            "location": "resource_areas",
            "recipient": "enemy_supply_sources"
        },
        "prompt": "implement tactics on",
        "require_response": False
    },
    "Implement Guerilla Warfare": {
        "publicity": "non-public",
        "input": {
            "initiator": "guerilla_warfare_leader",
            "location": "enemy_patrols",
            "recipient": "guerilla_targets"
        },
        "prompt": "engage against",
        "require_response": False
    },
    "Engage in Siege Warfare": {
        "publicity": "public",
        "input": {
            "initiator": "siege_commander",
            "location": "fortified_targets",
            "recipient": "siege_objectives"
        },
        "prompt": "engage in siege on",
        "require_response": False
    },
    "Organize Raiding Parties": {
        "publicity": "non-public",
        "input": {
            "initiator": "raiding_party_leader",
            "location": "enemy_supply_lines",
            "recipient": "raid_targets"
        },
        "prompt": "organize raids on",
        "require_response": False
    },
    #PART 6
    "Establish Defensive Fortifications": {
        "publicity": "public",
        "input": {
            "initiator": "defensive_engineer",
            "location": "strategic_locations",
            "recipient": "defensive_structures"
        },
        "prompt": "build fortifications at",
        "require_response": False
    },
    "Execute Flanking Maneuvers": {
        "publicity": "public",
        "input": {
            "initiator": "flank_commander",
            "location": "enemy_flanks",
            "recipient": "flank_targets"
        },
        "prompt": "execute maneuvers on",
        "require_response": False
    },
    "Create Diversions": {
        "publicity": "public",
        "input": {
            "initiator": "diversion_planner",
            "location": "key_enemy_areas",
            "recipient": "diversion_targets"
        },
        "prompt": "create diversions near",
        "require_response": False
    },
    "Implement Supply Chain Disruption": {
        "publicity": "non-public",
        "input": {
            "initiator": "supply_disruption_leader",
            "location": "enemy_supply_routes",
            "recipient": "supply_disruption_targets"
        },
        "prompt": "disrupt supply chains on",
        "require_response": False
    },
    "Use Cavalry for Shock Tactics": {
        "publicity": "public",
        "input": {
            "initiator": "cavalry_tactics_commander",
            "location": "enemy_lines",
            "recipient": "shock_tactic_targets"
        },
        "prompt": "use cavalry for shock tactics into",
        "require_response": False
    },
    "Develop Counter-Siege Measures": {
        "publicity": "public",
        "input": {
            "initiator": "counter_siege_specialist",
            "location": "siege_locations",
            "recipient": "siege_countermeasures"
        },
        "prompt": "develop measures at",
        "require_response": False
    },
    "Implement Decoy Strategies": {
        "publicity": "non-public",
        "input": {
            "initiator": "deception_commander",
            "location": "decoy_areas",
            "recipient": "deception_targets"
        },
        "prompt": "implement decoy strategies in",
        "require_response": False
    },
    "Form Defensive Shields": {
        "publicity": "public",
        "input": {
            "initiator": "shield_formation_leader",
            "location": "troop_formations",
            "recipient": "defensive_positions"
        },
        "prompt": "form shields among",
        "require_response": False
    },
    "Create Obstacles for Enemy Cavalry": {
        "publicity": "public",
        "input": {
            "initiator": "obstacle_designer",
            "location": "charge_paths",
            "recipient": "enemy_cavalry"
        },
        "prompt": "create obstacles on",
        "require_response": False
    },
    "Employ Archers": {
        "publicity": "public",
        "input": {
            "initiator": "archer_unit_commander",
            "location": "enemy_units",
            "recipient": "archery_targets"
        },
        "prompt": "employ archers against",
        "require_response": False
    },
    "Form Defensive Pike Formations": {
        "publicity": "public",
        "input": {
            "initiator": "pike_formation_leader",
            "location": "vulnerable_points",
            "recipient": "defensive_areas"
        },
        "prompt": "form pike formations around",
        "require_response": False
    }

}




if __name__ == '__main__':
    # print(action_property_definition)
    # print(len(action_property_definition.keys()))
    print(format_prompt(action_list,{}))