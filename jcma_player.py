from game_logic import *
from jcma_minimax_player import minimax

def play(game, player):
    return minimax(game, player, 3, heuristic, moves)

def moves(game, player):
	for x in range(game.size):
		for y in range(game.size):
			if game[x, y] == EMPTY:
				yield (x, y)


def heuristic(game, player):
    oponent = 'W' if player=='B' else 'B'
    p_len = connected(game, player)
    o_len = connected(game, oponent)
    return 0 if o_len == p_len else (o_len - p_len) / max(p_len, o_len)

def connected(game, player):
    join = set()
    
    for i in range(game.size):
        for j in range(game.size):
            if game[i,j] == player:
                neighbors = game.neighbour(i,j)
                for r, c in neighbors:
                    if game[r,c] == player and (r,c) not in join:
                        join.add((r, c))

    return len(join)