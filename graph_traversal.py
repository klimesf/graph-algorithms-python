from collections import deque

#
#      7 - 8 - 9    15 - 16
#      |       |     |
#      2       |    17
#      |       |
#  0 - 1 - 3 - 10 - 11
#      |
#      4 - 5 - 6  - 14
#              |
#              12 - 13

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1, 7],
    3: [1, 10],
    4: [1, 5],
    5: [4, 6],
    6: [5, 12, 14],
    7: [2, 8],
    8: [7, 9],
    9: [8, 10],
    10: [3, 9, 11],
    11: [10],
    12: [6, 13],
    13: [12],
    14: [6],
    15: [16, 17],
    16: [15],
    17: [15]
}


def create_visited_dict(adjacency_list):
    visited = {}
    for key in adjacency_list:
        visited[key] = False

    return visited


def dfs(adjacency_list):
    visited = create_visited_dict(adjacency_list)

    for vertex in adjacency_list:
        if not visited[vertex]:
            dfs_walk(vertex, adjacency_list, visited)

    return


def dfs_walk(vertex, adjacency_list, visited):
    print vertex,
    visited[vertex] = True
    for value in adjacency_list[vertex]:
        if not visited[value]:
            dfs_walk(value, adjacency_list, visited)

    return


def bfs(adjacency_list):
    visited = create_visited_dict(adjacency_list)

    for vertex in adjacency_list:
        if not visited[vertex]:
            bfs_walk(adjacency_list, visited, deque([vertex]))

    return


def bfs_walk(adjacency_list, visited, to_visit):
    if not to_visit:
        return

    vertex = to_visit.popleft()
    print vertex,
    visited[vertex] = True
    for value in adjacency_list[vertex]:
        if not visited[value]:
            to_visit.append(value)

    bfs_walk(adjacency_list, visited, to_visit)

    return


print "DFS: ",
dfs(graph)
print
print "BFS: ",
bfs(graph)
