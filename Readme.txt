# MinimaxSoccer

This is an implement of my proposed work called "STATE-SPACE PARTITION-BASED Q-LEARNING (SPQ)".
One player's learning can be accelerated by duplicating into multiple players and share informaiton via a central Q-table. 
Each player also use MinimaxQ to learn how to player.


player.py is the class for players.
field.py contains all setting and functions for a soccer field.
game.py is the game. 


Trail: independent experiments number; game: games number in each experiment; movement is the maximum movenments for each game
Each game overs whether when there is a player shoot the goal or the total movements reach the maximum. 





