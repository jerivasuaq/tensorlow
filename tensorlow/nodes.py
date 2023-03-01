class Graph:
    _default_graph = None

    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []

    def set_as_default(self):
        Graph._default_graph = self


class Node:
    input_nodes = []
    output_nodes = []
    input_values = []
    output_value = None

    def __init__(self, input_nodes=[]):
        self.input_nodes = input_nodes
        self.output_nodes = []
        self.input_values = []
        self.output_value = None


class Placeholder(Node):
    def __init__(self):
        self.output_nodes = []
        Graph._default_graph.placeholders.append(self)


class Variable(Node):
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.output_nodes = []
        Graph._default_graph.variables.append(self)
