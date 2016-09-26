"""
Name: Rahul Patil

"""
import sys, operator
import argparse
from Queue import *

#Code for implementing priority queue
class PriorityQueue(object):
    def __init__(self):
        self.vlist = []
    #Adds elements to the min heap
    def addElements(self,vertices_list):
        for key,value in vertices_list.items():
            if value.upStatusFlag == True:
                self.heapInsert(value)
    #Inserts elements into the heap at appropriate location            
    def heapInsert(self,value):
        self.vlist.append(value)
        self.downHeapify(0, len(self.vlist)-1)
        
    #Restores the min-heap property from the root down.
    def downHeapify(self, start, end):
        newelement = self.vlist[end]
        while end  > start:
            index = (end-1)/ 2
            parent = self.vlist[index]
            if newelement < parent:
                self.vlist[end] = parent
                end = index
                continue
            break
        self.vlist[end] = newelement
    #Pops the minimum item from the heap    
    def extractMin(self):
        lastelement = self.vlist.pop()    
        if self.vlist:
            returnitem = self.vlist[0]
            self.vlist[0] = lastelement
            self.upHeapify(0)
        else:
            returnitem = lastelement
        return returnitem
    
    #Finds the vertex in the heap and moves it up to place in appropriate position
    def decKey(self,vertexValue):
        vert_index = self.vlist.index(vertexValue)
        while vert_index >0 and self.vlist[(vert_index-1)/2]> self.vlist[vert_index]:
            temp = self.vlist[vert_index]
            self.vlist[vert_index] = self.vlist[(vert_index-1)/2]
            self.vlist[(vert_index-1)/2] = temp
            vert_index= (vert_index-1)/2
    #Restores min heap property from the leaf up.
    def upHeapify(self, location):
        end = len(self.vlist)
        start = location
        newitem = self.vlist[location]
        # Move the smaller child up until reaching a leaf.
        child = 2*location + 1    
        while child < end:
            # Set child to index of smaller child.
            right = child + 1
            if right < end and not self.vlist[child] < self.vlist[right]:
                child = right
            # Move up the smaller child.
            self.vlist[location] = self.vlist[child]
            location = child
            child = 2*location + 1
        self.vlist[location] = newitem
        self.downHeapify(start, location)

#Vertex Class holds all the information about the vertices of the graph
class Vertex(object):
    def __init__(self,name,upStatusFlag):
        self.name = name
        self.upStatusFlag = upStatusFlag
        self.predecessor = None
        self.transmit_time = float('inf')
    #Functions that are called while using comparision operations.
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return (self.transmit_time) == (other.transmit_time)
    def __lt__(self, other):
        return (self.transmit_time) < (other.transmit_time)
    def __le__(self, other):
        return (self.transmit_time) <= (other.transmit_time)
    def __ge__(self, other):
        return (self.transmit_time) >= (other.transmit_time)
    def __gt__(self, other):
        return (self.transmit_time) > (other.transmit_time)
    def __ne__(self, other):
        return (self.transmit_time) != (other.transmit_time)

#Edge class holds all the information about the edges of the graph
class Edge(object):
    def __init__(self,srcVertex,destVertex,transmit_time,upStatusFlag):
        self.srcVertex = srcVertex
        self.destVertex = destVertex
        self.transmit_time = float(transmit_time)
        self.upStatusFlag = upStatusFlag
    def __hash__(self):
        return hash((self.srcVertex,self.destVertex))
    def __eq__(self, other):
        return (self.srcVertex,self.destVertex,self.transmit_time,self.upStatusFlag) == (other.srcVertex,other.destVertex,other.transmit_time,other.upStatusFlag)
    
