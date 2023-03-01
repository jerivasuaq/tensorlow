import pytest

from tensorlow.operations import Operation, add, multiply


class TestOperation:
    def test(self):
        x = []
        o = Operation(x)
        assert o is not None


# class TestAdd():

#     def test(self):
#         x = []
#         y = []
#         o = add(x, y)
#         self.assertIsNotNone(o)


# class TestAdd:
#     def test(self):
#         x = []
#         y = []
#         o = multiply(x, y)
#         self.assertIsNotNone(o)
