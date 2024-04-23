# Standard library imports
import json5 as json
import pickle
import uuid
from abc import ABC, abstractmethod
from datetime import timedelta
import re


# Local application/library-specific imports
from procoder.functional import format_prompt#, replaced_submodule
from procoder.prompt import *

from prompt import Detachment_Agent_prompt
from prompt.action_space_setting import action_list, action_property_definition
from prompt.Detachment_Agent_prompt import action_instruction_block, json_constraint_variable, json_example_text
from prompt.Detachment_Agent_prompt import *
from prompt.map_setting import map_info_json

# Conflict info
from prompt.agent_profile import country_E_Army, country_F_Army, System_Setting, History_Setting

from utils.LLM_api import run_LLM
from utils.VLM_api import run_gpt4v
from utils.surrounding_visualization import plot_tactical_positions

# 基本代理类
class BasicAgent(ABC):
    def __init__(self, identity, model_type):
        self.identity = identity
        self.model_type = model_type
        self.history = []
        
    @abstractmethod
    def construct_prompt(self):
        pass

    def run_model(self, prompt):    
        return run_LLM(self.model_type, prompt)
            
    @abstractmethod
    def parse_llm_output(self):
        # return json result
        pass

    @abstractmethod
    def validate_parsed_output(self):
        pass

    @abstractmethod
    def parsed_data_sync(self, parse_data):
        pass
    
    @abstractmethod
    def execute(self):
        pass


def BranchStreamlining(agent, target_agent_id):
    print("doing the BranchStreamlining")
    sub_agent_entity = None
    for sub_agent in agent.hierarchy.sub_agents:
        if sub_agent.hierarchy.id == target_agent_id:
            sub_agent_entity = sub_agent
            break
    
    # Handle the case where the target agent is not found
    if sub_agent_entity is None:
        return "BranchStreamlining stop."
    if sub_agent_entity.profile.moral == "Low":
        streamlining_label  = "Prune"
    else:
        streamlining_label = "Merge"
        
    subsub_agents_list = sub_agent_entity.hierarchy.sub_agents
    
    if len(subsub_agents_list)>0:
        for subsub_agent in subsub_agents_list:
            subsub_agent.hierarchy.parent_agent = agent
            agent.hierarchy.sub_agents.append(subsub_agent)
            
            
    if streamlining_label == "Merge":
        # Do Merge
        agent.profile.deployed_num_of_troops -= sub_agent_entity.profile.original_num_of_troops
        agent.profile.lost_num_of_troops += sub_agent_entity.profile.lost_num_of_troops
        
    elif streamlining_label == "Prune":
        # Do Prune
        agent.profile.deployed_num_of_troops -= sub_agent_entity.profile.original_num_of_troops
        agent.profile.lost_num_of_troops += sub_agent_entity.profile.original_num_of_troops
        
    # disable the subagent
    agent.hierarchy.sub_agents.remove(sub_agent_entity)
    sub_agent_entity.mergedOrPruned = True

    return "agent {agent.hierarchy.id} BranchStreamlining Done"



class ConstantPromptConfig:
    def __init__(self, System_Setting, History_Setting, army_setting, role_setting, troop_information, json_constraint_variable, json_example_text, action_list, action_property_definition, action_instruction_block, map_info_json, additional_settings):
        # Overall Setting
        self.System_Setting = System_Setting
        self.History_Setting = History_Setting

        # Army Setting
        self.army_setting = army_setting
        self.role_setting = role_setting
        self.troop_information = troop_information

        # Prompt setting 
        self.json_constraint_variable = json_constraint_variable
        self.action_list = action_list
        self.action_property_definition = action_property_definition
        self.action_instruction_block = action_instruction_block
        self.map_info_json = map_info_json

        # Additional Settings
        self.additional_settings = additional_settings
        


