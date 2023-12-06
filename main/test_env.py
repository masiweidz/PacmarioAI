from env_setup import setup_mario_env


def test_env():
    env = setup_mario_env()
    env.reset()

    done = False
    while not done:
        env.render()  # 实时渲染环境
        action = env.action_space.sample()  # 随机选择一个动作
        _, _, done, _ = env.step(action)  # 执行动作并获取结果

    env.close()

if __name__ == "__main__":
    test_env()
