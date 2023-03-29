import graphviz

with open("list_of_edges164.txt", 'r') as file:
    edge = file.read().strip()
edges = list(map(lambda x: (x.split()[0], x.split()[1]), edge.split('\n')))

print(edges)

g = graphviz.Graph()

for i in edges:
    g.edge(i[0], i[1])

g.view()