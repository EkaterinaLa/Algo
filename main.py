import collections
import random
import itertools


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_coord(self, x, y, h):
        self.graph.append([x, y, h])


def algo_levit(gr, start):
    m0 = []
    m1 = collections.deque()
    m2 = [x for x in range(gr.vertices)]

    m1.append(m2.pop(start))

    dist = [float('inf')] * gr.vertices
    dist[start] = 0

    p = [-1] * gr.vertices

    while m1:
        current = m1.popleft()
        for x, y, h in gr.graph:
            if x == current:
                if y in m2:
                    dist[y] = dist[x] + h
                    m1.append(y)
                    m2.remove(y)
                    p[y] = x

                elif y in m1:
                    if dist[y] >= dist[x] + h:
                        dist[y] = dist[x] + h
                        p[y] = x

                elif y in m0:
                    if dist[y] > dist[x] + h:
                        dist[y] = dist[x] + h
                        m1.appendleft(y)
        m0.append(current)

    return dist


gr = Graph(7)
gr.add_coord(0, 1, 1)
gr.add_coord(0, 2, 3)
gr.add_coord(0, 3, 4)
gr.add_coord(1, 2, 1)
gr.add_coord(1, 4, 6)
gr.add_coord(2, 3, 2)
gr.add_coord(2, 5, 5)
gr.add_coord(3, 5, 3)
gr.add_coord(4, 5, 4)


print(algo_levit(gr, 0))

