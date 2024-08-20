def creategraph():
    n=int(input("Enter the no.of nodes : "))
    graph={}
    for i in range(n):
        node=input(f"Enter key for node{i+1}: ").strip()
        adj=input(f"Enter adjacent nodes to the node{node}:").strip().split();
        graph[node]=adj;
    return graph
def get_adjnodes(graph):
    node=input("Enter node to get adjacent nodes: ").strip()
    if node in graph:
        print(f"Adjacent nodes to node{node}:{graph[node]}")
    else:
        print(f"Node{node}isn't found in the graph.")
if __name__=="__main__":
    graph=creategraph()
    print("Graph: ",graph)
    get_adjnodes(graph)

