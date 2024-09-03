#!/usr/local/bin/python3
#
# mystical_castle.py : a maze solver
#
# Submitted by : [Mihir Jayantibhai Patel AND mjp5]
#
# Based on skeleton code provided in CSCI B551, Fall 2023.

import sys
#from queue import Queue
# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the castle_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
# This function MUST take a single parameter as input -- the castle map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

# referred tutorial points & geeks for geeks  

def directn(current, next):
    diff = (next[0] - current[0], next[1] - current[1])   #gives  directn  
    directn = {"U": (-1, 0), 
               "D": (1, 0), 
               "L": (0, -1), 
               "R": (0, 1)}
    for d, move in directn.items():
        if move == diff:
            return d
    return ""


def search(castle_map):
     # Find current start position
    current_loc = [(row_i, col_i) for col_i in range(len(castle_map[0])) for row_i in range(len(castle_map)) if castle_map[row_i][col_i] == "p"][0]
    fringe = [(current_loc, 0, "")]              # start position in current_loc, dist (0), empty string
    visit = set()                      #positions that it has already been to (v)

    while fringe:
        (curr_move, curr_dist, path_p) = fringe.pop(0)        #before I was just using pop instead of pop(0) due to which it was giving different route.      
        
        if curr_move in visit:          #if position is visited skip it
            continue
        visit.add(curr_move)     

        if castle_map[curr_move[0]][curr_move[1]] == "@":
            return (curr_dist, path_p)                        #return a dummy answer

        for move in moves(castle_map, *curr_move):   #all possible moves from currnt position and adding it to fringe
            dist_n = curr_dist + 1
            path_n = path_p + directn(curr_move, move)
            fringe.append((move, dist_n, path_n))

    return (-1, "path not available")


# Main Function
if __name__ == "__main__":
        castle_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(castle_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])
        

