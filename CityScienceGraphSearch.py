import sys #Needed to take in inputs from the command line.
fileName = str(sys.argv[len(sys.argv) - 3]) #fileName stores the file name of the file storing data on the graph, as specified in the command line by the user e.g. 'exmouth-links.dat'.
startNode = str(sys.argv[len(sys.argv) - 2]) #startNode stores the initial node in the path, as specified in the command line by the user.
endNode = str(sys.argv[len(sys.argv) - 1]) #endNode stores the target node, as specified in the command line by the user.
if startNode == endNode: #If the start and end nodes are the same, then we have a path of length zero between them and the only node included is the start/end node.
    print(startNode)
else: #If the start and end nodes are different, then the distance between them is calculated using Dijkstra's algorithm.
    file = open(fileName, 'r') #The file holding data on the graph is opened so that a list can be initialised to store the distance to each node.
    distances = [[startNode, 0]] #distances is a list which will store each node that has an edge leading to it, the current best distance to that node, and the preceeding node on the path with this length. distances is also initialised to contain startNode and the distance to this node is 0.
    for line in file: #This for loop iterates through each line in the file storing the graph data.
        lineValues = line.split() #lineValues is initialised to be a list storing the information from the current line in the file. It will have a length of three, and will store one node in index position 0, a second node in index position 1 and the length of the edge from the first node to the second node in index position 2.
        for nodeIndex in range(0, len(distances)): #This for loop iterates through the indexes of each element in distances.
            if distances[nodeIndex][0] == lineValues[1]: #If the node from lineValues that is being mapped to is already listed in distances, then the next line in the graph file is checked.
                break
            elif nodeIndex == len(distances) - 1: #If distances does not currently contain the node from lineValues that is being mapped to, then this node is added to distances.
                distances.append([lineValues[1], -1]) #When a node is added to distances, the distance to this node is initialised to be equal to -1.
    file.close() #All the necessary information from the graph file has been read, so it is closed.
    shortestPathFound = False #shortestPathFound is initialised to be false and remains so until Dijkstra's algorithm determines the shortest path from startNode to endNode.
    currentNodeIndex = 0 #The index of the current node from distances being explored is initialised to be the index of startNode.
    checkedDistances = [] #checkedDistances stores the elements of distances that have been marked as 'visited' by Dijkstra's algorithm (see the Wikipedia page).
    pathExists = True #pathExists is initialised to be true and remains so until it has been confirmed that there is no path from startNode to endNode.
    while shortestPathFound == False: #This while loop runs until Dijkstra's algorithm determines the shortest path from startNode to endNode.
        file = open(fileName, 'r') #The file holding data on the graph is opened so that the edges leading from the node that is currently being explored can be examined.
        for line in file: #This for loop iterates through each line in the file storing the graph data.
            lineValues = line.split() #lineValues initialised to be a list storing the information from the current line in the file. It will have a length of three, and will store a node in index position 0, a second node in index position 1 and the weight of the edge from the first node to the second node in index position 2.
            if lineValues[0] != distances[currentNodeIndex][0]: #If the first node in the line is not the node we are currently exploring, then the next line is considered.
                continue
            else: #If the first node in the line is the node we are currently exploring, then this line details an edge to another node, which we examine.
                for neighbourNodeIndex in range(0, len(distances)): #This for loop iterates through the indexes of the elements of distances.
                    if distances[neighbourNodeIndex][0] == lineValues[1]: #Once the element in distances corresponding to the destination node has been found, the current distance to this node is checked.
                        if distances[neighbourNodeIndex][1] == -1: #If the distance to this node is still -1, then no edge to this node has been considered yet, so distance to this node is set to be the distance from the startNode to the node currently being explored plus the distance from the node currently being explored to this node and the preceeding node in the path is set to be the node currently being explored. 
                            distances[neighbourNodeIndex][1] = distances[currentNodeIndex][1] + int(lineValues[2])
                            distances[neighbourNodeIndex].append(distances[currentNodeIndex][0])
                        elif distances[neighbourNodeIndex][1] > distances[currentNodeIndex][1] + int(lineValues[2]): #If the listed distance to this node is longer than the distance from startNode to the node currently being explored plus the distance from the node currently being explored to this node, then the distance to this node is set to be the distance from the startNode to the node currently being explored plus the distance from the node currently being explored to this node and the preceeding node in the path is set to be the node currently being explored. 
                            distances[neighbourNodeIndex][1] = distances[currentNodeIndex][1] + int(lineValues[2])
                            distances[neighbourNodeIndex][2] = distances[currentNodeIndex][0]
                        else:
                            continue
                    else:
                        continue
        file.close() #All the necessary information from the graph file has been read, so it is closed.
        checkedDistances.append(distances[currentNodeIndex]) #We have checked all the edges leading from the node that is currently being explored, so it has been 'visited' and its corresponding element from distances is added to checkedDistances.
        if distances[currentNodeIndex][0] == endNode: #If the newly visited node is endNode, then we have found the shortest path from startNode to the endNode, so the while loop ends.
            shortestPathFound = True
            break
        else: #If the newly visited node is not endNode, then the next node to be explored is chosen.
            distances.pop(currentNodeIndex) #The element corresponding to the newly visisted node is removed from distances.
            if distances == []: #If every node with an edge leading to it has been explored and no path from startNode to endNode has been found, then no such path exists and so pathExists is set to be false and the while loop ends.
                pathExists = False
                break
            nextNodeIndex = -1 #The index of the next node to be explored is initialised to be -1.
            noNodesToCheck = True #noNodesToCheck is initialised to be true and reamins so unless an element from distances is found which corresponds to a node with a known path of positive length leading to it.
            for nodeIndex in range(0, len(distances)): #The for loop iterates through the indexes of the elements of distances.
                if distances[nodeIndex][1] > 0: #If an element of distances is found which corresponds to a node with a known path of positive length leading to it, the length of this path is checked to see if this will be the next node to be explored.
                    noNodesToCheck = False #There is still a node to explore, so noNodesToCheck is set to false.
                    if nextNodeIndex == -1: #If no node is currently set to be explored, then the node corresponding to nodeIndex is set to be explored next. 
                        nextNodeIndex = nodeIndex
                    elif distances[nodeIndex][1] < distances[nextNodeIndex][1]: #If a node is currently set to be explored, but it is further away from startNode than the node corresponding to nodeIndex, then the next node to be explored will instead be the one corresponding to nodeIndex.
                        nextNodeIndex = nodeIndex
                    else:
                        continue
                else: #If no elements of distances correspond to a node with a known path of positive length leading to it, then no path from startNode to endNode exists and so pathExists is set to false and the for loop ends.
                    if noNodesToCheck == True:
                        if nodeIndex == len(distances) - 1:
                            pathExists = False
                            break
                        else:
                            continue
                    else:
                        continue
            if pathExists == False: #If pathExists is set to false then the while loop ends.
                break
            currentNodeIndex = nextNodeIndex #The index for the node to be explored during the next iteration of the while loop is set to nextNodeIndex.
    if pathExists == False: #If we have confirmed that there is no path from startNode to endNode, then a message confirming this is printed in the command prompt.
        print("There is no path from " + startNode + " to " + endNode + ".")
    else: #If, on the other hand, we have found a path from startNode to endNode (which will be the shortest such path thanks to Dijkstra's algorithm), we will print the nodes in this path in the command prompt.
        shortestPathListed = False #shortestPathListed is initialised to be false and remains so until every node in our shortest path has been added to the list shortestPath.
        shortestPath = [endNode] #shortestPath is initialised to contain endNode.
        currentNodeIndex = len(checkedDistances) - 1 #currentNodeIndex is given the value of the index of endNode in checkedDistances (since this will always be the last node visited before the shortest path from startNode to endNode is found).
        while shortestPathListed == False: #This while loop runs until each of the nodes in the shortest path from startNode to endNode has been added to shortestPath (once the while loop ends, these nodes will be listed in reverse order).
            shortestPath.append(checkedDistances[currentNodeIndex][2]) #The node preceeding the current node in the shortest path from startNode to endNode is added to shortestPath.
            if checkedDistances[currentNodeIndex][2] == startNode: #If the newly added node is startNode, then the set of nodes in the shortest path from startNode to endNode has been fully listed and the while loop ends.
                shortestPathListed = True
                break
            else: #If the newly added node is not startNode, then the index of the next node to be added is found.
                for nodeIndex in range(0, len(checkedDistances)): #This for loop iterates through the indexes of the elements of checkedDistances.
                    if checkedDistances[nodeIndex][0] == checkedDistances[currentNodeIndex][2]: #When the element in checkedDistances corresponding to the node preceeding the newly added node has been found, currentNodeIndex is given the value of that element's index position.
                        currentNodeIndex = nodeIndex
        for nodeIndex in range(0, len(shortestPath)): #The elements of shortestPath are printed to the command prompt in reverse order (that is, from startNode to endNode).
            print(shortestPath[len(shortestPath) - 1 - nodeIndex])
