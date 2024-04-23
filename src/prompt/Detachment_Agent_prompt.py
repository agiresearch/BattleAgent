from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *


RoleSetting = NamedVariable(
    refname="RoleSetting",
    name="role_setting",
    content="""You are a {profile.identity} Commander of at Level {hierarchy.level} in the command structure on the battlefield, positioned at {profile.position} now. Your initial mission is {profile.initial_mission}. You are responsible to {hierarchy.parent_agent_id} (parent node). Your subordinates include {hierarchy.sub_agent_ids} (sub nodes).""",
)

TroopInformation = NamedVariable(
    refname="TroopInformation",
    name="troop_information",
    content="""Your unit initially had {profile.original_num_of_troops} personnel, now this unit have {profile.remaining_num_of_troops}. {profile.lost_num_of_troops} members have been casualties. {profile.deployed_num_of_troops} members have been deployed externally.
Restrictions: (1) The total number of soldiers deployed externally should not exceed {profile.prompt_max_deploy_nb}; (2) You should not deploy a sub-unit of less than 100 soldiers. You must adhere to these two restrictions when you provide the decision in JSON format."""
)


decision_thought_variable = NamedVariable(
    refname="decision_thought",
    name="Thought for Action",
    content="Develop your thoughts step-by-step."
)

action_name_variable = NamedVariable(
    refname="action_name",
    name="The Actions to Perform",
    content="Choose action among '## Action Space'."
)

final_action_variable = NamedVariable(
    refname="final_action",
    name="Present Final Action List in JSON format",
    content="Format your final action list in JSON. and follow json template in the ##json constraint."
)

# 构建提示块
action_instruction_block = NamedBlock(
    refname="Action_Choosing_Instruction",
    name="Action Choosing Instructions",
    content=Block(
        # "Assess the prevailing conditions and strategically select actions that optimize the balance between efficacy and security",
        "",
        Sequential(
            Collection(
                decision_thought_variable,
                action_name_variable,
                # action_input_variable,
                # failed_attempt_variable,
                final_action_variable,
            ).set_sep("\n"),
        )
    ).set_sep("\n\n"),
)


json_constraint_variable = NamedVariable(
    refname="json_constraint",
    name="json constraint",
    content= """
The JSON needs to reflect the following elements:

The JSON structure can be formalized as follows, You need to strictly adhere to the given JSON format:

- **Root Object**:
  - **agentNextActionType**: String
  - **targetedAgentId**: String
  - **remarks**: String
  - **SubAgentsRecall**: list(String)
  - **agentMoral**: string (can be "High", "Medium", "Low")
  - **speed**: Integer
  - **agentNextPosition**: Array of 2 Integers 
  - **deploySubUnit**: Boolean
  - **actions**: Array of Objects (actions for new deployed sub-units)
    - Each Object contains:
      - **subAgent_NextActionType**: String
      - **troopType**: String
      - **speed**: Integer (the unit is in coordinate units per minute. (This indicates how many units of the coordinate system the entity moves per minute.))
      - **deployedNum**: Integer
      - **ownPotentialLostNum**: Integer
      - **enemyPotentialLostNum**: Integer
      - **position**: Array of 2 Integers (This likely represents the X and Y coordinates in a 2D space, determining the entity's location on a grid or map.)
      - **agent_id**: String (can be "None") 
      - **remarks**: String (description of the action in detail)
      
      ### Definition of JSON Keys:
      1.agentNextPosition: Given the `speed`, ## Current Battlefield Situation and ## History Action Plan, what position do you think you should and can move to next before next game round?
      2.position: This is the agent's location at the beginning of the next round. Factors like the battlefield dynamics and the movement speed of your chosen troop type should be considered.
      3.agent_id, targetedAgentId: Those identifiy potential enemies you may encounter in the near future. You need to choose a suitable 'agent_id' from the ## Current Battlefield Situation - 'enemy' - 'agent_id'.
      4.ownPotentialLostNum: This is the estimated number of casualties that the agent will suffer if the action is executed. You should consider the current sitatuation and give the reasonable estimation.
      5.enemyPotentialLostNum: This is the estimated number of casualties that the enemy will suffer if the action is executed.
      6.deployedNum: An estimate of the deployment number should be given. It only can be an integer, not any string like 'All'.
      7.deploySubUnit: This indicates who executes an action: `true` means it's carried out by a subordinate platoon, while `false` means the commander's main force executes it. 
      8.speed:The speed parameter is measured in coordinate units per minute. One coordinate unit is equivalent to 10 yards in the simulated environment.
      9.SubAgentsRecall: If you consider the situation urgent, you may attempt to recall a sub-agent. However, you should not recall an agent unless absolutely necessary.
      
Estimating Losses
Estimate potential losses (ownPotentialLostNum and enemyPotentialLostNum) based on the action type, troop strength, and historical data or simulations provided within the game. These estimates should be as accurate as possible to reflect the expected outcomes of your actions.

""")

json_example_text = ""

if __name__ == '__main__':
    prompt_variables = {}  
    print(json_example_text)
