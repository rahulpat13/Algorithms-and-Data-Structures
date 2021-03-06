Name: Rahul Patil

Programming Language used: Python 2.7.6
Compiler version: GCC 4.8.2

Program Description: Dijkstra's Shortest Path Algorithm using min-heap priority queue
The program takes the scriptname and the text file containing the graph information to calculate
the shortest path between any two vertices and also provides the option to make changes to the 
graph using queries that can be entered at the prompt after the program script is run.
The Vertex class and Edge Class hold the vertex and edge information of the graph.
The Graph Class builds a graph out of this information using an adjacency list.
The PriorityQueue Class holds the information about the min-heap data structure.


Algorithm to compute the Reachable Vertices:
Uses the Breadth first search algoithm to print the reachable vertices. Running time of this is O(V+E) for each vertex/EDGE that is UP.          
Worst Case Running time for overall graph is O(V*(V + E)) assuming all Vertices and Edges are UP since the loop runs for each vertex.
Implemented as the function calcReachable.

Data Structure Design:
The priority queue is implemented in the form of a min-heap for improved efficiency. 
The min-heap is used to store the distances of the vertices from the source vertex and help 
to extract the closest vertex very fast.

Input Queries:
1. addedge tailvertex headvertex transmit_time 
		Adds an Edge from the tailvertex to headvertex with the weight as transmit_time.

2. deleteedge tailvertex headvertex
		Deletes the edge specified by the tailvertex and headvertex.

3. edgedown tailvertex headvertex
		Marks the edge from tailvertex to headvertex as DOWN.

4. edgeup tailvertex headvertex
		Marks the edge from tailvertex to headvertex as UP.

5. vertexdown vertex
		Marks the specified vertex as DOWN

6. vertexup vertex
		Marks the specified vertex as UP.

7. path from_vertex to_vertex
		Calculates the shortest path from the source to destination using Dijkstra's shortest path algorithm.

8. print
		Prints the graph contents vertex by vertex in alphabetical order.

9. reachable
		Prints the reachable vertices from the current in alphabetical order.

To run the program:
1. Navigate to the directory containing the inputs and the scripts.
2. At the command prompt enter:
	$python graph.py <filename.txt>
3.After which there will be a blinking cursor where the queries can be entered to edit and print the graph.
