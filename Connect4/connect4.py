"""
Notes:
 - Need to handle draws
 - Need to d make sure that both players get a reward when the game is finished
    - Where should this go?
    - Return tuple of P1, P2 rewards?
"""

import numpy as np

class Board:
    def __init__(self,rows=6,cols=7,players=2):
        self.board = np.zeros((rows,cols)).astype(int)
        self.rows = self.board.shape[0]
        self.cols = self.board.shape[1]
        self.in_play = np.ones(cols).astype(int)*(self.rows-1)


    def get_board(self):
        return self.board

    def make_move(self,drop_column,player):
        if not self.is_full(drop_column):
            row = self.in_play[drop_column]
            self.board[row,drop_column] = player
            self.in_play[drop_column]-=1

    def is_full(self,drop_column):
        if self.in_play[drop_column] < 0:
            return True
        else:
            return False


class Connect4:
    """
    Class for the connect 4 game.
     - Should accommodate more than 2 players
     - Should accommodate larger or smaller grids

    """
    def __init__(self,rows=6,cols=7,players=2,player_tokens = ["O","X"],
                l_reward=-1, verbose=False):
        self.board = Board(rows=rows,cols=cols,players=players)
        self.player_tokens = player_tokens
        self.players = players
        self.player_list = np.arange(players)+1
        self.player_list = self.player_list.astype(int).tolist()
        self.active_player = 1
        self.living_reward = l_reward
        self.iteration = 0
        self.ply = 0
        self.verbose=verbose
        self.invalid_move_penalty = -100
        self.win_reward = 100
        self.lose_reward = -100

    def step(self,action):
        self.board.make_move(action,self.active_player)
        new_state = self.board.get_board()
        is_done = self.check_for_win(new_state)
        if  self.check_for_draw(self.board):
            return self.get_draw()

        self.next_turn()
        reward = self.get_reward(new_state,is_done)
        extra_stuff = {"turn":self.ply,"iteration":self.iteration}
        if self.board.is_full(action):
            reward = self.invalid_move_penalty
            extra_stuff.update({"Error": "Invalid Move"})
        return new_state, reward, is_done, extra_stuff

        #TODO Modify Reward function to return dict of {player_number: reward_value}
    def get_reward(self,new_state,done):
        rewards = {}
        for p in range(self.players): rewards.update({p:0})
        if done:
            for p in range(self.players): rewards.update({p:self.lose_reward})
            rewards[self.active_player] = self.win_reward
        else:
            rewards[self.active_player] = self.living_reward
        return rewards

    def get_draw(self):
        print("It's a draw")
        rewards = {}
        for p in range(self.players): rewards.update({p:0})
        done = True
        new_state = self.board.get_board()
        extra_stuff = {
            "turn":self.ply,
            "iteration":self.iteration,
            "error": "Board is full.  It's a draw"
            }
        return new_state, rewards, done, extra_stuff

    def next_turn(self):
        self.active_player = self.player_list[self.active_player%self.players]
        self.iteration +=1
        self.ply = self.iteration/self.players

    def check_for_draw(Self,board):
        for column in range(board.cols):
            # print("Checking if column {!s} is full: ".format(board.is_full(column)))
            if not board.is_full(column):
                return False
        return True

    def check_for_win(self,board):
        # Only the active player can win, so we'll only do checks for that
        # Check for horizontal win

        diagonal_lists = []
        for i in range(self.board.rows):
            hcount = 0
            for j in range(self.board.cols):
                if board[i,j] == self.active_player: hcount +=1
                else:
                    hcount =0
                if hcount >=4:
                    if self.verbose:
                        print("HORIZONTAL WIN")
                        print ("Congratulations Player:{}!".format(str(self.active_player)))
                        print ((i,j),(i,j-1),(i,j-2),(i,j-3))
                        return True


        # Check for vertical win
        for j in range(self.board.cols):
            vcount=0
            for i in range(self.board.rows):
                if board[i,j] == self.active_player: vcount += 1
                else:vcount =0
                if vcount >=4:
                    if self.verbose:
                        print("VERTICAL WIN (COLUMN: {})".format(str(j)))
                        print ("Congratulations Player:{}!".format(str(self.active_player)))
                        print ((i,j),(i-1,j),(i-2,j),(i-3,j))
                        return True


        # Diagonal Check
        # TODO Vectorize and make wayyy better
        for i in range(self.board.rows-3):
            for j in range(self.board.cols-3):
                if board[i,j] == self.active_player and \
                   board[i+1,j+1] == self.active_player and \
                   board[i+2,j+2] == self.active_player and \
                   board[i+3,j+3] == self.active_player:
                   if self.verbose:
                       print("DIAGONAL WIN (\)")
                       print ("Congratulations Player:{}!".format(str(self.active_player)))
                       print ((i,j),(i+1,j+1),(i+2,j+2),(i+3,j+3))
                       return True
                if board[i,j] == self.active_player and \
                   board[i-1,j-1] == self.active_player and \
                   board[i-2,j-2] == self.active_player and \
                   board[i-3,j-3] == self.active_player:
                   if self.verbose:
                       print("DIAGONAL WIN (/)")
                       print ("Congratulations Player:{}!".format(str(self.active_player)))
                       print (self.active_player)
                       print ((i,j),(i-1,j-1),(i-2,j-2),(i-3,j-3))
                   return True
        return False

    def render(self):
        disp_strings = []
        for row in range(self.board.rows):
            str="| "
            for col in range(self.board.cols):
                if self.board.board[row,col]-1 in np.arange(self.players).astype(int).tolist():
                    str += "["+self.player_tokens[self.board.board[row,col]-1]+"]"
                else:
                    str += "[ ]"
                str+=" "
            str += "|"
            disp_strings.append(str)
            print(str)
        print ("******************************")
