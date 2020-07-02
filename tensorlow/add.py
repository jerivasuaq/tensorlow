from tensorlow.operation import Operation

class add(Operation):
    def __init__(self, x, y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var + y_var

