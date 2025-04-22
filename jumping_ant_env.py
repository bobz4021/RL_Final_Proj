import gymnasium as gym
import numpy as np
from gymnasium.envs.registration import register

class JumpingAntEnv(gym.Env):
    def __init__(self, render_mode=None):
        self.env = gym.make("Ant-v4", render_mode=render_mode)
        self.observation_space = self.env.observation_space
        self.action_space = self.env.action_space
        self.render_mode = render_mode

    def reset(self, **kwargs):
        obs, info = self.env.reset(**kwargs)
        return obs, info

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)

        # Reward: encourage forward velocity (x-direction)
        forward_vel = self.env.unwrapped.data.qvel[0]  # x-axis linear velocity
        torso_height = self.env.unwrapped.data.qpos[2]  # z height of torso

        reward = forward_vel * 10.0  # scale forward velocity
        if torso_height < 0.2:
            reward -= 50  # penalize falling
            terminated = True

        return obs, reward, terminated, truncated, info

    def render(self):
        return self.env.render()

    def close(self):
        self.env.close()

# Register the environment
register(
    id="JumpingAnt-v0",
    entry_point="jumping_ant_env:JumpingAntEnv"
)

# Run the environment for visual debug
if __name__ == "__main__":
    env = gym.make("JumpingAnt-v0", render_mode="human")
    obs, _ = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, _ = env.step(action)
        print(f"Reward: {reward:.2f}")
        if terminated or truncated:
            obs, _ = env.reset()

    env.close()
