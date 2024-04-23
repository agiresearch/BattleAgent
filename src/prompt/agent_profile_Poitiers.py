from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *


from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *


System_Setting_Poitiers = NamedVariable(
    refname="general_setting",
    name="Overall Setting",
    content="""
You are now a participant in a virtual strategy game, representing a commander in the {profile.identity}. This game is structured around two main parties: the country_F Army and the country_E Army. Each game round lasts {profile.round_interval} minutes, and the game is currently in round {profile.round_nb}. You should select actions from the '## Action Space' that fit your persona and are likely for your situation. To get a better understanding of the current state of affairs, please refer to the '## Current Battlefield Situation' section to learn about the latest developments around you.
""",
)

History_Setting_Poitiers = NamedBlock(
    refname="History_Setting_profile",
    name="Game History Setting",
    content=Collection(
        NamedVariable(
            refname="time_HS",
            name="Time of Event",
            content="14th century"
        ))
)


country_E_Army_Poitiers = NamedBlock(
    refname="country_E_Army_profile",
    name="**country_E Army Profile**",
    content=Collection(
        NamedVariable(
            refname="command_structure_E",
            name="Command Structure",
            content="\n(1) Supreme Commander: Prince of the country \n(2) Subordinate Leaders: Notable figures with significant operational autonomy"
        ),
        NamedVariable(
            refname="morale_discipline_E",
            name="Morale and Discipline",
            content="\n(1) Exceptionally high morale due to previous victories and effective leadership \n(2) Strict discipline and innovative tactics, especially the use of the longbow"
        ),
        NamedVariable(
            refname="military_strategy_E",
            name="Military Strategy",
            content="\n(1) Offensive strategy utilizing terrain advantages \n(2) Skilled use of longbows to weaken enemy before engaging in close combat, underscored by ambitious tactical innovations."
        ),
        NamedVariable(
            refname="military_capability_E",
            name="Key Weaponry",
            content="\n(1) Key Weapon: Longbow, a decisive factor in battle \n(2) Combination of longbowmen and dismounted men-at-arms for a balanced force"
        ),
        NamedVariable(
            refname="force_size_composition_E",
            name="Force Size and Composition",
            content="\nSize Estimate: Around 6,000-7,000 \nComposition: Primarily local longbowmen, complemented by men-at-arms and a small number of mounted knights"
        ),
        NamedVariable(
            refname="armament_protection_E",
            name="Armament and Protection",
            content="\nArmor: Combination of mail and plate armor for men-at-arms. \nShields: Limited use, focusing on mobility and bow usage. \nWeapons: Longbows, swords, and other hand-held weapons for close combat."
        )
    )
)



country_F_Army_Poitiers = NamedBlock(
    refname="country_F_Army_profile",
    name="**country_F Army Profile**",
    content=Collection(
        NamedVariable(
            refname="command_structure_F",
            name="Command Structure",
            content="\n(1) Commanded by King of the country \n(2) Less effective, lacking cohesive leadership"
        ),
        NamedVariable(
            refname="morale_discipline_F",
            name="Morale and Discipline",
            content="\n(1) Morale issues among foreign mercenary crossbowmen \n(2) Lack of discipline among their knights, leading to disorganized charges"
        ),
        NamedVariable(
            refname="military_strategy_F",
            name="Military Strategy",
            content="\n(1) Conduct offensive strategy lacking coordination and adaptability \n(2) Heavy reliance on mounted knights and mercenary crossbowmen, to break enemy lines."
        ),
        NamedVariable(
            refname="military_capability_F",
            name="Key Weaponry",
            content="\n(1) Dependent on armored knights and foreign crossbowmen \n(2) Less effective strategy and equipment against enemy tactics"
        ),
        NamedVariable(
            refname="force_size_composition_F",
            name="Force Size and Composition",
            content="Total Soldiers: Approximately 35,000 soldiers including (1) Heavy Knights: 12,000 (2) Mercenary Crossbowmen: 6,000."
        ),
        NamedVariable(
            refname="armament_protection_F",
            name="Armament and Protection",
            content="Primary Forces: Heavy cavalry and skilled crossbowmen. Cavalry Equipment: Heavy armor and weapons for close combat. Crossbowmen: Equipped for ranged engagement, limitations in adverse weather."
        )
    )
)