class Detachment_AgentProfile:
    def __init__(self, identity, position, original_num_of_troops, initial_mission = "win the battles",  constant_prompt_config = None):
        ### Army Information
        self.identity = identity
        self.position = position
        self.deployed_num_of_troops = 0
        self.lost_num_of_troops = 0
        self.original_num_of_troops = original_num_of_troops
        
        ### Prompt Part
        self.constant_prompt_config = constant_prompt_config
        
        self.System_Setting = constant_prompt_config.System_Setting
        self.history_setting = constant_prompt_config.History_Setting
        self.army_setting = constant_prompt_config.army_setting
        self.RoleSetting = constant_prompt_config.role_setting
        self.TroopInformation = constant_prompt_config.troop_information
        self.json_constraint_variable = constant_prompt_config.json_constraint_variable
        self.action_list = constant_prompt_config.action_list
        self.action_property_definition = constant_prompt_config.action_property_definition
        self.action_instruction_block = constant_prompt_config.action_instruction_block
        self.map_info_json = constant_prompt_config.map_info_json
        
        ###
        self.initial_mission = initial_mission
        
        ###
        self.max_deploy_percent = 0.6
        self.prompt_max_deploy_percent = self.max_deploy_percent * 100 
        self.prompt_max_deploy_nb = int(self.original_num_of_troops * self.max_deploy_percent)
        
        ### system setting
        self.current_stage = "In Battle"
        self.agent_clock = None 
        self.round_nb = None
        self.round_interval = 15
        self.CurrentBattlefieldSituation = ""
        
        self.history_board = {}
        self.history_board["initial_mission"] = self.initial_mission
        
        self.current_action = initial_mission # 用于记录当前动作
        self.troopType = ""
        
        self.init_position = position
        self.position_hist_dict = {}
        
        # self.streamlining_label = "Merge" #default is merge
        self.moral = "Medium"
        
    def position_updated_hist(self, round_nb,new_position):
        next_round_nb = round_nb + 1
        self.position_hist_dict[round_nb] = new_position   
    
    def get_position_hist(self):
        return self.init_position, self.position_hist_dict    
            
    @property
    def lapse_time(self):
        return self.round_nb * self.round_interval
    
    @property
    def remaining_num_of_troops(self):
        return self.original_num_of_troops - self.deployed_num_of_troops - self.lost_num_of_troops
    

class Detachment_AgentHierarchy:
    def __init__(self, level, parent_agent=None):
        short_uuid = str(uuid.uuid4())[:8]  # 取UUID的前8位
        self.id = f"ARMY-{short_uuid}"  # 添加前缀
        
        self.level = level
        self.parent_agent = parent_agent
        self.sub_agents = []
        
        # self.target_agent_name_list = []
        self.target_agent_id = ""
        
    @property
    def target_agent_list(self):
        pass
    
    
    @property
    def parent_agent_id(self):
        """Returns the ID of the parent agent if it exists, otherwise None."""
        return self.parent_agent.hierarchy.id if self.parent_agent else None

    @property
    def sub_agent_ids(self):
        """Returns a list of IDs of sub-agents."""
        return [agent.hierarchy.id for agent in self.sub_agents]
    
    def add_sub_agent(self, sub_agent):
        self.sub_agents.append(sub_agent)
        sub_agent.parent_agent = self

