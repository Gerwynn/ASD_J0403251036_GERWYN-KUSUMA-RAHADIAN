#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

# Fungsi untuk membuat Adjacency List
def createAdjList(nodes, edges):
    adj = {node: [] for node in nodes}

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # since the graph is undirected
        adj[v].append(u)
        
    return adj

# Fungsi untuk membuat Adjacency Matrix
def createAdjMatrix(nodes, edges):
    V = len(nodes)
    mat = [[0 for _ in range(V)] for _ in range(V)]

    # Add each edge to the adjacency matrix
    for it in edges:
        # Mengubah string nama kota menjadi angka indeks
        u_idx = nodes.index(it[0])
        v_idx = nodes.index(it[1])
        
        mat[u_idx][v_idx] = 1

        # since the graph is undirected
        mat[v_idx][u_idx] = 1
        
    return mat

if __name__ == "__main__":
    # 1. vertex
    nodes = ["Semarang", "Solo", "Magelang", "Pekalongan", "Cilacap"]
    
    # 2. edge
    edges = [
        ("Semarang", "Pekalongan"), 
        ("Semarang", "Solo"), 
        ("Semarang", "Magelang"), 
        ("Solo", "Magelang"), 
        ("Solo", "Cilacap"), 
        ("Magelang", "Cilacap")
    ]

    # Build the graph using edges
    adj_list = createAdjList(nodes, edges)
    adj_matrix = createAdjMatrix(nodes, edges)

    # --- OUTPUT PROGRAM ---
    print("1. Nama Node")
    print(nodes)

    print("\n2. Relasi Antar Node (Edges)")
    for it in edges:
        print(f"{it[0]} <---> {it[1]}")

    print("\nAdjacency List Representation:")
    for i in nodes:
        # Print the vertex
        print(f"{i}:", end=" ")
        
        for j in adj_list[i]:
            # Print its adjacent
            print(j, end=" ")
        print()

    print("\nAdjacency Matrix Representation:")
    V = len(nodes)
    for i in range(V):
        for j in range(V):
            print(adj_matrix[i][j], end=" ")
        print()