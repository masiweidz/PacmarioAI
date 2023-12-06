# train.py

import torch
from env_setup import setup_mario_env
from ppo_part import PolicyNetwork, ValueNetwork
from data_processing import process_observation


def train_agent(env, policy_network, value_network, device, epochs=10, steps_per_epoch=1000):

    """
    训练代理的主要函数。

    参数:
    env: 游戏环境。
    policy_network: 策略网络。
    value_network: 价值网络。
    epochs: 训练周期数。
    steps_per_epoch: 每个周期的步数。
    """
    for epoch in range(epochs):
        observation = env.reset()
        processed_observation = process_observation(observation)
        # 这里应该包含与环境的交互、收集数据和更新网络的代码
        # 例如：states, actions, rewards, etc = collect_data(env, policy_network, steps_per_epoch)
        #       update_policy(policy_network, ...)
        #       update_value_network(value_network, ...)
        
        # 打印进度信息（可选）
        print(f'Epoch {epoch + 1}/{epochs} completed')

if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {0}")

    # 初始化环境
    env = setup_mario_env()
    num_actions = env.action_space.n
    num_inputs = env.observation_space.shape[0]  # 获取观察空间的维度

    # 创建策略和价值网络模型
    policy_network = PolicyNetwork(num_inputs, num_actions).to(device)
    value_network = ValueNetwork(num_inputs).to(device)

    # 开始训练
    train_agent(env, policy_network, value_network, device)
