from p6_game import Simulator
from collections import deque

ANALYSIS = {}

def analyze(design):
	ANALYSIS.clear()
	queve = deque()
	sim = Simulator(design)
	init = sim.get_initial_state()
	#init_pos, init_ability = init
	#ANALYSIS = {next_state:current_state}
	ANALYSIS[init] = None
	queve.append(init)

	while queve:
		current_state = queve.popleft()
		#current_position,current_abilities = current_state
		moves = sim.get_moves()
		for next_move in moves:			
			next_state = sim.get_next_state(current_state,next_move)
			if next_state == None:
				continue
			#next_position, next_abilities = next_state
			if next_state not in ANALYSIS:
				ANALYSIS[next_state] = current_state
				queve.append(next_state)
				
def inspect((i,j), draw_line):
    #current_position = (i,j)
    #Draw all the paths
    for find_state in ANALYSIS:
    	#print find_state[0] 
    	if find_state[0] == (i,j):
    		while find_state:
	    		draw_line(find_state[0], ANALYSIS[find_state][0], offset_obj = None, color_obj= find_state[1])
	    		find_state = ANALYSIS[find_state]
 