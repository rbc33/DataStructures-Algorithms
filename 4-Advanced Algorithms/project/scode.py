import heapq
from math import sqrt

def shortest_path(M, start, goal):
    visited = set()
    g_score = {start: 0.0}
    came_from = {start:None}
    open_set = [(0, start)]
    f_score = {}

    def euclidean(node1, node2):
        x1, y1 = M.intersections[node1]
        x2, y2 = M.intersections[node2]
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)

    f_score[start] = euclidean(start, goal)

    while len(open_set) > 0:
        current_f, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Reverse to get path from start to goal
        visited.add(current)
        for node in M.roads[current]:
            if node in visited:
                continue
            tentative_g = g_score[current] + euclidean(node, goal)

            if node not in g_score or tentative_g < g_score[node]:
                came_from[node] = current
                g_score[node] = tentative_g
                f_score[node] = g_score[node] + euclidean(node, goal)

            if node not in [node for _, node in open_set]:
                heapq.heappush(open_set, (f_score[node], node))
                
    return [-1]