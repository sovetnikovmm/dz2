import graphviz

with open("list_of_edges164.txt", 'r') as file:
    graph = graphviz.Graph()
    edges = []
    for line in file:
        vertices = line.split()
        if len(vertices) == 2:
            graph.edge(vertices[0],vertices[1])
            edges.append(vertices)
        elif len(vertices) == 1:
            graph.node(vertices[0])
            edges.append(vertices)
        else:
            print("Invalid input")
            break
    print(edges)
graph.view()
