from graph import graph
import math

# INPUT: 
#   1) Source node/ position of user
#   2) School map from graph

# EX: Starting from SRE, find path to {COB2, Library, ACS}


# Potential Issues:
#   1) May need to recalculate path after a new node has been visited
#       - Remove source and previously visited nodes from list


# ===== Implement path finding algorithm here =====

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.vertex_map = {}
 
    def printSolution(self, dist, vertex_names):
        print("Vertex \t Distance from Source")
        for i in range(self.V):
            print(vertex_names[i], "\t\t", dist[i])
 
    def minDistance(self, dist, sptSet):
        min = float('inf')
        min_index = -1

        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index
 
    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and not sptSet[v] and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist, list(self.vertex_map.keys()))
 
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex in self.vertex_map and to_vertex in self.vertex_map:
            u = self.vertex_map[from_vertex]
            v = self.vertex_map[to_vertex]
            self.graph[u][v] = weight
            self.graph[v][u] = weight  # For undirected graph

    def setup_graph(self, graph):
        self.vertex_map = {node: index for index, node in enumerate(graph.keys())}
        self.V = len(self.vertex_map)
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

        for node, edges in graph.items():
            for edge in edges:
                if edge['weight'] is not None:  # Ensure weight is not NULL
                    self.add_edge(node, edge['to'], edge['weight'])

# Driver program
g = Graph(len(graph))
g.setup_graph(graph)
g.dijkstra(g.vertex_map['SRE'])


# ===== Debugging: Print all graph nodes and their connections =====
# for node in graph:
#     for edge in graph[node]:
#         print(f"Node {node} connects to {edge['to']} through {edge['pathName']} with a distance of {edge['weight']}")