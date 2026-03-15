class Problem:
    def initial_state(self):
        raise NotImplementedError

    def goal_test(self, state):
        raise NotImplementedError

    def get_neighbors(self, state):
        raise NotImplementedError

    def pretty_print(self, state):
        raise NotImplementedError
