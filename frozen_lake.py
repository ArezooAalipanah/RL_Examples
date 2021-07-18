"""1. Implement policy iteration. The stopping tolerance (defined as
maxs |Vold(s) − Vnew(s)|) is tol = 10−3. Use γ = 0.9. Return the optimal value function and
the optimal policy.
2. Implement value iteration in vi_and_pi.py. The stopping tolerance is tol = 10−3.
Use γ = 0.9. Return the optimal value function and the optimal policy.
"""
import gym
import random

actions = {
    'Left': 0,
    'Down': 1,
    'Right': 2,
    'Up': 3}
IS_STOCHASTC=False

def main():
    #random_acts(IS_STOCHASTC)
    value_iter(IS_STOCHASTC)
    policy_iter(IS_STOCHASTC)



def value_iter(IS_STOCHASTC):
    env = make_env(IS_STOCHASTC)
    env.reset()
    env.render()
    for i in range(5):
        new_state, reward, done, info = env.step()
        env.render()
        print("Reward: {:.2f}".format(reward))
        print(info)
        if done:
            break


def policy_iter(IS_STOCHASTC):
    env = make_env(IS_STOCHASTC)
    env.reset()
    env.render()
    for i in range(5):
        new_state, reward, done, info = env.step()
        env.render()
        print("Reward: {:.2f}".format(reward))
        print(info)
        if done:
            break


def random_acts(IS_STOCHASTC):
    # To make some random acts
    env = make_env(IS_STOCHASTC)
    env.reset()
    env.render()
    """point: The 'prob' element is showing with how much probability the agent 
    would select another action, in order to make your world deterministic use
    env = gym.make("FrozenLake-v0", is_slippery=False) instead.
    In order to make your custom map or use other maps add 
    map_name='8x8'(or the custom one you've made) inside the parentheses """
    for iter in range(3):
        random_act=random.choice(list(actions.values()))
        new_state, reward, done, info = env.step(random_act)
        env.render()
        print("Reward: {:.2f}".format(reward))
        print(info)

def make_env(IS_STOCHASTC):
    if IS_STOCHASTC:
        env=gym.make("FrozenLake-v0")
    else:
        env=gym.make("FrozenLake-v0",is_slippery=False)
    return env


if __name__ == '__main__':
    main()