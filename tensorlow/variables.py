class Variable():
    def __init__(self, initial_value = None):
        self.value = initial_value
        self.output_nodes = []
        _default_graph.variables.append(self)



