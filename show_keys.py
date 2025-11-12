# 运行前保存为 show_keys.py 并在你的 conda 环境中执行： python show_keys.py
import gym
import gym_super_mario_bros
from pyglet.window import key as pyg_key

env = gym.make('SuperMarioBros-v0')  # 或你想查询的 env id
get_map = env.get_keys_to_action if hasattr(env, 'get_keys_to_action') else env.unwrapped.get_keys_to_action
mapping = get_map()

def key_name(k):
    try:
        return pyg_key.symbol_string(k)
    except Exception:
        return str(k)

for keys, action in mapping.items():
    # keys 是按键常量的 tuple，转换为可读名字
    names = tuple(key_name(k) for k in keys)
    print(f"{names} -> action {action}")

env.close()