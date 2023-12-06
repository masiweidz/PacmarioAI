import gym

class CustomRewardWrapper(gym.Wrapper):
    def __init__(self, env):
        """
        自定义奖励包装器的初始化。
        参数:
        env: 需要包装的原始游戏环境。
        """
        super(CustomRewardWrapper, self).__init__(env)

    def step(self, action):
        """
        环境的 step 方法，每次动作执行后调用。
        参数:
        action: 执行的动作。
        返回:
        state: 新的状态。
        reward: 根据自定义规则计算的奖励。
        done: 是否完成。
        info: 额外信息。
        """
        state, reward, done, info = self.env.step(action)
    
        # 自定义奖励逻辑
        # 例如，可以根据 'x_pos' 来增加奖励
        # reward += info.get('x_pos', 0)

        return state, reward, done, info

# 可以添加其他相关函数或类