#The graph class holds the adjacency list and hence the information about the edges and vertices
class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        self.adjList = {}
        
    #Adds a new Vertex to the graph
    def addvertex(self,name_vertex,vertex):
        self.vertices[name_vertex] = vertex
        
    #Adds a new Edge to the graph
    def addEdge(self,edgeKey,Edge):
        self.edges[edgeKey] = Edge

    #Checks and updates Edges if not already present
    def addUpdateEdge(self,headV,tailV,transmit_time):
        if not self.vertices.has_key(headV):
            self.addvertex(headV,Vertex(headV,True))
        if not self.vertices.has_key(tailV):
            self.addvertex(tailV,Vertex(tailV,True))
        if self.edges.has_key((headV,tailV)):
            self.edges[(headV,tailV)].transmit_time = float(transmit_time)
        else:
            self.addEdge((headV,tailV),Edge(headV,tailV,transmit_time,True))
            self.addAdjVertices(headV,tailV)
            self.addAdjVertices(tailV,None)

    #Updating the Adjacency List
    def addAdjVertices(self,v1,v2):
        if not v2 == None:
            self.adjList.setdefault(v1,[]).append(v2)
        else:
            self.adjList.setdefault(v1,[])


    #Marks an existing edge as DOWN
    def edgeDown(self,headV,tailV):
        self.edges[(headV,tailV)].upStatusFlag = False

    #Marks an existing edge as UP
    def edgeUp(self,headV,tailV):
        self.edges[(headV,tailV)].upStatusFlag = True



    #Marks an existing Vertex as DOWN
    def vertexDown(self,vertex):
        self.vertices[vertex].upStatusFlag = False

    #Marks an existing Vertex as UP
    def vertexUp(self,vertex):
        self.vertices[vertex].upStatusFlag = True

    
    #Delete an exisitng edge and update the Adjacency List        
    def deleteEdge(self,v1,v2):
        del self.edges[(v1,v2)]
        self.adjList[v1].remove(v2)

    #Print the graph in the correct order
    def printGraph(self):
        for vertices in (sorted(self.vertices.keys())):
            print (self.vertices[vertices].name), "DOWN" if (self.vertices[vertices].upStatusFlag == False) else ""
            for adj_vertices in sorted(self.adjList[vertices]):
              print " ", adj_vertices,self.edges[(vertices,adj_vertices)].transmit_time, "DOWN" if (self.edges[(vertices,adj_vertices)].upStatusFlag == False) else ""

 
            
    #Computes the shortest path from the source to destination
    def path(self,source,destination):
        #Using the priority Queue
        pq = PriorityQueue()
        for vertex in self.vertices.keys():
            self.vertices[vertex].predecessor = None
            self.vertices[vertex].transmit_time = float('inf')
        self.vertices[source].transmit_time = 0.0
        dist = []
        distSoFar = {key: val for key,val in self.vertices.items() if val.upStatusFlag == True}
        pq.addElements(distSoFar)
        while pq.vlist:
            u = pq.extractMin()
            for v in self.adjList[u.name]:
                if self.vertices[v].upStatusFlag == True and self.edges[(u.name,v)].upStatusFlag == True:
                    if self.vertices[v].transmit_time > (self.vertices[u.name].transmit_time + self.edges[(u.name,v)].transmit_time) :
                        self.vertices[v].transmit_time = self.vertices[u.name].transmit_time + self.edges[(u.name,v)].transmit_time
                        self.vertices[v].predecessor = u
                        pq.decKey(self.vertices[v])
        node = self.vertices[destination]
        while node.predecessor is not None:   #Display the vertices in the correct order
            dist.append(node.name)
            node = node.predecessor
        dist.append(node.name)
        dist.reverse()
        print " ".join([str(vert) for vert in dist]),self.vertices[destination].transmit_time
    

    #Print the printReachable vertices using BFS   
    def printReachable(self):
        for vertex in (sorted(self.vertices.keys())):
            if self.vertices[vertex].upStatusFlag == True:
                self.calcReachable(vertex)



    #Calculates the printReachable vertices from the given vertex using graph coloring    
    def calcReachable(self,vertex):
        colored_vertices = {}
        printReachable = {}
        distSoFar = {key: val for key,val in self.vertices.items() if (key != vertex and val.upStatusFlag == True)}
        for rvertex in self.vertices.keys():
            colored_vertices[rvertex] = "white"
        colored_vertices[vertex] = "gray"
        q = Queue()
        q.put(vertex)
        while not q.empty():
            u = q.get()
            for v in sorted(self.adjList[u]):
                if colored_vertices[v] == "white" and self.vertices[v].upStatusFlag == True and self.edges[(u,v)].upStatusFlag == True:
                    colored_vertices[v] == "gray"
                    q.put(v)
                    printReachable[v] =v
            colored_vertices[u] = "black"
        print vertex
        for vlist in sorted(printReachable.keys()):
            print " ", vlist

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Filename containing the graph")
    args = parser.parse_args()

    filename = args.filename
    
    #Creating a graph
    graph = Graph()
    #Read the contents of input file
    with open(filename,'r') as f:
        for line in f:
            v1 = Vertex(line.split()[0],True)
            v2 = Vertex(line.split()[1],True)
            #Add the vertices and edges to the graph
            graph.addvertex(v1.name,v1)
            graph.addvertex(v2.name,v2)
            edge1 = Edge(line.split()[0],line.split()[1],line.split()[2],True)
            edge2 = Edge(line.split()[1],line.split()[0],line.split()[2],True)
            graph.addEdge((v1.name,v2.name),edge1)
            graph.addEdge((v2.name,v1.name),edge2)
            graph.addAdjVertices(v1.name,v2.name)
            graph.addAdjVertices(v2.name,v1.name)
            #print graph

    while True:
        line = sys.stdin.readline()
        if line.strip():
            input_query = line.split()
            if input_query[0] == "addedge":
                graph.addUpdateEdge(input_query[1],input_query[2],input_query[3])

            elif input_query[0] == "deleteedge":
                graph.deleteEdge(input_query[1],input_query[2])

            elif input_query[0] == "edgedown":
                graph.edgeDown(input_query[1],input_query[2])

            elif input_query[0] == "edgeup":
                graph.edgeUp(input_query[1],input_query[2])

            elif input_query[0] == "vertexdown":
                graph.vertexDown(input_query[1])

            elif input_query[0] == "vertexup":
                graph.vertexUp(input_query[1])

            elif input_query[0] == "print":
                graph.printGraph()

            elif input_query[0] == "reachable":
                graph.printReachable()

            elif input_query[0] == "path":
                graph.path(input_query[1],input_query[2])

if __name__ == '__main__':
    main()
