#!/bin/bash

# Define the configurations in arrays
conflict_names=("Falkirk" "Falkirk" "Falkirk")
LLM_MODELS=("gpt" "gpt" "claude")
is_GPT4V_activates=(0 1 0) #"False" "True" "False"
simulation_times=(90 150 90)
update_intervals=(15 15 15)

ENV_NAME="rag_vrf"
CONDA_PATH="/common/home/sl2148/anaconda3/envs"

PYTHON_SCRIPT_PATH="/common/users/sl2148/BA/BattleAgent_4_3/src/simulation_controller.py"


for j in {0..2}; do
  for i in {1..5}; do
    "${CONDA_PATH}/${ENV_NAME}/bin/python" "$PYTHON_SCRIPT_PATH" \
                    --conflict_name ${conflict_names[$j]} \
                    --LLM_MODEL ${LLM_MODELS[$j]} \
                    --is_GPT4V_activate ${is_GPT4V_activates[$j]} \
                    --simulation_time ${simulation_times[$j]} \
                    --update_interval ${update_intervals[$j]} &
    sleep 5 # Wait for 5 seconds before starting the next iteration
  done
done
wait # Wait here for all background jobs to finish