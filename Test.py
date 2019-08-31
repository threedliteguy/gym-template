import gym

env = gym.make('gym_echo:echo-v0', mode='asdf')

ob = env.reset()
print('ob=',ob)

action = env.action_space.sample()
print('action=', action)

ob, reward, done, _ = env.step(action)

print('ob =', ob, ' reward=', reward, ' done=', done)

env.close()

