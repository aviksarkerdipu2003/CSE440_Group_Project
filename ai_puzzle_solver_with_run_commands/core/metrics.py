import time

class Metrics:
    def __init__(self):
        self.nodes_expanded=0; self.max_depth=0; self.solution_length=0; self.start=None; self.end=None
    def start_timer(self): self.start=time.time()
    def stop_timer(self): self.end=time.time()
    def summary(self):
        return {
            "nodes_expanded": self.nodes_expanded,
            "max_depth": self.max_depth,
            "solution_length": self.solution_length,
            "elapsed_time_sec": None if self.start is None or self.end is None else self.end-self.start
        }
