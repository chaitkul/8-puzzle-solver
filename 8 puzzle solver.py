from copy import deepcopy
from queue import Queue

# Initializing the start_node and the goal_node
start_node = [[1, 0, 3], [4, 2, 6], [7, 5, 8]]
goal_node = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Finding the position of the blank tile using for loops
def find_blank_tile(current_state):
     for i in range(0,3):
          for j in range(0,3):
               if current_state[i][j] == 0:
                    return i,j

# Function to move the blank tile (0) to the left and return None if action is not possible
def move_left(current_state):
    for i in range(0,3):
        for j in range(0,3):
            if current_state is not None and current_state[i][j] == 0:
                if j>0 and j<=2:
                    child_node1 = deepcopy(current_state)
                    child_node1[i][j] = child_node1[i][j-1]
                    child_node1[i][j-1] = 0
                    return child_node1
    return None

# Function to move the blank tile (0) to the right and return None if action is not possible
def move_right(current_state):
    for i in range(0,3):
        for j in range(0,3):
            if current_state is not None and current_state[i][j] == 0:
                if j>=0 and j<2:
                    child_node2 = deepcopy(current_state)
                    child_node2[i][j] = child_node2[i][j+1]
                    child_node2[i][j+1] = 0
                    return child_node2
    return None

# Function to move the blank tile (0) up and return None if action is not possible
def move_up(current_state):
    for i in range(0,3):
        for j in range(0,3):
            if current_state is not None and current_state[i][j] == 0:
                if i>0 and i<=2:
                    child_node3 = deepcopy(current_state)
                    child_node3[i][j] = child_node3[i-1][j]
                    child_node3[i-1][j] = 0
                    return child_node3
    return None

# Function to move the blank tile (0) down and return None if action is not possible
def move_down(current_state):
    for i in range(0,3):
        for j in range(0,3):
            if current_state is not None and current_state[i][j] == 0:
                if i>=0 and i<2:
                    child_node4 = deepcopy(current_state)
                    child_node4[i][j] = child_node4[i+1][j]
                    child_node4[i+1][j] = 0
                    return child_node4
    return None

# Creating data structures Dictionary and Queue
# Dictionary is used to store the explored nodes and their index which will be used in backtracking
# Queue is used store the nodes which are yet to be explored

explored_nodes = {}
queue = Queue()
explored_nodes[str(start_node)] = None
queue.put(start_node)

# The Breadth First Search Algorithm
# Until the queue is not empty, perform Left, Right, Up and Down functions and add the new nodes generated to the queue.
# Add the newly generated node in the explored dictionary only if it is not present already and it's not 'None'.

def breadth_first_search():
    while not queue.empty():
        current_node = queue.get()
        if current_node == goal_node:
            break
        else:
            child_node1 = move_left(current_node)
            if str(child_node1) is not None and str(child_node1) not in explored_nodes:
                    queue.put(child_node1)
                    explored_nodes[str(child_node1)] = current_node
            child_node2 = move_right(current_node)
            if str(child_node2) is not None and str(child_node2) not in explored_nodes:
                    queue.put(child_node2)
                    explored_nodes[str(child_node2)] = current_node        
            child_node3 = move_up(current_node)
            if str(child_node3) is not None and str(child_node3) not in explored_nodes:
                    queue.put(child_node3)
                    explored_nodes[str(child_node3)] = current_node        
            child_node4 = move_down(current_node)
            if str(child_node4) is not None and str(child_node4) not in explored_nodes:
                    queue.put(child_node4)
                    explored_nodes[str(child_node4)] = current_node     
   
# This function is used for backtracking
# The data is stored in the dictionary as {child : parent}
# After reaching the goal node we use the parent node to find way back to the start node.

def generate_path(start_node, goal_node):
    backtrack_path = []
    current_node = goal_node
    while explored_nodes[str(current_node)] != explored_nodes[str(start_node)]:
        backtrack_path.append(current_node)
        current_node = explored_nodes[str(current_node)]
    backtrack_path.append(start_node)
    backtrack_path.reverse()
        
    # Print data in the form of a 3x3 matrix
    for column in backtrack_path:
        for row in column:
            print(row)
        print()
    
    return backtrack_path

# Calling the Search Algorithm and the path generation function.

breadth_first_search()
backtrack_path = generate_path(start_node, goal_node)

# nodePath = backtrack_path
# with open("nodePath_testcase2.txt", "w") as f:
#     for list in nodePath:
#         for inner_list in list:
#             f.write(" ".join(str(elem) for elem in inner_list) + " ")
#         f.write("\n")

# nodes = explored_nodes

# with open("nodes_testcase2.txt", "w") as f:
#     for list in nodes:
#         for inner_list in list:
#             for inner_list1 in inner_list:
#                 for inner_list2 in inner_list1:
#                     f.write(" ".join(str(elem) for elem in inner_list2) + " ")
#         f.write("\n")
