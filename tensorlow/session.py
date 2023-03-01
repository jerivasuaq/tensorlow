from typing import List
import numpy as np
from tensorlow.nodes import Node, Placeholder, Variable
from tensorlow.operations import Operation


class Session:
    def traverse_postorder(self, operation: Operation) -> List[Node]:
        """
        PostOrder Traversal of Nodes.
        Basically makes sure computations are done in the correct order
        (Ax first, then Ax+b).
        """

        nodes_postorder = []

        def recurse(node: Node):
            if isinstance(node, Operation):
                for input_node in node.input_nodes:
                    recurse(input_node)

            nodes_postorder.append(node)

        recurse(operation)

        return nodes_postorder

    def run(self, operation: Operation, feed_dict={}):
        nodes_postorder = self.traverse_postorder(operation)

        for node in nodes_postorder:
            if isinstance(node, Placeholder):
                node.output_value = feed_dict[node]
            elif isinstance(node, Variable):
                node.output_value = node.value
            elif isinstance(node, Operation):
                inputs = []
                for input_node in node.input_nodes:
                    inputs.append(input_node.output_value)

                node.inputs = inputs
                node.output_value = node.compute(*node.inputs)

            if type(node.output_value) == list:
                node.output_value = np.array(node.output_value)

        return operation.output_value
