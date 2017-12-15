from player import Player
import operator
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import namedtuple 
import seaborn as sns
import pandas as pd 
from field import * 

## Record each independent game's scores for player and opponent respectively.


playerWin = [] 
opponentWin = []

def groupGame(player, opponent, pWin, oWin, explore, main):




	for i in range(Movement):


		p_current_state = player.current_state
		o_current_state = opponent.current_state

		if getGoal(player):
			if main == True:
				pWin = pWin + 1
			break

		elif getGoal(opponent):
			if main == True:
				oWin = oWin + 1
			break
		
		if explore == True:

			pAction = player.takeAction()
			oAction = opponent.takeAction()

		else:

			pAction = player.exploit()
			oAction = opponent.exploit()

		pState = newState(player, pAction)
		oState = newState(opponent, oAction)

		player.updateState(pState)
		opponent.updateState(oState)
			
		meetUp(player, opponent)

		pR = getReward(player, opponent)[0]
		oR = getReward(player, opponent)[1]

		player.updateQ(p_current_state, player.current_state, pAction, oAction, pR)
		opponent.updateQ(o_current_state, opponent.current_state, oAction, pAction, oR)

		player.updatePolicy(p_current_state)
		opponent.updatePolicy(o_current_state)



def restart(player, init_state):
	player.current_state = init_state


for i in range(Trial):

	# Make mutiple copies of the players to accelerate

	player = Player(player_goal[0], True, states, actions, playerQ, playerPi, player_start[0])
	opponent = Player(opponent_goal, False, states, actions, opponentQ.copy(), opponentPi, opponent_start[0])
	player1 = Player(player_goal[0], True, states, actions, playerQ, playerPi, player_start[0])
	player2 = Player(player_goal[0], True, states, actions, playerQ, playerPi, player_start[1])
	player3 = Player(player_goal[0], True, states, actions, playerQ, playerPi, player_start[2])

	player1.subField= subFields['back']
	player2.subField = subFields['middle']
	player3.subField = subFields['front']

	opponent1 = Player(opponent_goal, False, states, actions, opponentQ.copy(), opponentPi, opponent_start[0])
	opponent2 = Player(opponent_goal, False, states, actions, opponentQ.copy(), opponentPi, opponent_start[1])
	opponent3 = Player(opponent_goal, False, states, actions, opponentQ.copy(), opponentPi, opponent_start[2])

	pWin = 0
	oWin = 0

	for j in range(Game):

		restart(player, player_start[0])
		restart(player1, player_start[0])
		restart(player2, player_start[1])
		restart(player3, player_start[2])
		restart(opponent, opponent_start[0])
		restart(opponent1, opponent_start[0])
		restart(opponent2, opponent_start[1])
		restart(opponent3, opponent_start[2])


		groupGame(player1, opponent1, pWin, oWin, True, False)
		groupGame(player2, opponent2, pWin, oWin, True, False)
		groupGame(player3, opponent3, pWin, oWin, True, False)
		groupGame(player3, opponent3, pWin, oWin, False, True)


	playerWin.append(pWin)
	opponentWin.append(oWin)
	
	del player, player1, player2, player3
	del opponent, opponent1, opponent2, opponent3


print('[pWin] = ', pWin)













