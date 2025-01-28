#for draw graph
import networkx as nx
#to display graph
import matplotlib.pyplot as plt

#...............create.graph.(create.with.adjacency.matrixe).......................................................................

class graph:
    #strutore method
    def __init__(self, n):
        self.parent = list(range(n))                                #create list for each node
        self.order = [0] * n                                        #define name for each node (start as 0)

    #path optimazation and compression
    def find(self, u):
        if self.parent[u] != u:                                     #parent check
            self.parent[u] = self.find(self.parent[u])              #find parent root
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)                                       #merge tow collection
        root_v = self.find(v)                                       #merge tow collection
        if root_u != root_v:
            if self.order[root_u] > self.order[root_v]:             #concting tow colection by value
                self.parent[root_v] = root_u
            elif self.order[root_u] < self.order[root_v]:
                self.parent[root_u] = root_v
            else:                                                   #if tow root equal together add a unit to one of the nodees
                self.parent[root_v] = root_u
                self.order[root_u] += 1

#.............kuskal.algorithm.....................................................................................................

def kruskal(n, adjacency_matrix):
    edges = []                                                      #create list for save edge
    for i in range(n):                                              #add weighted edges of a graph from adjacency matrix (class graph)
        for j in range(i + 1, n):
            if adjacency_matrix[i][j] != 0:
                edges.append((i, j, adjacency_matrix[i][j]))

    edges.sort(key=lambda x: x[2])                                  #sorting edges by weight
    disjoint_set = graph(n)
    minimum_spanning_tree = []                                      #list to store the edges of the minimum spanning tree.
    total_weight = 0                                                #store all of weight of node

    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):            #add nodes to Minimum Spanning Tree
            disjoint_set.union(u, v)
            minimum_spanning_tree.append((u, v, weight))
            total_weight += weight

    return minimum_spanning_tree, total_weight                      #return node of Minimum Spanning Tree and weight of node

#....................draw graph for dispaly a graphicy garph.......................................................................

def draw_graph(n, adjacency_matrix, minimum_spanning_tree):
    G = nx.Graph()                                                  #create empty graph

    for i in range(n):                                              #add edges to graph
        for j in range(i + 1, n):
            if adjacency_matrix[i][j] != 0:
                G.add_edge(i, j, weight=adjacency_matrix[i][j])

    pos = nx.spring_layout(G)                                       #define position of each node

    #draw all edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    #draw all edges of Minimum Spanning Tree
    minimum_spanning_tree_edges = [(u, v) for u, v, _ in minimum_spanning_tree]
    nx.draw_networkx_edges(G, pos, edgelist=minimum_spanning_tree_edges, edge_color='r', width=2)

    plt.title("Graph and Minimum Spanning Tree (minimum_spanning_tree)")            #dispaly graph in output
    plt.show()

#..........main....................................................................................................................

if __name__ == "__main__":
    n = int(input("enter num of node: "))
    adjacency_matrix = []

    print("enter adjacency matrix data row by row. ")

    for i in range(n):
        row = list(map(float, input(f"enter data for row {i} of the adjacency matrix: ").split()))
        adjacency_matrix.append(row)

    minimum_spanning_tree, total_weight = kruskal(n, adjacency_matrix)

    print("edge of Minimum Spanning Tree: \n")
    for edge in minimum_spanning_tree:
        print(f"{edge[0]} -- {edge[1]} weight {edge[2]}")
    print("\ntotal weigth of Minimum Spanning Tree : ", total_weight)

    draw_graph(n, adjacency_matrix, minimum_spanning_tree)
