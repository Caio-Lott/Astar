from queue import PriorityQueue

def astar(start, goal, neighbors_fn, heuristic_fn):
    frontier = PriorityQueue()
    frontier.put((0 + heuristic_fn(start), start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return list(reversed(path))

        for neighbor in neighbors_fn(current):
            new_cost = cost_so_far[current] + 1  # Assuming all edges have unit cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(neighbor)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

    # No path found
    return None
