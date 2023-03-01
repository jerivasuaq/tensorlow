from tensorlow.nodes import Graph, Placeholder, Variable
from tensorlow.session import Session
from tensorlow.operations import add, matmul, Sigmoid


class TestSession:
    def test_session(self):
        g = Graph()
        g.set_as_default()
        x = Placeholder()
        w = Variable([1, 1])
        b = Variable(-5)
        z = add(matmul(w, x), b)
        a = Sigmoid(z)

        sess = Session()
        res = sess.run(operation=a, feed_dict={x: [8, 10]})

        assert res == 0.999997739675702

        res = sess.run(operation=a, feed_dict={x: [2, -10]})
        assert res == 2.2603242979035746e-06
