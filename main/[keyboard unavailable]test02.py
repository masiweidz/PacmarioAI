import nes_py
import time
from pynput import keyboard

# 初始化 NES 环境
rom_path = r'C:\Users\Bear\.conda\envs\StreetFighterAI\Lib\site-packages\retro\data\stable\StreetFighterIISpecialChampionEdition-Genesis\Super Mario Bros. (World).nes'
env = nes_py.NESEnv(rom_path)
env.reset()
env.render()

# 定义动作映射
key_action_mapping = {
    'j': 1,
    'k': 2,
    '1': 3,
    '2': 4,
    'w': 5,  # 向上的动作
    's': 6,  # 向下的动作
    'a': 7,  # 向左的动作
    'd': 8,   # 向右的动作
}

# 当前动作
current_action = 0

# 定义键盘监听器的回调函数
def on_press(key):
    global current_action
    try:
        key_char = key.char
        if key_char in key_action_mapping:
            current_action = key_action_mapping[key_char]
    except AttributeError:
        pass

def on_release(key):
    global current_action
    current_action = 0  # 当键释放时，设置动作为默认状态

# 监听键盘
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# 主循环
try:
    while True:
        state, reward, done, info = env.step(current_action)
        env.render()
        time.sleep(0.01)
        if done:
            env.reset()
except KeyboardInterrupt:
    env.close()
    listener.stop()