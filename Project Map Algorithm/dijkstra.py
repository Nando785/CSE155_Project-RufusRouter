from graph import graph

# INPUT: 
#   1) Source node/ position of user
#   2) School map from graph

# EX: Starting from SRE, find path to {COB2, Library, ACS}


# Potential Issues:
#   1) May need to recalculate path after a new node has been visited
#       - Remove source and previously visited nodes from list


# MAP CLARIFICATION NEEDED:
# Determine if algorithm returns a single shortest path to all provided nodes
#   = or =
# Determine which node in designated list is closest and provide user with path to node


# ===== Implement path finding algorithm here =====



# ===== Debugging: Print all graph nodes and their connections =====
for node in graph:
    for edge in graph[node]:
        print(f"Node {node} connects to {edge['to']} through {edge['name']} with a distance of {edge['weight']}")