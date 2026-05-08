#=======================================================================================
# Nama    : Gerwyn Kusuma Rahadian
# NIM     : J0403251036
# Kelas   : A1
#=======================================================================================

"""
1. nodes = ['A', 'B', 'C', 'D']
2. edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
"""
"""
1. Jenis graph tersebut adalah undirected graph, karena tidak terdapat panah yang menunjukkan arah pada edge-nya.
2. Graph tersebut memiliki 4 node (A, B, C, D) dan 4 edge yang menghubungkan node-node tersebut.
3. Node A terhubung dengan B dan C
4. Node B terhubung dengan A dan D
5. Node C terhubung dengan A dan D
6. Node D terhubung dengan B dan C
"""

def createGraph(nodes, edges):
    # Menggunakan dictionary comprehension untuk inisialisasi list kosong pada tiap node (huruf)
    adj = {node: [] for node in nodes}

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # since the graph is undirected
        adj[v].append(u)
        
    return adj

if __name__ == "__main__":
    # Daftar node menggunakan huruf
    nodes = ['A', 'B', 'C', 'D']

    # List of edges (u, v)
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]

    # Build the graph using edges
    adj = createGraph(nodes, edges)

    print("Adjacency List Representation:")
    for i in nodes:
        
        # Print the vertex
        print(f"{i}:", end=" ")
        
        for j in adj[i]:
            # Print its adjacent
            print(j, end=" ")
        print()