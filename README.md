# RL_Final_Proj: Vertical Jumping Ant with PPO

This project trains a MuJoCo Ant robot to jump vertically as high as possible using reinforcement learning. We build on Gymnasium's `Ant-v4` environment and define a custom reward function that encourages explosive vertical movement. The policy is trained using Proximal Policy Optimization (PPO) from the Stable-Baselines3 library.

##  Project Preview

The Ant learns to generate vertical lift using torque commands on its 8 joints (4 hips, 4 ankles). No changes are made to the robot's structure or XML.

##  Features

-  Built on MuJoCo 3.3.1  
-  Custom Gym wrapper (`JumpingAnt-v0`)  
-  Dense reward: vertical velocity + height  
-  PPO with parallel training environments  
-  Visualizable with `render_mode="human"`  
-  No camera or vision input needed (pure proprioception)

##  Setup Instructions

### 1. Download MuJoCo 3.3.1

- Download from: https://mujoco.org/
- Extract it to the root of this project folder:

RL_Final_Proj/  
├── mujoco-3.3.1/

### 2. Set Environment Variables

**Windows (PowerShell):**  
$env:MUJOCO_GL = "osmesa"  
$env:MUJOCO_PY_MUJOCO_PATH = "$(Get-Location)\mujoco-3.3.1"

**macOS/Linux (bash):**  
export MUJOCO_GL=egl  
export MUJOCO_PY_MUJOCO_PATH=$(pwd)/mujoco-3.3.1

### 3. Install Dependencies

Create and activate a virtual environment:  
python -m venv rl_env  
# Activate:  
# Windows: rl_env\Scripts\activate  
# macOS/Linux: source rl_env/bin/activate  

Install packages:  
pip install gymnasium[all] stable-baselines3 mujoco

## ▶ How to Run

To run the environment with random actions:  
python main.py

To train PPO (optional):  
python train.py

##  Folder Structure

RL_Final_Proj/  
├── mujoco-3.3.1/               # MuJoCo engine files  
├── jumping_ant_env.py         # Custom Gym wrapper with vertical jump reward  
├── main.py                    # Script to run environment manually  
├── train.py                   # (Optional) PPO training loop  
├── README.md                  # Project documentation

##  Reward Function

The reward function is designed to encourage vertical lift and efficient takeoff:  
- +10 × v_z – torso vertical velocity  
- +10 × z – torso height  
- −50 – penalty if torso height falls below z < 0.2  
- −1 – per-step penalty to discourage stalling

##  Authors

- Qingyang Zeng  
- Huaze Liu  
- Zihao Gao  


##  References

- MuJoCo: Todorov et al., 2012 – https://mujoco.org/  
- Gymnasium: Farama Foundation, 2023 – https://github.com/Farama-Foundation/Gymnasium  
- Stable-Baselines3: Raffin et al., 2021 – https://github.com/DLR-RM/stable-baselines3  
- PPO: Schulman et al., 2017 – https://arxiv.org/abs/1707.06347

