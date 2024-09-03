#!/usr/local/bin/python3
#
# place_turrets.py : arrange turrets on a grid, avoiding conflicts
#
# Submitted by : [Mihir Jayantibhai Patel AND mjp5]
#
# Based on skeleton code in CSCI B551, Fall 2022.

# Discussed with Rutvij

import sys
# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of turrets on castle_map
def count_turrets(castle_map):
    return sum([ row.count('p') for row in castle_map ] )

# Return a string with the castle_map rendered in a human-turretly format
def printable_castle_map(castle_map):
    return "\n".join(["".join(row) for row in castle_map])

# Add a turret to the castle_map at the given position, and return a new castle_map (doesn't change original)
def add_turret(castle_map, row, col):
    return castle_map[0:row] + [castle_map[row][0:col] + ['p',] + castle_map[row][col+1:]] + castle_map[row+1:]

def possiblity(castle_map,rw, col, directn):
    r_max = len(castle_map)
    col_max = len(castle_map[0])
    dr, dc = 0, 0    #change in row and change in column

    if directn == 'Right':
        dc= 1
    elif directn == 'Left':
        dc= -1
    elif directn == 'Down':
        dr= 1
    elif directn == 'Up':
        dr= -1
    elif directn == 'Diag_R_Dwn':
        dr=1
        dc=1
    elif directn == 'Diag_l_Dwn':
        dr=1
        dc=-1
    elif directn == 'Diag_R_Up':
        dr=-1
        dc=1
    elif directn == 'Diag_L_Up':
        dr=-1
        dc=-1

    while 0 <= rw < r_max and 0 <= col < col_max:   #checking if turret placing is possible or not in a specified direction
        if castle_map[rw][col] == 'p':           #to check if turret is there or not already
            return False
        if castle_map[rw][col] in 'X':      # to check if there is obstacle in current posi or not
            break
        rw=rw+ dr
        col=col+dc

    return True



# Get list of successors of given castle_map state
def successors(castle_map):
    drctn= ['Right', 'Left', 'Down', 'Up', 'Diag_R_Dwn', 'Diag_l_Dwn', 'Diag_R_Up', 'Diag_L_Up']
    return [ add_turret(castle_map, r, c) for r in range(0, len(castle_map)) for c in range(0,len(castle_map[0])) if castle_map[r][c] == '.' and all(possiblity(castle_map, r, c, direction) for direction in drctn) ]

# check if castle_map is a goal state
def is_goal(castle_map, k):
    return count_turrets(castle_map) == k 

# Arrange turrets on the map
#
# This function MUST take two parameters as input -- the castle map and the value k --
# and return a tuple of the form (new_castle_map, success), where:
# - new_castle_map is a new version of the map with k turrets,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_castle_map, k):
    fringe = [initial_castle_map]
    visit = set()

    while len(fringe) > 0:
        for new_castle_map in successors(fringe.pop()):
            # Convert the list to a tuple before using it in the set
            new_castle_map_tuple = tuple(map(tuple, new_castle_map))
            if new_castle_map_tuple in visit:
                continue
            elif is_goal(new_castle_map_tuple, k):
                return (new_castle_map_tuple, True)
            visit.add(new_castle_map_tuple)
            fringe.append(list(map(list, new_castle_map_tuple)))

    return [], False



# Main Function
if __name__ == "__main__":
    castle_map=parse_map(sys.argv[1])
    # This is k, the number of turrets
    k = int(sys.argv[2])
    print ("Starting from initial castle map:\n" + printable_castle_map(castle_map) + "\n\nLooking for solution...\n")
    solution = solve(castle_map,k)
    print ("Here's what we found:")
    print (printable_castle_map(solution[0]) if solution[1] else "False")
