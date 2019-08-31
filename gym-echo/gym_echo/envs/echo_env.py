import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.spaces import Discrete, Tuple

class EchoEnv(gym.Env):
    metadata = {'render.modes': ['human']}


    def __init__(self, mode):
        print('init ', mode)
        self.action_space = Tuple([Discrete(2),Discrete(2)])
        self.observation_space = Tuple([Discrete(2),Discrete(2)])
        self.seed()
        self.reset()

    def reset(self):
        print('reset')
        ob = self.observation_space.sample()
        return ob

    def step(self, action):
        print('step')
        reward = 0.0
        ob = self.observation_space.sample()
        episode_over = False
        return ob, reward, episode_over, {}

    def render(self, mode='human'):
        print('render')

    def close(self):
        print('close')

    def seed(self, seed=None):
        print('seed')
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

