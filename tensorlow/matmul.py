import operation
import numpy as np

class matmul(Operation):
    def __init__(self, x, y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var.dot(y_var)

if __name__ == '__main__':
    x= [1]
    y= [2]
    operation = matmul(x,y)


