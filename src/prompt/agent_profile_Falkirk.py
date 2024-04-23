from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *


System_Setting_Falkirk = NamedVariable(
    refname="general_setting",
    name="Overall Setting",
    content="""
You are now a participant in a virtual strategy game, representing a commander in the {profile.identity}. This game is structured around two main parties: the country_F Army and the country_E Army. Each game round lasts {profile.round_interval} minutes, and the game is currently in round {profile.round_nb}. You should select actions from the '## Action Space' that fit your persona and are likely for your situation. To get a better understanding of the current state of affairs, please refer to the '## Current Battlefield Situation' section to learn about the latest developments around you.
""",
)


History_Setting_Falkirk = NamedBlock(
    refname="History_Setting_profile",
    name="Game History Setting",
    content=Collection(
        NamedVariable(
            refname="time_HS",
            name="Time of Event",
            content="Summer of 1298"
        )
        )
)


country_E_Army_Falkirk = NamedBlock(
    refname="country_E_Army_profile",
    name="**country_E Army Profile**",
    content=Collection(
        NamedVariable(
            refname="command_structure_E",
            name="Command Structure",
            content="Experienced military commanders with well-defined roles"
        ),
        NamedVariable(
            refname="morale_discipline_E",
            name="Morale and Discipline",
            content="\n(1) High morale, bolstered by recent successes in battles \n(2) Strict discipline and well-organized army structure"
        ),
        # NamedVariable(
        #     refname="military_strategy_E",
        #     name="Military Strategy",
        #     content="\n(1) Offensive strategy with a focus on utilizing longbowmen effectively \n(2) Tactical deployment of cavalry to exploit weaknesses in the enemy formation"
        # ),
        NamedVariable(
            refname="military_strategy_E",
            name="Military Strategy",
            content="\n(1) Offensive strategy with a focus on utilizing longbowmen to decisively eliminate the enemy forces.\n(2) Aggressively deploy cavalry to exploit and devastate any weaknesses in the enemy formation"
        ),
        NamedVariable(
            refname="military_capability_E",
            name="Key Weaponry",
            content="\n(1) Key Weapon: Longbow, used to disrupt enemy formations \n(2) Combination of cavalry and infantry, with an emphasis on coordinated attacks"
        ),
        NamedVariable(
            refname="force_size_composition_E",
            name="Force Size and Composition",
            content="\nSize Estimate: Approximately 15,000 \nComposition: a large contingent of longbowmen, supported by cavalry and infantry units."
        ),
        NamedVariable(
            refname="armament_protection_E",
            name="Armament and Protection",
            content="\nArmor: Combination of plate and chainmail for knights and men-at-arms. \nShields: Primarily used by infantry. \nWeapons: Longbows, swords, spears, and other medieval weaponry."
        )))


country_F_Army_Falkirk = NamedBlock(
    refname="country_F_Army_profile",
    name="**country_F Army Profile**",
    content=Collection(
        NamedVariable(
            refname="command_structure_F",
            name="Command Structure",
            content="\n(1) Supreme Commander: a very experienced, brave, well-respected commander \n(2) Subordinate Leaders: Various local nobles with regional influence"
        ),
        NamedVariable(
            refname="morale_discipline_F",
            name="Morale and Discipline",
            content="\n(1) High morale driven by the struggle for their country independence \n(2) Challenges in maintaining discipline due to diverse composition of the army"
        ),
        NamedVariable(
            refname="military_strategy_F",
            name="Military Strategy",
            # content="\n(1) Offensive strategy focused on using terrain and formation to advantage \n(2) Reliance on the schiltron formation to counter enemy cavalry"
            content="\n(1) Aggressive offensive strategy leveraging terrain and formation superiority to dominate the battlefield.\n(2) Unyielding reliance on the schiltron formation to aggressively annihilate enemy cavalry, ensuring their total defeat"
        ),
        NamedVariable(
            refname="military_capability_F",
            name="Key Weaponry",
            content="\n(1) Main strength in infantry, particularly spearmen \n(2) Limited cavalry and archery capabilities compared to the enemy"
        ),
        NamedVariable(
            refname="force_size_composition_F",
            name="Force Size and Composition",
            content="\nSize Estimate: Around 6,000 \nComposition: Largely made up of infantry, including spearmen and a small number of archers and light cavalry."
        ),
        NamedVariable(
            refname="armament_protection_F",
            name="Armament and Protection",
            content="\nArmor: Generally light, to enhance mobility. \nShields: Used by spearmen and other infantry. \nWeapons: Primarily spears, with swords and axes for close combat."
        )
    )
)

