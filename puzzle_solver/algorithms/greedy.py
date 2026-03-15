#Greedy Best First Search Algorithm
import heapq   #heapq is python's priority queue implementation


class Node:                 #A Node represents a state in the search tree
    """
    Node used in search tree
    """

    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def path(self):
        """
        Returns the path from root to current node
        """
        node = self
        path = []

        while node is not None:
            path.append(node.state)
            node = node.parent

        return list(reversed(path))


def greedy_search(problem, heuristic):
    """
    Greedy Best-First Search Algorithm

    Parameters
    ----------
    problem : puzzle problem instance
    heuristic : heuristic function

    Returns
    -------
    solution path or None
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

                child = Node(next_state, current_node)

                priority = heuristic(next_state)

                heapq.heappush(frontier, (priority, child))

    return None