class Detachment_Agent(BasicAgent):
    def __init__(self, model_type, profile, hierarchy):
        super().__init__(profile.identity, model_type)
        self.model_type = model_type
        self.profile = profile
        self.hierarchy = hierarchy
        self.LLM_response = None

        self.execute_nb = 0
        self.extracted_json_history = {}
        self.LLM_response_history = {}
        self.round_invalid_messages = []
        self.invalid_messages_history = []
        self.additional_prompt = "" # 用于暂时存储额外的信息，日后可以加入profile里面
        
        
        self.action_restrictions_require = False
        self.mergedOrPruned = False
        
        self.log_folder_name = ""

    def __eq__(self, other):
        return isinstance(other, Detachment_Agent) and self.hierarchy.id == other.hierarchy.id
    
    def __hash__(self):
        return hash(self.hierarchy.id)
    
    @property
    def prompt(self):
        return self.construct_prompt()
    
    def generate_action_list(self):
        actions_text = '\n'.join([
            # f"{action}: {properties.get('prompt', 'No description available')}"
            f"{action}"
            for action, properties in self.profile.action_property_definition.items()
        ])
        return actions_text

    
    def validate_parsed_output(self, json_data):
        invalid_messages = []
        
        # Validate root object fields
        if not isinstance(json_data.get("agentNextActionType"), str):
            invalid_messages.append("agentNextActionType must be a String")
        if not isinstance(json_data.get("remarks"), str):
            invalid_messages.append("remarks must be a String")
        if not isinstance(json_data.get("SubAgentsRecall"), list) or not all(isinstance(item, str) for item in json_data.get("SubAgentsRecall", [])):
            invalid_messages.append("SubAgentsRecall must be a list of Strings")
        if json_data.get("agentMoral") not in ["High", "Medium", "Low"]:
            invalid_messages.append("agentMoral must be 'High', 'Medium', or 'Low'")
        if not isinstance(json_data.get("speed"), int):
            invalid_messages.append("speed must be an Integer")
        if not isinstance(json_data.get("agentNextPosition"), list) or len(json_data.get("agentNextPosition", [])) != 2 or not all(isinstance(item, int) for item in json_data.get("agentNextPosition", [])):
            invalid_messages.append("agentNextPosition must be an Array of 2 Integers")
        if not isinstance(json_data.get("deploySubUnit"), bool):
            invalid_messages.append("deploySubUnit must be a Boolean")
        
        # Validate actions array and its objects
        actions = json_data.get("actions", [])
        if not isinstance(actions, list):
            invalid_messages.append("actions must be an Array of Objects")
        else:
            for action in actions:
                if not isinstance(action.get("subAgent_NextActionType"), str):
                    invalid_messages.append("Each action's subAgent_NextActionType must be a String")
                if not isinstance(action.get("troopType"), str):
                    invalid_messages.append("Each action's troopType must be a String")
                if not isinstance(action.get("speed"), int):
                    invalid_messages.append("Each action's speed must be an Integer")
                if not isinstance(action.get("deployedNum"), int):
                    invalid_messages.append("Each action's deployedNum must be an Integer")
                if not isinstance(action.get("ownPotentialLostNum"), int):
                    invalid_messages.append("Each action's ownPotentialLostNum must be an Integer")
                if not isinstance(action.get("enemyPotentialLostNum"), int):
                    invalid_messages.append("Each action's enemyPotentialLostNum must be an Integer")
                if not isinstance(action.get("position"), list) or len(action.get("position", [])) != 2 or not all(isinstance(item, int) for item in action.get("position", [])):
                    invalid_messages.append("Each action's position must be an Array of 2 Integers")
                if not isinstance(action.get("agent_id"), str):
                    invalid_messages.append("Each action's agent_id must be a String")
                if not isinstance(action.get("remarks"), str):
                    invalid_messages.append("Each action's remarks must be a String")
                    
        return invalid_messages

    
    def construct_prompt(self):
        actions_text = self.generate_action_list()

        battle_prompt = format_prompt(
        Sequential(
            self.profile.System_Setting, 
            self.profile.history_setting,
            # army profile
            self.profile.army_setting,
            self.profile.RoleSetting,
            self.profile.TroopInformation,
            
            # self.profile.action_list,
            self.profile.action_instruction_block,
            self.profile.json_constraint_variable,
            
            # current situation
            
        ).set_sep("\n\n").set_indexing_method(sharp2_indexing), {"profile":self.profile,"hierarchy" : self.hierarchy})
        
        battle_prompt += "\n\n" + "## initial mission\n" + "initial mission refers to the first task or objective assigned to the country_E Commander at the start of the game.\n" + self.profile.initial_mission
        battle_prompt += "\n\n" + f"## battle field infomation\n This JSON data describes a map of Battle field.  It includes geographic features, military movements, and other relevant details.\n {self.profile.map_info_json}. The map's dimensions range from -1000 to +1000. Going beyond this range (leaving the map's boundaries) is considered a defeat of this agent."  

        battle_prompt += "\n\n" + "## Action Space\n" + "In this simulation, you can use the following actions.\n" + actions_text
        # battle_prompt +=  "\n\n" + self.profile.json_example_text
        
        ## assemble the invalid messages
        flat_invalid_messages = [message for sublist in self.round_invalid_messages for message in sublist]
        invalid_messages_str = "\n".join(flat_invalid_messages)
        battle_prompt += "\n\n" + invalid_messages_str
        
        battle_prompt += "\n\n" + "## History Action Plan\n" + f"This is all of your analysis and planning from previous rounds. It will assist you in determining the stage of the war, helping you make significant decisions.\n {self.LLM_response_history}" 
        
        
        battle_prompt += "\n\n" + "## Current Battlefield Situation\n" + f"This is what's happening around you. You can discern the number of enemies and allies, as well as their current actions, within a certain range.\n {self.profile.CurrentBattlefieldSituation}" 
        
        battle_prompt += "\n\n" + "War is on the verge of breaking out. To initiate an attack on the enemy, based on the speed you've estimated, you and your deployed sub-agents will advance towards the enemy, navigating by the coordinates."
        
        if self.action_restrictions_require:
            battle_prompt += "\n\n" + "## Restriction on Sub-Agent Deployment\n" + "Limitation: Due to previous extensive deployment of sub-agents, your current strategy must be confined to your main force, requiring the 'actions' array in the output JSON to include only one action specifically for your command. This constraint prohibits dispatching subsidiary agents and ensures a singular, focused action directive."
        
        battle_prompt += "\n\n" + self.additional_prompt

        print("--------------")
        return battle_prompt

    

    def parse_llm_output(self, LLM_response):
        def extract_json_from_text(text):
            """
            Extracts the JSON part from a given string which may contain mixed content.
            It assumes that the JSON part starts with '{' and ends with '}'.
            """
            try:
                # Finding the indices of the first '{' and the last '}'
                start_index = text.index('{')
                end_index = text.rindex('}') + 1

                # Extracting the JSON substring
                json_part = text[start_index:end_index]

                # Attempting to parse the JSON part
                parsed_json = json.loads(json_part)
                return parsed_json
            except ValueError as e:
                # Error handling if JSON parsing fails
                return f"Error extracting JSON: {e}"

        extracted_json = extract_json_from_text(LLM_response)
        
        if not isinstance(extracted_json, dict):
            print(LLM_response)
        else:
            pass
        

        return extracted_json

    def parsed_data_sync(self, parsed_json):
        sync_results = []
        if parsed_json["agentMoral"]:
            self.profile.moral = parsed_json["agentMoral"]
        
        if parsed_json["SubAgentsRecall"]:
            for recalled_agent_id in parsed_json["SubAgentsRecall"]:
                bS_message = BranchStreamlining(self, recalled_agent_id)
                print("do the BranchStreamlining")
                
        if self.profile.position != parsed_json["agentNextPosition"]:
            print(f"Moved from {self.profile.position} to {parsed_json['agentNextPosition']}")
        else:
            print("postion no change")    
        
        if len(parsed_json['agentNextPosition']) == 2 and all(isinstance(item, int) for item in parsed_json['agentNextPosition']):
            self.profile.position = parsed_json["agentNextPosition"]
            self.profile.position_updated_hist(self.profile.round_nb, parsed_json["agentNextPosition"])
        # self.profile.position_hist_dict.append(parsed_json["currentAgentPosition"])

        self.profile.current_action = parsed_json["agentNextActionType"] + " " + parsed_json["remarks"]
        self.target_agent_id = parsed_json["targetedAgentId"]
        # Process each action in the actions list
        for action in parsed_json["actions"]:
            if len(action['position']) == 2 and all(isinstance(item, int) for item in action['position']):
                new_sub_agent = self.create_sub_agent(action)
                
                
                new_sub_agent.hierarchy.target_agent_id = action["agent_id"]
                new_sub_agent.profile.troopType = action["troopType"]
                
                sync_results.append({"action": action["subAgent_NextActionType"], "result": "sub_agent_created", "sub_agent": new_sub_agent})
                if "deployedNum" in action and action['deployedNum'] not in ["All available", "All remaining"]:
                    self.profile.deployed_num_of_troops += int(action['deployedNum'])

        # Check for other conditions like Crushing Defeat or fleeing Off the Map
        if self.profile.remaining_num_of_troops < self.profile.original_num_of_troops * 0.1 or self.profile.lost_num_of_troops > self.profile.original_num_of_troops * 0.5:
            self.profile.current_stage = "Crushing Defeat"

        if self.profile.position[0] > 1000 or self.profile.position[1] > 1000:
            self.profile.current_stage = "fleeing Off the Map"

        # Return the results of the synchronization
        return sync_results
    
    ### Misc method
    def create_sub_agent(self, action):
        # Create a new profile based on the current agent's profile
        new_profile = Detachment_AgentProfile(
            identity=self.profile.identity,  
            position=action['position'], 
            original_num_of_troops=int(action['deployedNum']) if action['deployedNum'] != "All available" else self.profile.remaining_num_of_troops,  # 根据动作设置部队数量
            initial_mission=action["subAgent_NextActionType"], 
            constant_prompt_config=self.profile.constant_prompt_config  
        )
        
        # Create a new hierarchy level for the subunit
        new_hierarchy = Detachment_AgentHierarchy(
            level=self.hierarchy.level + 1,  # Set the hierarchy level one step deeper
            parent_agent=self  # Set the current hierarchy as the parent
        )

        # Initialize the new sub-agent
        new_sub_agent = Detachment_Agent(self.model_type, new_profile, new_hierarchy)
        new_sub_agent.new_born = True
        new_sub_agent.log_folder_name = self.log_folder_name

        # Add the new sub-agent to the current hierarchy
        self.hierarchy.add_sub_agent(new_sub_agent)
        

        return new_sub_agent

    
    def DEVELOPING_MODE_save_sync_results_with_pickle(self, sync_results, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(sync_results, file)
        
        
    def calculate_troop_deployments(self, actions):
        new_troops_deployed = 0
        for action in actions:
            # Extract the number of troops from each action and add to the total
            number_of_troops_in_this_action = action.get('number', -1)
            if number_of_troops_in_this_action == -1:
                raise ValueError("number of troop don't decide")
            
            if number_of_troops_in_this_action not in ["All available","All"]:
                new_troops_deployed += int(number_of_troops_in_this_action)
        return new_troops_deployed

    def get_logged_attributions(self):
        # Fetching attributes from the profile
        identity = self.profile.identity
        position = self.profile.position
        deployed_troops = self.profile.deployed_num_of_troops
        original_troops = self.profile.original_num_of_troops
        remaining_troops = self.profile.remaining_num_of_troops
        lost_num_of_troops = self.profile.lost_num_of_troops
        current_battlefield_situation = self.profile.CurrentBattlefieldSituation
        current_stage = self.profile.current_stage
        agent_clock = self.profile.agent_clock

        # Fetching attributes from the hierarchy
        agent_level = self.hierarchy.level
        
        parent_agent = self.hierarchy.parent_agent.hierarchy.id if self.hierarchy.parent_agent else None
        sub_agents = [agent.hierarchy.id for agent in self.hierarchy.sub_agents] if self.hierarchy.sub_agents else []


        # Organizing the fetched information into a dictionary
        attributes = {
            "identity": identity,
            "position": position,
            "troop_info": {
                "deployed": deployed_troops,
                "original": original_troops,
                "lost": lost_num_of_troops,
                "remaining": remaining_troops
            },
            "battlefield_situation": current_battlefield_situation,
            "hierarchy_info": {
                "level": agent_level,
                "parent_agent": parent_agent,
                "sub_agents": sub_agents
            },
            "system_setting": {
                "current_stage": current_stage,
                "agent_clock": agent_clock
            }
        }
        
        text_msg = f"This level {attributes['hierarchy_info']['level']} {attributes['identity']} unit is {attributes['system_setting']['current_stage']}. It is at {attributes['position']}. It initially has {attributes['troop_info']['original']} soldiers, out of which {attributes['troop_info']['deployed']} were deployed. {attributes['troop_info']['lost']} troops have been lost, and {attributes['troop_info']['remaining']} are still remaining.'"

        return attributes, text_msg

    
    def execute(self, LLM_response=None):
        max_attempts = 3
        attempts = 0

        # 更新执行次数
        self.hierarchy.target_agent_id = ""
        
        self.execute_nb += 1

        if LLM_response in [None, ""]:
            LLM_response = self.run_model(self.prompt)
            

        # 记录LLM响应历史
        self.LLM_response_history[self.execute_nb] = LLM_response
        
        while attempts < max_attempts:
            extracted_json = self.parse_llm_output(LLM_response)
            print(f"[Execute #{self.execute_nb}] Attempt #{attempts + 1}: Extracted JSON: {extracted_json}")
            ## Do json validation
            invalid_messages = self.validate_parsed_output(extracted_json)
            
            print("--------------")

            # extra json history 
            self.extracted_json_history[self.execute_nb] = extracted_json
            
            if invalid_messages != []:
                print(f"[Execute #{self.execute_nb}] Attempt #{attempts + 1}: Invalid messages detected: {invalid_messages}")
                if attempts == max_attempts:
                    raise Exception("Invalid messages after maximum attempts.")
                else:
                    LLM_response = self.run_model(self.prompt)
                    self.round_invalid_messages.append(invalid_messages)
                    attempts += 1
            else:
                # Synchronize data based on parsed JSON
                self.invalid_messages_history.append(self.round_invalid_messages)
                self.round_invalid_messages = []
                
                sync_results = self.parsed_data_sync(extracted_json)
                
                return {
                    "success": True,
                    "sync_results": sync_results,
                    "attempts": attempts,
                    "invalid_messages": invalid_messages
                }
        return

    def execute_WithGpt4V(self):
        print(self.log_folder_name)

        max_attempts = 5
        attempts = 0

        # 更新执行次数
        self.hierarchy.target_agent_id = ""
        
        self.execute_nb += 1
        plot_tactical_positions(self.profile.CurrentBattlefieldSituation, img_save_path = f"{self.log_folder_name}", img_name = f"{self.profile.identity}_{self.hierarchy.id}_{self.execute_nb}")

        image_path = f"{self.log_folder_name}/{self.profile.identity}_{self.hierarchy.id}_{self.execute_nb}.png"
        LLM_response = run_gpt4v(image_path, self.prompt)

        self.LLM_response_history[self.execute_nb] = LLM_response
        
        while attempts < max_attempts:
            extracted_json = self.parse_llm_output(LLM_response)
            print(f"[Execute #{self.execute_nb}] Attempt #{attempts + 1}: Extracted JSON: {extracted_json}")
            print("--------------")

            self.extracted_json_history[self.execute_nb] = extracted_json

            if "Error" in extracted_json:
                invalid_messages = True
            else:
                invalid_messages = False 
            
            if invalid_messages:
                print(f"[Execute #{self.execute_nb}] Attempt #{attempts + 1}: Invalid messages detected: {invalid_messages}")
                if attempts == max_attempts:
                    raise Exception("Invalid messages after maximum attempts.")
                else:
                    LLM_response = run_gpt4v(r"logs\tactical_positions_plot.png", self.prompt)
                    attempts += 1
            else:
                # Synchronize data based on parsed JSON
                sync_results = self.parsed_data_sync(extracted_json)
                
                return {
                    "success": True,
                    "sync_results": sync_results,
                    "attempts": attempts,
                    "invalid_messages": invalid_messages
                }
        return

# tree visiualization
def build_tree(tree, hierarchy_node, parent_id=None):
    tree.create_node(tag=hierarchy_node.id, identifier=hierarchy_node.id, parent=parent_id)
    for sub_agent in hierarchy_node.sub_agents:
        build_tree(tree, sub_agent, parent_id=hierarchy_node.id)
