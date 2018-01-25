
import operator
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import namedtuple 
import seaborn as sns
import pandas as pd 

## The Soccer Field basic info


####################################  Variables   ###########################################################
Trial = 10
Game = 300
Movement = 50
score = 1000
Group = 3
per_par = 0.5

pwins = [0]*Game
owins = [0]*Game

field = (9, 4)
#states = [(x, y) for x in range(field[0]) for y in range(field[1])]
states = [((x, y), ball) for x in range(field[0]) for y in range(field[1]) for ball in [True, False]]
actions = [ (0, 1), (1, 0),(-1, 0), (0, -1)]

player_goal = ((-1, 1), (-1, 2))
opponent_goal = ((9, 1), (9, 2))


# the sart should be randomly generated!
player_start = [((7, 2), True),((4, 1), True),((2, 2), True)]
opponent_start = [((6, 2), False),((3, 2), False),((1, 1), False)]

front_field = [(x, y) for x in np.arange(0, int(field[0]/3), 1) for y in range(field[1])] #(0, int(field[0]/3-1))
middle_field = [(x, y) for x in np.arange(int(field[0]/3), int(2*field[0]/3), 1) for y in range(field[1])] # (int(field[0]/3), int(2*field[0]/3-1))
back_field = [(x, y) for x in np.arange(int(2*field[0]/3), int(field[0]), 1) for y in range(field[1])]  #(int(2*field[0]/3), int(field[0]))


subFields = {'front': front_field, 'middle': middle_field, 'back': back_field}
wholeField = [(x, y) for x in range(field[0]) for y in range(field[1])]


playerQ = {(state, p_action, o_action): 0 for state in states for p_action in actions for o_action in actions}
opponentQ = {(state, p_action, o_action): 0 for state in states for p_action in actions for o_action in actions}
playerPi = {(state, action): 1/len(actions) for state in states for action in actions}
opponentPi = {(state, action): 1/len(actions) for state in states for action in actions}
playerV = {s: 0 for s in states}
opponentV = {s: 0 for s in states}

partition_r = 100
goal_r = 1000
#w_p = 0.8
#vare = 0.9



####################################  Functions   ###########################################################

def getGoal(player):
	if player.current_state[0] in player.goal and player.current_state[1]:
		return True
	else:
		return False

def meetUp(player, opponent):
	if player.current_state[0] == opponent.current_state[0]:
		#print('player.current_state[1]', player.current_state[1])
		player.current_state = (player.current_state[0], not player.current_state[1])
		opponent.current_state = (opponent.current_state[0], not opponent.current_state[1])
		# player.current_state[1] = not player.current_state[1]
		# opponent.current_state[1] = not opponent.current_state[1]
		

def newState(player, action):
	
	new_s =  tuple(map(operator.add, player.current_state[0], action))
	if ((new_s, player.current_state[1]) in player.states) or (((new_s in player.goal) and (player.current_state[1] == True))):
		
		return (new_s, player.current_state[1])
	else:
		
		return player.current_state
		
	
def getpartitionR(player):

	if player.subField != None:
		#if player.current_state in subFields[player.subField]:
		if player.current_state[0] in player.subField:
			return partition_r  
		else:
			return 0
	else: 
		return 0

def underlyReward(player, opponent):  ## Return the (player.reward, opponent.reward)
	if (player.current_state[0] in player_goal) and (player.current_state[1] == True) :
		return (goal_r, -goal_r)
		
	elif (opponent.current_state[0] in opponent_goal) and (opponent.current_state[1] == True):
		return (-goal_r, goal_r)
	else:
		return (0, 0)

def getReward(player, opponent, w_p):
	#print(underlyReward(player, opponent))
	p_under_r = underlyReward(player, opponent)[0]
	o_under_r = underlyReward(player, opponent)[1]
	p_r = (1- w_p)*p_under_r + w_p * getpartitionR(player)
	o_r = (1- w_p)*o_under_r + w_p * getpartitionR(opponent)
	#print(p_r, o_r)
	return (p_r, o_r)


def clear_tables(playerQ, opponentQ, playerPi, opponentPi, playerV, opponentV):
	playerQ = {(state, p_action, o_action): 0 for state in states for p_action in actions for o_action in actions}
	opponentQ = {(state, p_action, o_action): 0 for state in states for p_action in actions for o_action in actions}
	playerPi = {(state, action): 1/len(actions) for state in states for action in actions}
	opponentPi = {(state, action): 1/len(actions) for state in states for action in actions}
	playerV = {s: 0 for s in states}
	opponentV = {s: 0 for s in states}


































