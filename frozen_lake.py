import gym
import random
actions = {
    'Left': 0,
    'Down': 1,
    'Right': 2,
    'Up': 3}

def main():
    #Part 1: make some random acts first
    env = gym.make("FrozenLake-v0")
    env.reset()
    env.render()
    for iter in range(10):
        random_act=random.choice(list(actions.values()))
        new_state, reward, done, info = env.step(random_act)
        env.render()
        print("Reward: {:.2f}".format(reward))
        print(info)
        if done:
            break





if __name__ == '__main__':
    main()