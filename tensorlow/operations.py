from tensorlow.nodes import Graph, Node

import torch


class Operation(Node):
    def __init__(self, input_nodes=[]):
        super().__init__(input_nodes)
        
        for node in input_nodes:
            node.output_nodes.append(self)

        Graph._default_graph.operations.append(self)

    def compute(self):
        pass


class add(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var + y_var


class multiply(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var * y_var


class matmul(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var.dot(y_var)


if __name__ == "__main__":
    x = [1]
    y = [2]
    operation = matmul(x, y)

    print(operation.compute(x, y))
