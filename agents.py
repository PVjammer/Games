import numpy as np


def load_config(file_name):
    with open(file_name) as f:
        config = yaml.load(f)
    return config

class RandomAgent:
    def __init__(self,n_actions):
        self.n_actions = n_actions

    def act(self):
        return np.random.randint(self.n_actions)

class HumanAgent:
    def __init__(self,n_actions):
        self.n_actions = n_actions
        self.actions = np.arange(n_actions).astype(int)
    def act(self):
        string = "Please enter the column into which you wish to drop your piece (Choices ["
        for a in self.actions:
            string += str(a) + " "
        string += "]): "
        action = input(string)
        # print (type(action))
        try:
            return self.actions[int(action)]
        except Exception as e:
            # print (action)
            # print (e)
            print("You're an idiot, I'm choosing for you!")
            return np.random.randint(self.n_actions)
