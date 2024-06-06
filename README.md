# BattleAgent: Multi-modal Dynamic Emulation on Historical Battles to Complement Historical Analysis

<a href='https://arxiv.org/abs/2404.15532'><img src='https://img.shields.io/badge/Paper-PDF-red'></a> 
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/agiresearch/BattleAgent/blob/main/LICENSE)



<img align="center" alt="main" src="https://github.com/agiresearch/BattleAgent/assets/28013619/cd84e205-469b-465a-8c77-021a55a64498">

## Update!

[June 5th, 2024]🔥 We made the first demo based on LLM's generation for Battle of Crecy!

[April 23rd, 2024]🔥 We release BattleAgent paper! The first paper on LLM-based historical game engine!


## Abstract
This paper presents **BattleAgent**, a detailed emulation demonstration system that combines the Large Vision-Language Model and Multi-agent System. This novel system aims to simulate complex dynamic interactions among multiple agents, as well as between agents and their environments, over a period of time. It emulates both the decision-making processes of leaders and the viewpoints of ordinary participants, such as soldiers. The emulation showcases the current capabilities of agents, featuring fine-grained multi-modal interactions between agents and landscapes. It develops customizable agent structures to meet specific situational requirements, for example, a variety of battle-related activities like scouting and trench digging. These components collaborate to recreate historical events in a lively and comprehensive manner while offering insights into the thoughts and feelings of individuals from diverse viewpoints. The technological foundations of BattleAgent establish detailed and immersive settings for historical battles, enabling individual agents to partake in, observe, and dynamically respond to evolving battle scenarios. This methodology holds the potential to substantially deepen our understanding of historical events, particularly through individual accounts. Such initiatives can also aid historical research, as conventional historical narratives often lack documentation and prioritize the perspectives of decision-makers, thereby overlooking the experiences of ordinary individuals. This biased documentation results in a considerable gap in our historical understanding, as many stories remain untold. 

## Short Video Demo on Battle of Crecy Based on LLM generation

(A clearer version can be found [here](https://drive.google.com/file/d/1lFGz0ujeHHRz4FsqX8TmIjdZODupVwwp/view?usp=sharing))

https://github.com/agiresearch/BattleAgent/assets/28013619/33627864-3924-4660-b58b-70fd353f0c70


--------------------

## QuickStart
### Install environment
```
conda create --name battleagent python=3.9
conda activate battleagent

git clone https://github.com/agiresearch/BattleAgent.git
cd BattleAgent
pip install -r requirements.txt
```

### Set up API keys
If you want to use OpenAI model as base LLM:
```
export OPENAI_API_KEY=your_openai_api_key
```

If you want to use Claude model as base:
```
export CLAUDE_API_KEY=your_claude_api_key
```
### Run BattleAgent Sandbox
#### Basic Usage

To run the sandbox emulation, use the following command:

```
cd src
python simulation_controller.py
```

#### Advanced Options

The script includes several command-line options to customize the simulation:

```
cd src
python simulation_controller.py --conflict_name Poitiers --LLM_MODEL gpt --is_GPT4V_activate 0 --simulation_time 90 --update_interval 15
```

- `--conflict_name`: Choose the historical conflict to simulate. Options are 'Poitiers', 'Falkirk', 'Agincourt'.
- `--LLM_MODEL`: Specify the language model to use. Options include 'claude' and 'gpt'.
- `--is_GPT4V_activate`: If you want to use GPT-4 V instead of standard GPT-4. Set to 1 to activate.
- `--simulation_time`: Number of minutes the simulation will run.
- `--update_interval`: Minutes between simulation updates.

--------------------

## License
The source code of BattleAgent is licensed under [Apache 2.0](https://github.com/casmlab/NPHardEval/blob/main/LICENSE). The intended purpose is solely for research use.


