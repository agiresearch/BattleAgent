# BattleAgent: Multi-modal Dynamic Emulation on Historical Battles to Complement Historical Analysis

<img width="628" alt="Screen Shot 2024-04-23 at 9 39 28 AM" src="https://github.com/agiresearch/BattleAgent/assets/28013619/cd84e205-469b-465a-8c77-021a55a64498">


## Abstract
This paper presents \textbf{BattleAgent}, a detailed emulation demonstration system that combines the Large Vision-Language Model (VLM) and Multi-agent System (MAS). This novel system aims to simulate complex dynamic interactions among multiple agents, as well as between agents and their environments, over a period of time. It emulates both the decision-making processes of leaders and the viewpoints of ordinary participants, such as soldiers. The emulation showcases the current capabilities of agents, featuring fine-grained multi-modal interactions between agents and landscapes. It develops customizable agent structures to meet specific situational requirements, for example, a variety of battle-related activities like scouting and trench digging. These components collaborate to recreate historical events in a lively and comprehensive manner while offering insights into the thoughts and feelings of individuals from diverse viewpoints. The technological foundations of BattleAgent establish detailed and immersive settings for historical battles, enabling individual agents to partake in, observe, and dynamically respond to evolving battle scenarios. This methodology holds the potential to substantially deepen our understanding of historical events, particularly through individual accounts. Such initiatives can also aid historical research, as conventional historical narratives often lack documentation and prioritize the perspectives of decision-makers, thereby overlooking the experiences of ordinary individuals. This biased documentation results in a considerable gap in our historical understanding, as many stories remain untold. BattleAgent leverages the current advancements in Artificial Intelligence (AI) to provide some insights to bridge this gap. It illustrates AI's potential to revitalize the human aspect in crucial social events, thereby fostering a more nuanced collective understanding and driving the progressive development of human society. Quantitative evaluations are computed on the final emulation result, showing reasonable performance and effectiveness of the approach.


## QuickStart

### Install environment
```
conda create --name battleagent python=3.9
conda activate battleagent

git clone https://github.com/dhh1995/PromptCoder
cd PromptCoder
pip install -e .
cd ..

git clone https://github.com/agiresearch/BattleAgent.git
cd BatleAgent
pip install -r requirements.txt
```

### Set up API keys


### Run BattleAgent Sandbox

