# BattleAgent Demo

## Requirements:  
- Unity 2022.3.29f1
- Visual Studio 2022 (must be installed with Unity enabled)


## To Start: 
- Open `BA_UnitySimulation` folder in Unity
- At the `Project` tab in the Unity Editor, double click the scene at `Assets/Scenes/BattleSimulation.unity`
- Switch to `Game` View and add a new display resolution with 1140 x 776
- Click `Run` to see the animated events

## More Info:
- The manager script (`Assets/Scripts/SimulationManager.cs`) attached to the `SimulationManager` gameobject coordinates all the agents, gameobjects, and animations for the whole scene. 
- Check out the function `ManageBattleSequence()` in the manger script, where all actions should be animated sequentially.

## Supported Actions:
- MoveTo(Agent, Location)
- Explosion
- KnightAttack
- Death
- Idle
- SpearAttack
- SwordAttack
- CalvaryAttack
- ShieldDefense
- ArcheryAttack

## Transformation of Map Coordinates:  
```
X_unity = X / 50 - 5
Y_unity = - Y / 50
```



