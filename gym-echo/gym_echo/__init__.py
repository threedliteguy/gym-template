from gym.envs.registration import register

register(id='echo-v0',
         entry_point='gym_echo.envs:EchoEnv',
)
