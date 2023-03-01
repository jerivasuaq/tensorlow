import numpy as np
from tensorlow.nodes import Graph, Placeholder, Variable
from tensorlow.operations import add, matmul
from tensorlow.session import Session


class TestPlaceholder:
    def test(self):
        ph = Placeholder

        assert ph is not None


class TestGraph:
    def test_graph(self):
        g = Graph()
        g.set_as_default()

        assert g is not None

    def test_graph_operations(self):
        g = Graph()
        g.set_as_default()

        A = Variable([[10, 20], [30, 40]])
        b = Variable([1, 2])
        x = Placeholder()
        y = matmul(A, x)
        z = add(y, b)

        sess = Session()
        res = sess.run(operation=z, feed_dict={x: 10})

        print(res)
        assert (res == np.array([[101, 202], [301, 402]])).all()
