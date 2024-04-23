from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *


System_Setting_Agincourt = NamedVariable(
    refname="general_setting",
    name="Overall Setting",
    content="""
You are now a participant in a virtual strategy game, representing a commander in the {profile.identity}. This game is structured around two main parties: the country_F Army and the country_E Army. Each game round lasts {profile.round_interval} minutes, and the game is currently in round {profile.round_nb}. You should select actions from the '## Action Space' that fit your persona and are likely for your situation. To get a better understanding of the current state of affairs, please refer to the '## Current Battlefield Situation' section to learn about the latest developments around you.
""",
)

History_Setting_Agincourt = NamedBlock(
    refname="History_Setting_profile",
    name="Game History Setting",
    content=Collection(
        NamedVariable(
            refname="time_HS",
            name="Time of Event",
            content="October of 1415"
        )
        )
)


country_E_Army_Agincourt = NamedBlock(
    refname="country_E_Army_profile",
    name="**country_E Army Profile**",
    content=Collection(
        NamedVariable(
            refname="command_structure_E",
            name="Command Structure",
            content="\n(1) Supreme Commander: King of the country \n(2) Subordinate Leaders: Experienced nobles and knights, with limited autonomy under the king's strategic direction"
        ),
        NamedVariable(
            refname="morale_discipline_E",
            name="Morale and Discipline",
            content="\n(1) Exceptionally high morale, bolstered by the leadership of King \n(2) Disciplined troops, well-organized despite being outnumbered"
        ),
        NamedVariable(
            refname="military_strategy_E",
            name="Military Strategy",
            content="\n(1) Offensive strategy, despite being outnumbered \n(2) Innovative use of longbows to disrupt and weaken the enemy before close combat"
        ),
        NamedVariable(
            refname="military_capability_E",
            name="Key Weaponry",
            content="\n(1) Key Weapon: Longbow, a decisive factor in the battle \n(2) Combination of longbowmen and dismounted men-at-arms"
        ),
        NamedVariable(
            refname="force_size_composition_E",
            name="Force Size and Composition",
            content="\nSize Estimate: Approximately 6,000-9,000 soldiers \nComposition: A significant number of longbowmen, and a small group of men-at-arms"
        ),
        NamedVariable(
            refname="armament_protection_E",
            name="Armament and Protection",
            content="\nArmor: Combination of plate and mail armor, with some wearing lighter armor for increased mobility. \nShields: Limited use, emphasis on mobility and bow use. \nWeapons: Primarily the longbow, with swords, axes, and daggers for close combat."
        )
    )
)


country_F_Army_Agincourt = NamedBlock(
    refname="country_F_Army_profile",
    name="**country_F Army Profile**",
    content=Collection(
        NamedVariable(
            refname="command_structure_F",
            name="Command Structure",
            content="\n(1) Commanded by highest-ranked noble in the country, with various high-ranking nobles \n(2) Command structure characterized by a lack of unified command and competing interests among nobility"
        ),
        NamedVariable(
            refname="morale_discipline_F",
            name="Morale and Discipline",
            content="\n(1) Initial high morale due to numerical superiority \n(2) Discipline issues, particularly among nobles leading to impetuous and disorganized charges"
        ),
        NamedVariable(
            refname="military_strategy_F",
            name="Military Strategy",
            content="\n(1) Offensive strategy with heavy reliance on cavalry and armored knights \n(2) Underestimation of the enemy forces and overconfidence in numerical superiority"
        ),
        NamedVariable(
            refname="military_capability_F",
            name="Key Weaponry",
            content="\n(1) Main strength in heavy cavalry and armored knights \n(2) Ineffectiveness against the enemy longbowmen and terrain conditions"
        ),
        NamedVariable(
            refname="force_size_composition_F",
            name="Force Size and Composition",
            content="\nTotal Soldiers: Approximately 20,000-30,000 soldiers. Heavy Knights and Men-at-Arms: Majority of the force. Lesser number of Archers and Crossbowmen."
        ),
        NamedVariable(
            refname="armament_protection_F",
            name="Armament and Protection",
            content="\nPrimary Forces: Predominantly heavy cavalry. Cavalry Equipment: Extensive armor for knights, including plate armor. Infantry: Equipped with various weapons, including swords and polearms."
        )
    )
)

