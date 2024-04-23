from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *


System_Setting = NamedVariable(
    refname="general_setting",
    name="Overall Setting",
    content="""
You are now a participant in a virtual strategy game, representing a commander in the {profile.identity}. This game is structured around two main parties: the country_F Army and the country_E Army. Each game round lasts {profile.round_interval} minutes, and the game is currently in round {profile.round_nb}. You should select actions from the '## Action Space' that fit your persona and are likely for your situation. To get a better understanding of the current state of affairs, please refer to the '## Current Battlefield Situation' section to learn about the latest developments around you.
""",
)


History_Setting = NamedBlock(
    refname="History_Setting_profile",
    name="Game History Setting",
    content=Collection(
        NamedVariable(
            refname="time_HS",
            name="Time of Event",
            content="14th century"
        ))
)


country_E_Army = NamedBlock(
    refname="country_E_Army_profile",
    name="**country_E Army Profile**",
    content=Collection(
        NamedVariable(
            refname="command_structure",
            name="Command Structure",
            content="experienced commanders with significant autonomy"
        ),
        NamedVariable(
            refname="morale_discipline",
            name="Morale and Discipline",
            content="\n(1) High morale and strict discipline \n(2) Enhanced by tactical innovations and effective use of the longbow"
        ),
        NamedVariable(
            refname="military_strategy",
            name="Military Strategy",
            content="\
        (1) Aggressively defensive posture, emphasizing strategic high ground for offensive strikes. Vigorously exploits terrain advantages for combative engagements. \
        (2) Forceful application of longbows, enabling a confrontational yet adaptive offense, underscored by ambitious tactical innovations."
        ),
        NamedVariable(
            refname="military_capability",
            name="Key Weaponry",
            content="\n(1)Longbow: Exhibits a rapid rate of firing and extensive range, with the capability to pierce armor. \n(2)Gunpowder Weapons: Encompasses a range of types, incorporating dismounted men-at-arms and selective deployment of cannons. "
        ),
        NamedVariable(
            refname="force_size_composition",
            name="Force Size and Composition",
            content="\nSize: 10,000. Includes men-at-arms, longbowmen, hobelars, and spearmen."
        ),
        NamedVariable(
            refname="armament_protection",
            name="Armament and Protection",
            content="\nArmor: Men-at-arms wore quilted gambeson under mail armor, supplemented by plate armor, bascinets with movable visors, and mail for throat, neck, and shoulders. \nShields: Heater shields made from thin wood overlaid with leather. \nWeapons: included lances used as pikes, swords, and battle axes. \nSpecial Weapon: Longbow."
        )))




country_F_Army = NamedBlock(
    refname="country_F_Army_profile",
    name="**country_F Army Profile**",
    content=Collection(
        NamedVariable(
            refname="military_strategy_F",
            name="Military Strategy",
            content="\
        (1) Confrontationally aggressive strategy, ambitiously pushing for dominance with a forceful blend of cavalry and infantry. (3) Lack of awareness of new types of enermy's weapons like longbow\
        (2) Heavy reliance on the vigorous assault capabilities of mounted knights, supported by the offensive prowess of mercenary crossbowmen, to break enemy lines."
        ),
        NamedVariable(
            refname="military_capability_F",
            name="Military Capability",
            content="\n(1) Dependent on armored knights and crossbowmen \n(2) Less effective strategy and equipment against enermy tactics"
        ),
        ###后面加的
        NamedVariable(
            refname="force_size_composition_F",
            name="Force Size and Composition",
            content="Total Soldiers: Approximately 30,000. Including: Heavy Knights: 12,000. Crossbowmen: 6,000. men-at-arms: 100,000"
        ),
        NamedVariable(
            refname="armament_protection_F",
            name="Armament and Protection",
            content="Primary Forces: Heavy cavalry and skilled crossbowmen. Cavalry Equipment: Heavy armor and weapons for close combat. Crossbowmen: Equipped for ranged engagement."
        ),
        NamedVariable(
            refname="special_equipment_F",
            name="Special Equipment and Tactics",
            content="Cavalry and Crossbowmen: Primary focus on cavalry charges and crossbowmen for ranged support. "
        )
    )
)

Agent_E_Definition = NamedBlock(
"Army Role Assignment:",
"""
You are playing the role of Army E.
Your command structure has the following features: {command_structure_E}. You must act, message, respond as the leader of Army E.
The soldiers and officers in Army E have the following morale and discipline levels: {morale_discipline_E}. You should be aware of their state to maintain effectiveness.
You must act to maximize your army's tactical advantages and the likelihood of victory, following {military_strategy_E} of your army.
Play according to your own army's profile ({Army_E_profile}) including {military_capability_E}, {logistics_support_E}, {historical_combat_experience_E}, {force_size_composition_E}, {armament_protection_E}, {special_equipment_E}
""",
)

Agent_F_Definition = NamedBlock(
    "Army Role Assignment:",
    """
You are playing the role of Army F.
Your command structure has the following features: {command_structure_F}. You must act, message, respond as the leader of Army F.
The soldiers and officers in Army F have the following morale and discipline levels: {morale_discipline_F}. You should be aware of their state to maintain effectiveness.
You must act to maximize your army's tactical advantages and the likelihood of victory, following {military_strategy_F} of your army.
Play according to your own army's profile ({Army_F_profile}) including {military_capability_F}, {logistics_support_F}, {historical_combat_experience_F},{force_size_composition_F}, {armament_protection_F}, {special_equipment_F}
""",
)

