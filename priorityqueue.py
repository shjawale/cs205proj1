import heapq

class priorityQueue:
    ## overall template for class taken from geeksforgeeks.com
    ## heapq is a module that comes with python
    ## delete(), now popmin() edited to be relevant to the project
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def push(self, currNode): #, g, h):
        #data = g + h
        #self.queue.append(data) #heapq.push(data)
        heapq.heappush(self.queue, currNode)

    # for popping an element based on value of g(n)
    def popmin(self):
        #print("inside popmin: selfqueue =", self.queue[0].currPuzzleLayout)
        return heapq.heappop(self.queue) #somehow make heappop order the queue based on g(n)+h(n) via '<'
    
    def find(self, node): #given a node, find it in the priorityqueue
        return node in self.queue
    #    for i in self.queue:
    #        if i == node:
    #            return True
    #    return False #did not find node in frontier

    def update(self):
        heapq.heapify(self.queue)

#if __name__ == '__main__':
#    myQueue = priorityQueue()
#    myQueue.insert(12)
#    myQueue.insert(1)
#    myQueue.insert(14)
#    myQueue.insert(7)
#    print(myQueue)
#    while not myQueue.isEmpty():
#        print(myQueue.delete())

