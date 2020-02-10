"""
Adjacent lists
"""


class Vertex:
    def __init__(self, key):
        self._id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight: int = 0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connected_to: ' + str([x._id for x in self.connected_to])

    @property
    def connections(self):
        return self.connected_to.keys()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, key):
        self._id = key

    def weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def vertex(self, n):
        return self.vert_list.get(n)

    def __contains__(self, item):
        return item in self.vert_list

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    @property
    def vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vert_list)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.connections:
            print(v.id, w.id)
