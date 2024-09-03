# Mystical_castle
1.	parse_map function- Reads text file and processes to create a 2D List
2.	valid_index function- Check whether the 1st  element of pos is in range 0 to n and also checks if 2nd element is in 0 to m,  if both true returns true or vice versa.
3.	moves function – Returns valid possible moves considering boundary.
get_direction function- Give the direction to move from present position to next position . 
next[0], current[0] refers to row  co-ordinate 
next[1], current[1] refers to column  co-ordinate
Calculated direction based on difference between column and row co-ordinates between next and current.
For U (move up) Current position will decrement row by 1 and column will remain same which is (-1,0).
For D (move down) Current position will increment row by 1 and column will remain same which is (1,0).
For R (move Right) Current position will keep row same, while column will be incremented by 1 which is (0,1).
For L (move left) Current position will keep row same, while column will be decremented by 1 which is (0,-1).
No direction then returns empty string
4.	search function- Finds shortest distance using bfs from between your location (p) and the opening(@). It starts from p(current position) and checks all the possible moves while checking visited position respectively. It returns tuple of 3 elements- 1. Number of moves required to reach @(goal) from, pattern of moves, and a true if path was found or (-1,false) if path was not found  

# Turret Placements
Part 2: Search for Design
1.	parse_map function- reads text file and processes to create a 2D List
2. count_turrets function- this function counts total number of p (turrets) present 
3. add_turret function- Creates a new castle_map with a turret ('p') added at the specified row and column.
4. possibility function- This function takes the castle_map, rw (row), col (column), and directn (direction) as input. It checks whether it is possible to place turret in specified direction from the given position without encountering another turret ('p') or an obstacle ('X'). It will returns true if placement is possible, and false if its not.
5. successors function- It will try to add turret to every empty cell in the map and will create a list of these maps
6. is_goal function- checks whether exact number of turret are placed returns true if goal is reached and returns false if its not reached
7. solve function- Function keeps track of fringe and visited node. Also used Dfs algorithm, and it returns true and castle_map if objective is achieved else return false and empty string

This problem is similar to N-queen problem.






