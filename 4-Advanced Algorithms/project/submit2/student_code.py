import heapq
from math import sqrt  


def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    
    open_set = [(0, start)]  
    came_from = {start: None}
    g_score = {start: 0.0}  # Cost from start to current node
    f_score = {}  # Estimated total cost from start to goal through node
    
    # Calculate heuristic (Euclidean distance)
    def heuristic(node1, node2):
        x1, y1 = M.intersections[node1]
        x2, y2 = M.intersections[node2]
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)
    

    f_score[start] = heuristic(start, goal)
   
    visited = set()
    
    while open_set:
        # Get node with lowest f_score
        current_f, current = heapq.heappop(open_set)
        
        # If we've reached the goal, reconstruct and return the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Reverse to get path from start to goal
        
        # Mark as visited
        visited.add(current)
        
        # Explore neighbors
        for neighbor in M.roads[current]:
            # Skip if already visited
            if neighbor in visited:
                continue
                

            tentative_g = g_score[current] + heuristic(current, neighbor)
            
            # If this path is better than any previous one
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                # Update path and scores
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                
                # Add to open set if not already there
                if neighbor not in [node for _, node in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    # No path found
    return None