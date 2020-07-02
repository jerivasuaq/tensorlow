from tensorlow import *

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

y = multiply(A,x)
z = add(y, b)

