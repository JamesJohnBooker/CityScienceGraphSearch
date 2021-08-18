# CityScienceGraphSearch
This script performs Dijkstra's algorithm to find the shortest path from one node to another node in a graph. Information on Dijkstra's algorithm, including an outline of the algorithm itself, can be found below:

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

To run the code for testing purposes, do the following:
1) Download the CityScienceGraphSearch.py file in this repository and store it on your Desktop.
2) Create a file, such as a .dat or .txt file, listing nodes and edges on a graph, as described in the City Science programming task brief (i.e. each line should follow the format '<startNode> <endNode> <distance>') and store it on your Desktop as well
3) Open the command prompt.
5) In the command line, type 'cd Desktop'
6) In the command line, type 'python CityScienceGraphSearch.py <file-name>.<file-extension> <startNode> <endNode>' and press enter (here, <file-name> is the name of your graph file, <file-extension> is the file extension for the file type you used, e.g. .dat or .txt, <startNode> is the first node in the path you want and <endNode> is the target node in the path you want).
This will return either the shortest path from your specified start node to your specified end node if any such paths exist, and a text.

In my testing so far the code has worked well on the exmouth-links.dat file included in the City Science programmind task brief, as well as the various .txt files included in this repository.
