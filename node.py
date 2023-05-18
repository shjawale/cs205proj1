import priorityqueue, copy

#recesses = [3,5,7]
#recesses = [2,3]

#newnode = Node(None, 0, [0,1,2])

class Node():
    print('in node class')
    def __init__(self, parent, g, puzzle = None):
        self.parent = parent  #since we create a new node when we still have the parent. we can have parent as an argument
        self.gn = g
        self.hn = 0
        #self.currPuzzleLayout = copy.deepcopy(puzzle)  #copy instead of reference
        self.currPuzzleLayout = list()
        self.currPuzzleLayout.append( list(puzzle[0]) )
        self.currPuzzleLayout.append( list(puzzle[1]) )
        global_recesses = list()
        length = 0
        mapofPuzzle = dict()

    def isGoalState(self, prob):
        return self.currPuzzleLayout == prob.goal_state.currPuzzleLayout  #goal_state will be a node

    def update(self, parentnode, g):
        self.parent = parentnode
        self.gn = g

    def findEmptySpaces(self):
        emptySpaces = list()
        for c in range(len(self.currPuzzleLayout[0])): #column
            if self.currPuzzleLayout[0][c] == 0:
                emptySpaces.append([0,c])
            if self.currPuzzleLayout[1][c] == 0:
                emptySpaces.append([1,c])
        return emptySpaces
        
    #added function for cs205
    def findNeighbors(self, posEmptySpace):
        newNodeList = list()
        pass #print("posEmptySpace =", posEmptySpace)

        newNode = self.goUp(posEmptySpace) #newNode is a node containing the new puzzle layout
        if newNode is not None:
            newNodeList.append(newNode) #list of all new nodes adjacent to chosen node
            pass #print("  Up", newNode.currPuzzleLayout)
        
        newNode = self.goDown(posEmptySpace)
        if newNode is not None:
            newNodeList.append(newNode) #list of all new nodes adjacent to chosen node
            pass #print("  Down", newNode.currPuzzleLayout)

        newNode = self.goLeft(posEmptySpace)
        if newNode is not None:
            newNodeList.append(newNode) #list of all new nodes adjacent to chosen node
            pass #print("  Left", newNode.currPuzzleLayout)

        newNode = self.goRight(posEmptySpace)
        if newNode is not None:
            newNodeList.append(newNode) #list of all new nodes adjacent to chosen node
            pass #print("  Right", newNode.currPuzzleLayout)

        #for nodeI in newNodeList:
        #    print("in findNeighbors nodeNewList =", nodeI.currPuzzleLayout)

        return newNodeList

    #modified functions for cs205
    def goUp(self, posES):
        if not ((posES[0] == 1) and (posES[1] in Node.global_recesses)):    #any position except for in recesses
            #print("  in Up posES =", posES, global_recesses)
            return None

        k = self.currPuzzleLayout[0][posES[1]]
        if k == 0:
            return None

        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        adjacentNode.currPuzzleLayout[1][posES[1]] = k
        adjacentNode.currPuzzleLayout[0][posES[1]] = 0
        adjacentNode.hn = self.hn - 1
        #print("in Up:", adjacentNode.emptySpaces)
        return adjacentNode

    def goDown(self, posES): #returns new node with self as parent and new calculated currPuzzle, g(n), h(n)
        if not ((posES[0] == 0) and (posES[1] in Node.global_recesses)):    #any position except for in recesses
            #print("  in Down posES =", posES, global_recesses)
            return None

        k = self.currPuzzleLayout[1][posES[1]]
        if k == 0:
            return None

        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        adjacentNode.currPuzzleLayout[0][posES[1]] = k
        adjacentNode.currPuzzleLayout[1][posES[1]] = 0
        adjacentNode.hn = self.hn + 1
        return adjacentNode

    def goLeft(self, posES):
        if not ((posES[0] == 1) and ((posES[1] >= 1) and (posES[1] < Node.length))):    #any position except for in recesses
            #print("  in Left posES =", posES, length)
            return None

        k = self.currPuzzleLayout[1][posES[1]-1]            #k is value you want to swap with 0
        if k == 0:
            return None

        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout) #create newNode and modify 0's position
        adjacentNode.currPuzzleLayout[1][posES[1]] = k
        adjacentNode.currPuzzleLayout[1][posES[1]-1] = 0
        if Node.mapofPuzzle[k] < posES[1]:                               #desired pos of k
            adjacentNode.hn = self.hn + 1
        else:                                                       #>= since reaching the correct pos should decrease hn
            adjacentNode.hn = self.hn - 1
        return adjacentNode
    
    def goRight(self, posES):
        if not ((posES[0] == 1) and ((posES[1] >= 0) and (posES[1] < Node.length-1))):    #any position except for in recesses
            #print("  in Right posES =", posES, length)
            return None

        k = self.currPuzzleLayout[1][posES[1]+1]            #k is value you want to swap with 0
        if k == 0:
            return None

        adjacentNode = Node(self, self.gn+1, self.currPuzzleLayout)     #create newNode and modify 0's position
        adjacentNode.currPuzzleLayout[1][posES[1]] = k 
        adjacentNode.currPuzzleLayout[1][posES[1]+1] = 0
        if Node.mapofPuzzle[k] > posES[1]:                               #desired pos of k
            adjacentNode.hn = self.hn + 1
        else:   #<= since reaching the correct pos should decrease hn
            adjacentNode.hn = self.hn - 1
        return adjacentNode
    
    def __lt__(self, other): #should only be used by heap. we are deciding which node to keep
        #print("inside __lt__: self g(n) =", self.gn, "self h(n)", self.hn)
        return (self.gn + self.hn) < (other.gn + other.hn)
        
    def __eq__(self, other): #two nodes with the same layout are equal
        #print("inside __lt__: self g(n) =", self.gn, "self h(n)", self.hn)
        return self.currPuzzleLayout == other.currPuzzleLayout


    def __hash__(self):
        #print("inside __hash__: self hash =", hash(self.currPuzzleLayout))
        return hash((tuple(self.currPuzzleLayout[0]), tuple(self.currPuzzleLayout[1]),))

