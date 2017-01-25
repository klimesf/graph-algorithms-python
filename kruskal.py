from collections import namedtuple

Edge = namedtuple("Edge", ['x', 'y', 'weight'])

# 0 ==12 ==1 == 5 = 2 - 22 - 3
# |        ||       ||       ||
# 15       8        2        4
# |        ||       ||       ||
# 4 - 18 - 5 - 19 - 6 == 3 = 7
# ||       ||       |        |
# 11      10       20        14
# ||       ||       |        |
# 8 == 7 = 9 == 1 = 10==13 = 11
#
# Total cost = 1+2+3+4+5+7+8+10+11+12+13 = 76

graph = [
    Edge(0, 1, 12),
    Edge(0, 4, 15),
    Edge(1, 2, 5),
    Edge(1, 5, 8),
    Edge(2, 3, 22),
    Edge(2, 6, 2),
    Edge(3, 7, 4),
    Edge(4, 5, 18),
    Edge(4, 8, 11),
    Edge(5, 6, 19),
    Edge(5, 9, 10),
    Edge(6, 7, 3),
    Edge(6, 10, 20),
    Edge(8, 9, 7),
    Edge(9, 10, 1),
    Edge(10, 11, 13),
]


# Returns key of Edge
def get_key(edge):
    return edge.weight


class Node:
    value = None
    parent = None

    def __init__(self, value):
        self.value = value
        return

    def get_parent(self):
        if self.parent is None:
            return self
        return self.parent.get_parent()

    def append(self, other_node):
        self.get_parent().parent = other_node.get_parent()
        return


# Finds cost of minimum spanning tree
def kruskal(list_of_edges):
    if len(list_of_edges) < 1:
        return 0

    list_of_edges.sort(key=get_key)

    msp_cost = 0
    union_find = {}

    while len(list_of_edges) > 0:
        next_edge = list_of_edges.pop(0)

        if next_edge.x not in union_find:
            union_find[next_edge.x] = Node(next_edge.x)
        if next_edge.y not in union_find:
            union_find[next_edge.y] = Node(next_edge.y)
        union_find_x = union_find[next_edge.x]
        union_find_y = union_find[next_edge.y]

        if union_find_x.get_parent().value == union_find_y.get_parent().value:
            continue
        msp_cost += next_edge.weight
        union_find_y.append(union_find_x)

    return msp_cost


print kruskal(graph)
