import gymnasium as gym
from gymnasium.envs.registration import register
import jumping_ant_env  # This imports the custom environment class

# Register the environment (you can skip this if already registered elsewhere)
register(
    id="JumpingAnt-v0",
    entry_point="jumping_ant_env:JumpingAntEnv",
)

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

