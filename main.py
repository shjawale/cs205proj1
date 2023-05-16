#import os
import node, AstarF, math, problem

#def include(filename):
#    if os.path.exists(filename): 
#        execfile(filename)

global_recesses = list()
length = 0
mapofPuzzle = dict()
    
def findRecesses(puzzleLayout):
    global global_recesses
    global_recesses.clear()
    for i in range(len(puzzleLayout[0])):
        #print(puzzleLayout[0], i)
        if puzzleLayout[0][i] == 0:
            global_recesses.append(i)
    print("find recesses =", global_recesses)
    return global_recesses

def estcostuniform(nodeLayout, probLayout):
    return 0

def estcostTotManhattan(nodeLayout, probLayout): #probLayout is a list
    diffcr = 100
    result = 0
    pc = 0
    #print("probLayout =", probLayout)
    print("in manhattan nodeLayout =", nodeLayout)
   
    #print("mapofpuzzle =", mapofPuzzle)
    
    for k in range(1,10):       #k represents the actual value 1 to 9
        for c in global_recesses:
            if nodeLayout[0][c] == k:
                pc = mapofPuzzle[k]       #find location of each soldier
                diffcr = abs(c - pc) + 1
                break

        for c in range(len(probLayout[0])):
            if nodeLayout[1][c] == k:
                pc = mapofPuzzle[k]     #find location of 1 (1,c)
                diffcr = abs(c - pc) 
                break

        result += diffcr

    print("result =", result)
    return math.floor(result) #diff should be less than 8

def estcostmanhattan(nodeLayout, probLayout): #probLayout is a list
    diffcr = 100
    diffc = 100
    result = 0
    pc = 0
    #print("probLayout =", probLayout)
    print("in manhattan nodeLayout =", nodeLayout)
   
    #n = node.Node(None, 0, nodeLayout)
    #rec = n.findRecesses()


    for c in global_recesses:
        if nodeLayout[0][c] == 1:
            #pc = mapofPuzzle[nodeLayout[0][c]]       #find location of each soldier
            pc = 0
            diffcr = abs(c - pc) + 1
            #print("diffcr =", diffcr, "looking for", nodeLayout[0][c], "which should be in the trench at", pc, "but is in a recess at", c)
            break

    #print("  in rec diffc =", diffc)
    #print("mapofpuzzle =", mapofPuzzle)
    for c in range(len(probLayout[0])):
        if nodeLayout[1][c] == 1:
            #pc = mapofPuzzle[nodeLayout[1][c]]     #find location of 1 (1,c)
            pc = 0
            #print("h(n) =",c-pc)
            diffc = abs(c - pc) 
            break
        '''
        if nodeLayout[1][c] == 0:
            continue
        pc = mapofPuzzle[nodeLayout[1][c]]      #find location of each soldier
        #print("h(n) =", c - pc)
        diffc = c - pc 
        print("diffc =", diffc, "looking for", nodeLayout[1][c], "which should be in the trench at", pc, "but is in the trench at", c)
        result += diffc
        '''
    #print("  not in rec diffc =", diffc)
    if diffc == 100:
        result = diffcr
    elif diffcr == 100:
        result = diffc
    else:
        assert False

    print("result =", result)
    return math.floor(result) #diff should be less than 8

def main():
    print("Welcome to sjawa006 9 Men in a Trench solver.\nUsing a default puzzle...")
    puzzle = list()   #[[],[],[]]
    
    #puzzle = [[-1, -1, 0, 0, -1], [0, 2, 3, 4, 1]]
    #puzzle = [[-1,0,-1], [0,2,1]]
    puzzle = [[-1, -1, -1, 0, -1, 0, -1, 0, -1, -1], [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]]
    #puzzle = [[1, 2, 3], [4, 5, 0], [6, 7, 8]] 
    #print("There are no default puzzles.") #pick an existing puzzle
    
    global length
    global mapofPuzzle

    prob = problem.Problem(puzzle) # check type of everything involved with Problem
    rec = findRecesses(puzzle)
    length = len(puzzle[0])

    node.Node.global_recesses = rec
    node.Node.length = length

    probLayout = prob.goal_state.currPuzzleLayout
    for c in range(len(probLayout[0])):
        mapofPuzzle.update({probLayout[1][c] : (c)})
    node.Node.mapofPuzzle = mapofPuzzle

    print("\nEnter your choice of algorithm\nUniform Cost Search\nA* with the Misplace Tile heuristic\nA* with the Euclidean distance heuristic\n")
    algotype = input() #input
    if algotype == '1':
        ucs = AstarF.Astar(prob, estcostuniform)
        print("reached main from uniformcost", ucs)
    elif algotype == '2':
        Am = AstarF.Astar(prob, estcostmisplaced)
        print("reached main from Amisplaced", Am)
    elif algotype == '3':
        Ae = AstarF.Astar(prob, estcosteuclidean)
        print("reached main from Aeuclid", Ae)
    elif algotype == '4':
        man = AstarF.Astar(prob, estcostTotManhattan) #estcostmanhattan)
        print("reached main from Amanhattan", man)
    else:
        print("Invalid number. Reminder, valid algorithm numbers are '1', '2', or '3'.")
    return


if __name__ == "__main__":
    main()
