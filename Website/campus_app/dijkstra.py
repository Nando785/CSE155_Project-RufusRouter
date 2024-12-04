from graph import graph, node_coordinates

# ===== Implement path finding algorithm here =====

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.vertex_map = {}
        self.edge_map = {}
 
    def minDistance(self, dist, sptSet):
        min = float('inf')
        min_index = -1

        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index
 
    def dijkstra(self, start, end):
        dist = [float('inf')] * self.V
        dist[start] = 0
        sptSet = [False] * self.V
        predecessors = [-1] * self.V
        path_nodes = [None] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    predecessors[v] = u
                    path_nodes[v] = u
                    
        path = []
        current = end
        while current  != -1 and predecessors[current] != -1:
            path.insert(0, current)
            current = predecessors[current]
            
        # Insert original node
        if path[0] != start:
            path.insert(0,start)
            
        reverse_map = {v: k for k, v in self.vertex_map.items()}
        node_path = [reverse_map[node] for node in path]
        # return node_path
        path_coords = self.get_node_coordinates(node_path)
        return path_coords
 
    def add_edge(self, from_vertex, to_vertex, weight, path_name):
        if from_vertex in self.vertex_map and to_vertex in self.vertex_map:
            u = self.vertex_map[from_vertex]
            v = self.vertex_map[to_vertex]
            self.graph[u][v] = weight
            self.graph[v][u] = weight  # For undirected graph
            self.edge_map[(u, v)] = path_name
            self.edge_map[(v, u)] = path_name  # Both directions

    def setup_graph(self, graph):
        self.vertex_map = {node: index for index, node in enumerate(graph.keys())}
        self.V = len(self.vertex_map)
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

        for node, edges in graph.items():
            for edge in edges:
                if edge['weight'] is not None:  # Ensure weight is not NULL
                    self.add_edge(node, edge['to'], edge['weight'], edge['pathName'])
    
    def get_path_names(self, path):
        reverse_map = {v: k for k, v in self.vertex_map.items()}
        return [reverse_map[node] for node in path]
    
    def get_node_coordinates(self, nodeNames):
        coordinateList = []
        for node in node_coordinates:
            if node in nodeNames:
                coordinateList.append(node_coordinates[node])
        return coordinateList

# ===== Debugging: Test Dijkstra algorithm for correctness =====
# g = Graph(len(graph))
# g.setup_graph(graph)

# startNode = 'ssb'
# endNode = 'cob2'

# startIndex = g.vertex_map[startNode]
# endIndex = g.vertex_map[endNode]

# pathCoords = g.dijkstra(startIndex, endIndex)

# print("Shortest path: ", pathCoords)

# ===== Debugging: Print all graph nodes and their connections =====
# for node in graph:
#     for edge in graph[node]:
#         print(f"Node {node} connects to {edge['to']} through {edge['pathName']} with a distance of {edge['weight']}")
