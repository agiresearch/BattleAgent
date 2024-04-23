#!/bin/bash

# Define the configurations in arrays
conflict_names=("Agincourt" "Falkirk" "Poitiers")
ENV_NAME="rag_vrf"
CONDA_PATH="/common/home/sl2148/anaconda3/envs"
PYTHON_SCRIPT_PATH="/common/users/sl2148/BA/BattleAgent_4_3/src/simulation_controller.py"

# Run the simulation for each conflict 5 times
for conflict in "${conflict_names[@]}"; do
    echo "Starting simulations for $conflict"
    for ((i=1; i<=5; i++)); do
        "${CONDA_PATH}/${ENV_NAME}/bin/python" "$PYTHON_SCRIPT_PATH" \
                    --conflict_name $conflict \
                    --LLM_MODEL "claude" \
                    --is_GPT4V_activate 0 \
                    --simulation_time 90 \
                    --update_interval 15 &
        sleep 5 # Pause for 5 seconds before starting the next simulation
    done
    wait # Wait for all the simulations in this batch to complete before starting another
    echo "Completed simulations for $conflict"
done

