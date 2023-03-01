from tensorlow import Graph, Variable, Placeholder
from tensorlow.nodes import Node
from tensorlow.operations import Operation, multiply, add
from tensorlow.session import Session


if __name__ == "__main__":
    # z = Ax +b
    # A = 10
    # b = 1
    #
    # z = 10x + 1

    g = Graph()
    g.set_as_default()

    A = Variable(10)
    b = Variable(1)
    x = Placeholder()

    y = multiply(A, x)
    z = add(y, b)

    sess = Session()
    result = sess.run(operation=z, feed_dict={x: 10})

    print(result)
