from player import Player
import operator
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import namedtuple 
import seaborn as sns
import pandas as pd 
from field import * 
import datetime
import math
import seaborn as sns
import pandas as pd

## Record each independent game's scores for player and opponent respectively.


playerWin = [] 
opponentWin = []


def eachMove(player, opponent, explore, w_p):
	
	p_current_state = player.current_state
	o_current_state = opponent.current_state
	
	oAction = opponent.takeAction()
	pAction = player.takeAction()

	pState = newState(player, pAction)
	oState = newState(opponent, oAction)

	player.updateState(pState)
	opponent.updateState(oState)
	
	meetUp(player, opponent)

# THe agents should updat the central Q-table everywhere otherwise it will never win! 
	pR = getReward(player, opponent, w_p)[0]
	oR = getReward(player, opponent, w_p)[1]

	player.updateQ(p_current_state, player.current_state, pAction, oAction, pR)
	opponent.updateQ(o_current_state, opponent.current_state, oAction, pAction, oR)

	player.updatePolicy(p_current_state)
	opponent.updatePolicy(o_current_state)

def restart(player, init_state):
	player.current_state = init_state



print('[Start Time] = ',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

for i in range(Trial):

	pWin = 0
	oWin = 0
	
	player = Player(player_goal, states, actions, playerQ, playerV, playerPi, player_start[1])
	opponent = Player(opponent_goal, states, actions, opponentQ.copy(), opponentV.copy(), opponentPi.copy(), opponent_start[1])

	
	for state in states:
		for p_action in actions:
			for o_action in actions:
				playerQ[state, p_action, o_action] = 0
	for state in states:
		for p_action in actions:
			for o_action in actions:
				opponentQ[state, p_action, o_action] = 0
	for state in states:
		for action in actions:

			playerPi[state, action]= 1/len(actions) 

	for state in states:
		for action in actions:

			opponentPi[state, action]= 1/len(actions) 

	for s in states:
		playerV[s] = 0
	for s in states:
		opponentV[s] = 0
	

	player1 = Player(player_goal, states, actions, playerQ, playerV, playerPi, player_start[0])
	player2 = Player(player_goal, states, actions, playerQ, playerV, playerPi, player_start[1])
	player3 = Player(player_goal, states, actions, playerQ, playerV, playerPi, player_start[2])

	player1.subField= subFields['back']
	player2.subField = subFields['middle']
	player3.subField = subFields['front']

	opponent1 = Player(opponent_goal, states, actions, opponentQ.copy(), opponentV.copy(), opponentPi.copy(), opponent_start[0])
	opponent2 = Player(opponent_goal, states, actions, opponentQ.copy(), opponentV.copy(), opponentPi.copy(), opponent_start[1])
	opponent3 = Player(opponent_goal, states, actions, opponentQ.copy(), opponentV.copy(), opponentPi.copy(), opponent_start[2])

	opponent1.subField = wholeField
	opponent2.subField = wholeField
	opponent3.subField = wholeField

	players = [player1, player2, player3, player]
	opponents = [opponent1, opponent2, opponent3, opponent]


	for j in range(Game):
		print('Trail = ', i, 'Game = ', j)
	
		restart(player, player_start[0])
		restart(player1, player_start[0])
		restart(player2, player_start[1])
		restart(player3, player_start[2])
		restart(opponent, opponent_start[0])
		restart(opponent1, opponent_start[0])
		restart(opponent2, opponent_start[1])
		restart(opponent3, opponent_start[2])
		

		for k in range(len(players)):

			w_p = 0.8  # initliazed partition reward weight
			vare = 0.999  # discount parameter
			player = players[k]
			opponent = opponents[k]
			
			for m in range(Movement):

				w_p = w_p * vare
				if getGoal(players[k]) or getGoal(opponents[k]):

					if getGoal(player) and k == 3:
						
						pwins[j] = pwins[j]+1
						print('Pwin!')
						break
					
					if getGoal(opponent) and k == 3:
						
						owins[j]=owins[j]+1
						print('oWin!')
						break
					
				else:
					eachMove(player, opponent, True, w_p)
					

			V = [[playerV[(x, y), True]+playerV[(x, y), False] for x in range(field[0])] for y in range(field[1])]
			
	
	del player, player1, player2, player3
	del opponent, opponent1, opponent2, opponent3
	print('[Start Time] = ',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


data_dict = {
	'result_p' : pwins,  
	'result_o' : owins,  
	}

df = pd.DataFrame(data_dict) 
df.to_csv('test1.csv') 


print('[Terminate Time] = ',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


plt.plot(pwins)
plt.plot(owins)
plt.title('update subflieds/opponents run algorithm')
plt.show()











