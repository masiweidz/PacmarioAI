import gym
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from custom_reward_wrapper import CustomRewardWrapper

def setup_mario_env():
    env = gym_super_mario_bros.make('SuperMarioBros-v3')
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    env = CustomRewardWrapper(env)
    return env