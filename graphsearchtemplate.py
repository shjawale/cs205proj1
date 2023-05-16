#function GraphSearch(problem) returns a solution, or failure
#   initialize the frontier using the initial state of problem
#   initialize the explored set to be empty
#   LOOP DO:
#       IF the frontier is empty:
#           return failure
#       choose a leaf node and remove it from teh frontier
#       IF the node contains a goal state:
#           return corresponding solution
#       add the node to the explored set
#       IF choosen node is not in the frontier or explored sets:
#           expand the chosen node, adding the resulting node to the frontier

function GraphSearch(problem) returns a solution, or failure
   initialize the frontier using the initial state of problem
   initialize the explored set to be empty
   while (1):
       if the frontier is empty:
           return failure
       choose a leaf node and remove it from teh frontier
       if the node contains a goal state:
           return corresponding solution
       add the node to the explored set
       if choosen node is not in the frontier or explored sets:
           expand the chosen node, adding the resulting node to the frontier
