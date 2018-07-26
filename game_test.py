from Connect4.connect4 import *
from agents import *






def dev_test():
    env = Connect4(verbose=True)
    env.render()
    action_list = np.random.randint(7,size=200)
    # action_list = [0,0,0,0,2,1,1,1,5,3,5,2,5,5,5,5,5]

    for a in action_list:
        state_, reward, done, _ = env.step(a)
        env.render()
        if done:
            print ("GAME OVER MAN...GAME OVER")
            break

def agent_test():
    # r = RandomAgent(7)
    r = HumanAgent(7)
    h = HumanAgent(7)
    agents = [h,r]
    env = Connect4(verbose=True)
    env.render()
    agent_index = np.random.randint(1)
    done = False
    while not done:
        agent = agents[agent_index]
        state_, reward, done, _ = env.step(agent.act())
        env.render()
        agent_index = (agent_index + 1)%len(agents)
        if done:
            print ("GAME OVER MAN...GAME OVER")
            break

if __name__ == "__main__":
    agent_test()
