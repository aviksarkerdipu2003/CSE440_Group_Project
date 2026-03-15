import heapq    #import heap based priority queue


class Node:
   
   # Node class for search tree
   

    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost   # g(n)= cost of arrival

    def path(self):
        
        #Reconstruct solution path
        
        node = self
        path = []

        while node is not None:
            path.append(node.state)
            node = node.parent

        return list(reversed(path))


def astar_search(problem, heuristic):
    """
    A* Search Algorithm

    f(n) = g(n) + h(n)

    g(n) = path cost
    h(n) = heuristic estimate
    """

    start_node = Node(problem.start)

    frontier = []
    heapq.heappush(frontier, (heuristic(problem.start), start_node))

    explored = set()

    while frontier:

        _, current_node = heapq.heappop(frontier)
        current_state = current_node.state

        if problem.is_goal(current_state):
            return current_node.path()

        explored.add(current_state)

        successors = problem.get_successors(current_state)

        for next_state in successors:

            if next_state not in explored:

                g = current_node.cost + 1
                h = heuristic(next_state)

                child = Node(next_state, current_node, g)

                f = g + h

                heapq.heappush(frontier, (f, child))

    return None
