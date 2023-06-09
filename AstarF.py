#function GraphSearch(problem) returns a solution, or failure
#   initialize the frontier using the initial state of problem
#   initialize the explored set to be empty
#   LOOP DO:
#       IF the frontier is empty:
#           return failure
#       choose a leaf node and remove it from the frontier
#       IF the node contains a goal state:
#           return corresponding solution
#       IF choosen node is in the frontier, update node. IF chosen node is in explored set, do nothing:
#           expand the chosen node, adding the resulting node to the frontier
#       add the node to the explored set

# uniform cost search
# dequeue nodes in order of their cost (from initial node), g(n)
#   which is the same as A* = g(n) + h(n) where h(n) = 0

import priorityqueue, node, sys


def Astar(problem, estcost):  #returns either a solution or failure
    frontier = priorityqueue.priorityQueue()  #needs to be a priority queue (min heap)
    frontier_set = set()
    print("problem.initial_state =", problem.initial_state)
    
    #initialize the frontier using the initial state of problem
    root = node.Node(None, 0, problem.initial_state)
    #print("root =", root.currPuzzleLayout)
    #root.findRecesses()     #find the recesses                                     #added line for cs205
    #print("root.recesses =", root.recesses)                                        #added line for cs205
    frontier.push(root) #, root.gn, root.hn)
    frontier_set.add(root)
    #print("frontier after pushing root =", frontier.queue[0].currPuzzleLayout)

    root.hn = estcost(root.currPuzzleLayout, problem.goal_state.currPuzzleLayout)
   
    #uctree = tree.Tree()
    #uctree.source = root

    #initialize the explored set to be empty
    explored = set()
    #print("explored =", explored)

    while True:
        #print("in while loop")
        if frontier.isEmpty():
            return "failure" #what will failure look like??
        
        #choose a leaf node and remove it from the frontier
        #   the node with the least g(n) will be removed
        #       how to calculate g(n)??
        nodewithmingn = frontier.popmin()                       #initialize nodewithmingn with the first node in current frontier (which should be the node with the minimum g(n))
        frontier_set.remove(nodewithmingn)

        print("popped min from frontier", nodewithmingn.currPuzzleLayout, "f(n) =", nodewithmingn.gn+nodewithmingn.hn, "with a g(n) =", nodewithmingn.gn, "and a h(n) =", nodewithmingn.hn, "and a queue size of", len(frontier.queue))
        if 0 :
            if len(frontier.queue) > 1000 :
                sys.exit(0)
    
        if nodewithmingn.isGoalState(problem):
            #return nodewithmingn.findPath()
            return "found solution" #corresponding solution

        #expand chosen node, creating new nodes.
        #   if any new nodes are in explored set, do nothing:
        #   check if each is in the frontier. if it is, update or add to frontier.
        allnewnodes = list()
       
        #added for cs205
        emptySpaces = nodewithmingn.findEmptySpaces()
        for singleEmptySpace in emptySpaces:      #iterate through nodewithmingn.emptySpaces and find theneighboring nodes for each
            newNodeList = nodewithmingn.findNeighbors(singleEmptySpace)

            for nodeI in newNodeList:
                #nodeI.hn = estcost(nodeI.currPuzzleLayout, problem.goal_state.currPuzzleLayout)
                pass #print("nodeI =", nodeI.currPuzzleLayout)
                allnewnodes.append(nodeI)                           #list of all new nodes adjacent to chosen node

            
        if 0 :
            for i in range(len(allnewnodes)):
                print("after loop: allnewnodes[",i, "] =", allnewnodes[i].currPuzzleLayout)

        for n in allnewnodes: #iterate over nodes
            #print("n.currPuzzleLayout =", n.currPuzzleLayout)
            if (nodewithmingn.gn) > (n.gn):    #lower cost   (does not need hn)
                pass #print("lower", n.currPuzzleLayout, "f(n) =", n.gn+n.hn, "with a g(n) =", n.gn, "and a h(n) =", n.hn, "and a queue size of", len(frontier.queue))
            if n in explored:                                   #returns bool corresponding to whether given node is in explored set
                pass #print("explored", n.currPuzzleLayout, "f(n) =", n.gn+n.hn, "with a g(n) =", n.gn, "and a h(n) =", n.hn, "and a queue size of", len(frontier.queue))
                pass #print("new node is already in explored. do nothing")
            elif n in frontier_set:                              #returns bool corresponding to whether given node is in explored set
                if (nodewithmingn.gn) > (n.gn):    #lower cost   (does not need hn)
                    #print("before", n.currPuzzleLayout, "f(n) =", n.gn+n.hn, "with a g(n) =", n.gn, "and a h(n) =", n.hn, "and a queue size of", len(frontier.queue))
                    n.update(nodewithmingn, n.gn)       #updates node object with  given g(n) value (which should update frontier)
                    #print("after", n.currPuzzleLayout, "f(n) =", n.gn+n.hn, "with a g(n) =", n.gn, "and a h(n) =", n.hn, "and a queue size of", len(frontier.queue))
                    frontier.update()
                    pass #print("updated value of f(n)", n.currPuzzleLayout, "in frontier")
                else:
                    pass #print("new node has higher cost than existing node. do nothing")
            else:
                frontier.push(n)
                frontier_set.add(n)
                #print("pushed in frontier", n.currPuzzleLayout, "f(n) =", n.gn+n.hn, "with a g(n) =", n.gn, "and a h(n) =", n.hn, "and a queue size of", len(frontier.queue))
                pass #print("pushed", n.currPuzzleLayout, "to frontier")
                #print("frontier.queue[0] =", frontier.queue)
        #print("\n")

        #print("explored =", explored) 
        explored.add(nodewithmingn)                             #add the node to the explored set
