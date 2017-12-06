import collections
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = collections.defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

mygraph = Graph()
arr = [int(j) for j in raw_input().split()]
for i in range(1,arr[0]+1):
    mygraph.add_node(i)
chocaltecity = [int(j) for j in raw_input().split()]

for i in range(arr[1]):
    values = [int(j) for j in raw_input().split()] 
    mygraph.add_edge(values[0],values[1],values[2])   

cities = [int(j) for j in raw_input().split()] 
friendcitytochoclatecity = []
ourtochocolatecity       = []
for i in range(0,arr[2]):
    friendcitytochoclatecity.append() 

