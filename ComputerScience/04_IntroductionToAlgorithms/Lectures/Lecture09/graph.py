def bfs(Adj, s):
    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]
    while 0 < len(level[-1]):
        level.append([])
        for u in  level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)
    print("parent: ", parent)
    print("level: ", level)

def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
        order = []
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    print("parent: ", parent)
    print("oder: ", order)
    return parent, order

class Vertex:
    def __init__(self, index = None, color = None, distance = None, parent =
                 None):
        self.index = index
        self.color = color
        self.distance = distance
        self.parent = Parent
    def __str__(self):
        return f"self.index"

def breadth_first_search(graph, s):
    for v in  graph[s.id]:
        print("Nothing")

def main():
    Adj = {0: {1},
           1: {2},
           2: {3, 4, 5},
           3: {},
           4: {6},
           5: {6, 7},
           6: {},
           7: {}
          }
    print("The graph: algorithms bfs")
    bfs(Adj, 0)
    print("**************************")
    print("The graph: algorithms dfs")
    dfs(Adj, 0)

    print("Construct the graph")
    graph = {0: {Vertex}}
    print("object oriented! breadth first search")


if __name__=="__main__":
    main()
