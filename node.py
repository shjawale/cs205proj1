import priorityqueue, copy

#recesses = [3,5,7]
#recesses = [1, 2]
#recesses = [1,2,3,4,5]

class Node():
    print('in node class')
    def __init__(self, parent, g, puzzle = None):
        self.parent = parent  #since we create a new node when we still have the parent. we can have parent as an argument
        self.gn = g
        self.hn = 0
        self.recesses = list()
        self.currPuzzleLayout = copy.deepcopy(puzzle)  #copy instead of reference

    def printPuzzle(self):
        print(self.currPuzzleLayout)
        '''
        for c in range(9):
            if (c==3) or (c==5) or (c==7):
                print(self.currPuzzleLayout[c][0], self.currPuzzleLayout[c][1])
            else:
                print(self.currPuzzleLayout[c])
        '''
    
    def findRecesses(self):
        for i in range(len(self.currPuzzleLayout)):
            if self.currPuzzleLayout[0][i] == 0:
                self.recesses.append(i)
        print("recesses =", self.recesses)

    def isGoalState(self, prob):
        return self.currPuzzleLayout == prob.goal_state.currPuzzleLayout  #goal_state will be a node

    def update(self, parentnode, g):
        self.parent = parentnode
        self.gn = g

    def goDown(self): #returns new node with self as parent and new calculated currPuzzle, g(n), h(n)
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        #print("in goDown()")
        '''
        for c in self.recesses:
            #print("adjacentNode.currPuzzleLayout[c] =", adjacentNode.currPuzzleLayout[c])
            if adjacentNode.currPuzzleLayout[c][0] == 0:
                adjacentNode.currPuzzleLayout[c][0] = adjacentNode.currPuzzleLayout[c][1]
                adjacentNode.currPuzzleLayout[c][1] = 0
                return adjacentNode
        '''
        for c in self.recesses:
            if adjacentNode.currPuzzleLayout[0][c] == 0:
                adjacentNode.currPuzzleLayout[0][c] = adjacentNode.currPuzzleLayout[1][c]
                adjacentNode.currPuzzleLayout[1][c] = 0
                return adjacentNode
        return None

    def goUp(self):
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        '''
        for c in self.recesses:
            #print("adjacentNode.currPuzzleLayout[c] =", adjacentNode.currPuzzleLayout[c])
            if adjacentNode.currPuzzleLayout[c][1] == 0:
                adjacentNode.currPuzzleLayout[c][1] = adjacentNode.currPuzzleLayout[c][0]
                adjacentNode.currPuzzleLayout[c][0] = 0
                return adjacentNode
        '''
        for c in self.recesses:
            if adjacentNode.currPuzzleLayout[1][c] == 0:
                adjacentNode.currPuzzleLayout[1][c] = adjacentNode.currPuzzleLayout[0][c]
                adjacentNode.currPuzzleLayout[0][c] = 0
                return adjacentNode
        return None
    
    def goLeft(self):
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        for c in range(1, len(adjacentNode.currPuzzleLayout[0])):
            if adjacentNode.currPuzzleLayout[1][c] == 0:
                adjacentNode.currPuzzleLayout[1][c] = adjacentNode.currPuzzleLayout[1][c-1]
                adjacentNode.currPuzzleLayout[1][c-1] = 0
                return adjacentNode
        return None
    
    def goRight(self):
        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        for c in range(len(adjacentNode.currPuzzleLayout[0])-1): #column
            if adjacentNode.currPuzzleLayout[1][c] == 0:
                if adjacentNode.currPuzzleLayout[1][c+1] == 0:
                    print("both are 0")
                else:
                    adjacentNode.currPuzzleLayout[1][c] = adjacentNode.currPuzzleLayout[1][c+1]
                    adjacentNode.currPuzzleLayout[1][c+1] = 0
                    return adjacentNode
        return None

    
    def __lt__(self, other): #should only be used by heap. we are deciding which node to keep
        #print("inside __lt__: self g(n) =", self.gn, "self h(n)", self.hn)
        return (self.gn + self.hn) < (other.gn + other.hn)
        
    def __eq__(self, other): #two nodes with the same layout are equal
        #print("inside __lt__: self g(n) =", self.gn, "self h(n)", self.hn)
        return self.currPuzzleLayout == other.currPuzzleLayout


    def __hash__(self):
        #print("inside __hash__: self hash =", hash(self.currPuzzleLayout))
        return hash((tuple(self.currPuzzleLayout[0]), tuple(self.currPuzzleLayout[1]),))


#newnode = Node(None, 0, [0,1,2])
