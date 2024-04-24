import argparse
import os

from prompt.map_setting_of_other_battles import *
from prompt.agent_profile import country_E_Army, country_F_Army, System_Setting, History_Setting
from prompt.agent_profile_Poitiers import country_E_Army_Poitiers, country_F_Army_Poitiers, System_Setting_Poitiers, History_Setting_Poitiers
from prompt.agent_profile_Falkirk import country_E_Army_Falkirk, country_F_Army_Falkirk, System_Setting_Falkirk, History_Setting_Falkirk
from prompt.agent_profile_Agincourt import country_E_Army_Agincourt, country_F_Army_Agincourt, System_Setting_Agincourt, History_Setting_Agincourt

from agent import *
from sandbox import Sandbox

class ConflictConfig():
    def __init__(self, battle_name):
        self.battle_name = battle_name

    def get_opposing_agent_profile(self):
        # Battle configuration
        if self.battle_name == "Poitiers":
            country_E_agent_profile = Detachment_AgentProfile(
                identity="country_E",
                position=[15, -10],  
                original_num_of_troops=6000,  
                constant_prompt_config = country_E_constant_prompt_config
            )

            country_F_agent_profile = Detachment_AgentProfile(
            identity="country_F", 
                position=[-10, 5],  
                original_num_of_troops=15000,  
                constant_prompt_config = country_F_constant_prompt_config 
            )
        elif self.battle_name == "Falkirk":
            country_E_agent_profile = Detachment_AgentProfile(
                identity="country_E",
                position=[0, 0],  
                original_num_of_troops=15000,  
                constant_prompt_config = country_E_constant_prompt_config
            )

            country_F_agent_profile = Detachment_AgentProfile(
            identity="country_F", 
                position=[50, 0],  
                original_num_of_troops=6000,  
                constant_prompt_config = country_F_constant_prompt_config 
            )
            
        elif self.battle_name == "Agincourt":
            country_E_agent_profile = Detachment_AgentProfile(
                identity="country_E",
                position= [0,-100],  
                original_num_of_troops=6500,  
                constant_prompt_config = country_E_constant_prompt_config
            )

            country_F_agent_profile = Detachment_AgentProfile(
                identity="country_F", 
                position=[15, -50], 
                original_num_of_troops=35000, 
                constant_prompt_config = country_F_constant_prompt_config 
            )
        else:
            return "Invalid conflict name. Please choose from 'Poitiers', 'Falkirk', or 'Agincourt'."

        return country_E_agent_profile, country_F_agent_profile

    def get_prompt_config_args(self):
        if self.battle_name == "Poitiers":
            map_info_json_Type = map_info_json_Poitiers
            System_Setting_Type = System_Setting_Poitiers
            History_Setting_Type = History_Setting_Poitiers
            country_E_Army_Type = country_E_Army_Poitiers
            country_F_Army_Type = country_F_Army_Poitiers
        elif self.battle_name == "Falkirk":
            map_info_json_Type = map_info_json_Falkirk
            System_Setting_Type = System_Setting_Falkirk
            History_Setting_Type = History_Setting_Falkirk
            country_E_Army_Type = country_E_Army_Falkirk
            country_F_Army_Type = country_F_Army_Falkirk
        elif self.battle_name == "Agincourt":
            map_info_json_Type = map_info_json_Agincourt
            System_Setting_Type = System_Setting_Agincourt
            History_Setting_Type = History_Setting_Agincourt
            country_E_Army_Type = country_E_Army_Agincourt
            country_F_Army_Type = country_F_Army_Agincourt
        else:
            return "Invalid conflict name. Please choose from 'Poitiers', 'Falkirk', or 'Agincourt'."
        return System_Setting_Type, History_Setting_Type, country_E_Army_Type, country_F_Army_Type, map_info_json_Type


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Run a conflict simulation.') 
    parser.add_argument('--conflict_name', type=str, choices=['Poitiers', 'Falkirk', 'Agincourt'], default= "Poitiers",help='choose conflict name') 
    parser.add_argument('--LLM_MODEL', type=str, choices = ["claude","gpt"], default= "gpt", help='Language model to use') 
    parser.add_argument("--is_GPT4V_activate", type=int, default= 0, help="Use GPT-4 V instead of GPT-4")
    parser.add_argument('--simulation_time', type=int, default=90, help='Number of minutes to simulate')
    parser.add_argument('--update_interval', type=int, default=15, help='Interval for simulation updates')
    
    parser.add_argument('--have_diaries', type=int, default= 0, help='Whether to have diaries') #"False"
    parser.add_argument('--continue_run', type=int, default= 1, help='Whether to continue run') #"True"

    args = parser.parse_args()
    
    LLM_MODEL = args.LLM_MODEL
    simulation_time = args.simulation_time
    update_interval = args.update_interval
    conflict_name = args.conflict_name
    GPT4V = bool(args.is_GPT4V_activate)
    Is_have_diaries = bool(args.have_diaries)
    Does_continue_run = bool(args.continue_run)

    if LLM_MODEL != "gpt" and GPT4V == True:
        raise ValueError("GPT-4 V is only available for GPT model.")
    
    if LLM_MODEL == "gpt" and GPT4V == True:
        model_name_to_log = "gpt4V"
    else:
        model_name_to_log = LLM_MODEL
    
    LOG_FOLER_NMAE = f"{conflict_name}_{model_name_to_log}_{simulation_time}_{update_interval}"
    print(f"LOG_FOLER_NMAE: {LOG_FOLER_NMAE}")

    conflict_config = ConflictConfig(conflict_name)
    System_Setting_Type, History_Setting_Type, country_E_Army_Type, country_F_Army_Type,map_info_json_Type = conflict_config.get_prompt_config_args()
    
    country_E_constant_prompt_config = ConstantPromptConfig(
        System_Setting=System_Setting_Type,
        History_Setting=History_Setting_Type,
        
        army_setting=country_E_Army_Type,
        
        role_setting=RoleSetting,
        troop_information=TroopInformation,
        json_constraint_variable=json_constraint_variable,
        json_example_text=json_example_text,
        action_list=action_list,
        action_property_definition=action_property_definition,
        action_instruction_block=action_instruction_block,
        map_info_json=map_info_json_Type,
        additional_settings={} 
    )

    country_F_constant_prompt_config = ConstantPromptConfig(
        System_Setting=System_Setting_Type,
        History_Setting=History_Setting_Type,
        
        army_setting=country_F_Army_Type,
        
        role_setting=RoleSetting,
        troop_information=TroopInformation,
        json_constraint_variable=json_constraint_variable,
        json_example_text=json_example_text,
        action_list=action_list,
        action_property_definition=action_property_definition,
        action_instruction_block=action_instruction_block,
        map_info_json=map_info_json_Type,
        additional_settings={}  
    )
    
    country_E_agent_profile, country_F_agent_profile = conflict_config.get_opposing_agent_profile()

    country_E_agent_hierarchy = Detachment_AgentHierarchy(level = 1, parent_agent= None)
    country_F_agent_hierarchy = Detachment_AgentHierarchy(level = 1, parent_agent= None)
    
    country_E_agent_root = Detachment_Agent(LLM_MODEL, country_E_agent_profile, country_E_agent_hierarchy)
    country_F_agent_root = Detachment_Agent(LLM_MODEL, country_F_agent_profile, country_F_agent_hierarchy)
    
    country_E_agent_hierarchy.parent_agent = country_E_agent_root
    country_F_agent_hierarchy.parent_agent = country_F_agent_root
    
    # conflict name and time only used for logging
    sandbox = Sandbox(LLM_MODEL, map_info_json_Type, LOG_FOLER_NMAE, "1300-01-01 12:00", country_E_agent_root, country_F_agent_root)

    sandbox.have_diaries = Is_have_diaries
    sandbox.continue_run = Does_continue_run 
    sandbox.GPT4V = GPT4V 
    sandbox.LLM_MODEL = LLM_MODEL 
    
    simulation_results = sandbox.simulate(simulation_time, update_interval)