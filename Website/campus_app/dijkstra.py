from graph import graph, node_coordinates

# ===== Implement path finding algorithm here =====

class Graph():
 
    def __init__(self, nodeCount):
        # Initialize graph with node count
        self.nodeCount = nodeCount
        
        # Create an index map and adjacency matrix
        self.nodeIndices = {}
        self.graph = []
        
        # Populate adjacency matrix (size nodeCount x nodeCount)
        for i in range(nodeCount):
            row = [0] * nodeCount
            self.graph.append(row)
 
    # Find unvisited node with smallest distance
    def minDistance(self, minDistances, nodesVisited):
        # Set initial minimum distance to inf, min node to none
        min = float('inf')
        minIndex = -1

        # Iterate though all nodes, select unvisited node with smallest distance
        for node in range(self.nodeCount):
            if minDistances[node] < min and not nodesVisited[node]:
                min = minDistances[node]
                minIndex = node

        return minIndex
 
    def dijkstra(self, startNode, endNode):
        # Return list starting and ending in same location
        if startNode == endNode:
            reverseMap = {}
            for node, index in self.nodeIndices.items():
                reverseMap[index] = node
                
            return self.convertToCoordinates([reverseMap[startNode], reverseMap[endNode]])
        
        # Initialize array with infinity for all nodes
        minDistances = [float('inf')] * self.nodeCount
        minDistances[startNode] = 0
        
        nodesVisited = [False] * self.nodeCount
        predecessors = [-1] * self.nodeCount

        # Dijkstra's main loop
        for _ in range(self.nodeCount):
            # Get node with smallest distance, mark as visited
            currentNode = self.minDistance(minDistances, nodesVisited)
            nodesVisited[currentNode] = True

            # Update shortest distances for neighboring nodes
            for neighbor in range(self.nodeCount):
                # Checck for unvisited edge, and undiscovered shortest path
                if (self.graph[currentNode][neighbor] > 0 and not nodesVisited[neighbor] 
                        and minDistances[neighbor] > minDistances[currentNode] + self.graph[currentNode][neighbor]):
                    # Update neighbors shortest distance
                    minDistances[neighbor] = minDistances[currentNode] + self.graph[currentNode][neighbor]
                    # Set current node as neighbors predecessor
                    predecessors[neighbor] = currentNode
                    
        # Reconstruct path from endNode to startNode
        path = []
        current = endNode
        while current  != -1 and predecessors[current] != -1:
            path.insert(0, current)
            current = predecessors[current]
            
        # Insert original node
        if path[0] != startNode:
            path.insert(0,startNode)
        
        # Reverse map to correct order
        reverseMap = {}
        for node, index in self.nodeIndices.items():
            reverseMap[index] = node
            
        # Convert path of node names to node coordinates for api
        node_path = [reverseMap[node] for node in path]
        path_coords = self.convertToCoordinates(node_path)
        
        return path_coords
 
    def addEdge(self, startNode, endNode, edgeWeight):
        if startNode in self.nodeIndices and endNode in self.nodeIndices:
            # Get indices of start and end node
            startIndex = self.nodeIndices[startNode]
            endIndex = self.nodeIndices[endNode]
            
            # set weight for both directions
            self.graph[startIndex][endIndex] = edgeWeight
            self.graph[endIndex][startIndex] = edgeWeight  # For undirected graph

    def setupGraph(self, graph):
        # self.nodeIndices = {node: index for index, node in enumerate(graph.keys())}
        self.nodeIndices = {}
        for index, node in enumerate(graph.keys()):
            self.nodeIndices[node] = index
        
        # Get number of nodes in graph
        self.nodeCount = len(self.nodeIndices)

        # Populate matrix with edge weights
        for node, edges in graph.items():
            for edge in edges:
                if edge['weight'] is not None:  # Ensure weight is not NULL
                    self.addEdge(node, edge['to'], edge['weight'])
    
    # Convert a list of node names to a list of their coordinates
    def convertToCoordinates(self, nodeNames):
        coordinateList = []
        
        # Iterate through the nodeNames list to preserve the order
        for node in nodeNames:
            if node in node_coordinates:
                coordinateList.append(node_coordinates[node])
        return coordinateList


# ===== Debugging: Test Dijkstra algorithm for correctness =====
# g = Graph(len(graph))
# g.setupGraph(graph)

# # # Case 1
# # startNode = 'cob2'
# # endNode = 'acs'

# # # Case 2
# startNode = "acs"
# endNode = "acs"

# startIndex = g.nodeIndices[startNode]
# endIndex = g.nodeIndices[endNode]

# pathCoords = g.dijkstra(startIndex, endIndex)

# print("Shortest path: ", pathCoords)

# ===== Debugging: Print all graph nodes and their connections =====
# for node in graph:
#     for edge in graph[node]:
#         print(f"Node {node} connects to {edge['to']} through {edge['pathName']} with a distance of {edge['weight']}")
