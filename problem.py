import node

class Problem:
    def __init__(self, initial):
        self.initial_state = initial
        self.goal_state = node.Node(None, 0, [[-1, 0, -1, 0, -1, 0, -1, 0, -1, -1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]])
        #self.goal_state = node.Node(None, 0, [[-1, -1, 0, 0, -1], [1, 2, 3, 4, 0]])
        #self.goal_state = node.Node(None, 0, [[-1,0,-1], [1,2,0]])
        #self.operators = ["goLeft", "goDown", "goRight", "goUp"]


#puzzle = [0,1,2,3,4,5]
#problem = Problem(puzzle)
#print(problem.initial_state)
