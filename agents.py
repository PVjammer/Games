import numpy as np
from Connect4.rules import Connect4Rules
from HeuristicAgent.simple_functions import *


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

class HeuristicAgent:
    """
    General Agent which implements minimax with A/B pruning and evalates a user
    defined objective function (or a library function) at maximum depth.
    """
    def __init__(self, eval_func=None, config=None, game_rules=Connect4Rules()):
        if obj_func is not none:
            self.eval_function = obj_func
        else:
            self.eval_function = random_move
        if game_rules is not None:
            self.rules = game_rules

    def get_open_moves(board_state):
        if self.rules is not None:
            return self.rules.get_valid_moves(board_state)
        else:
            return None

    def act(self, state):
        pass

    def alpha_beta(self):
        pass

    def minimax(self):
        pass

    def ab_max(self):
        pass

    def ab_min(self):
        pass



class DQNAgent:
    def __init__(self, num_states, num_actions, model=None, config=None):
        if config is not None:
            pass
            #TODO Get default params from DeepQ Library
