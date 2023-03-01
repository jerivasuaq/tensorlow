import pytest
from tensorlow.nodes import Placeholder, Variable

from tensorlow.operations import Operation, add, multiply


class TestOperation:
    def test(self):
        x = []
        o = Operation(x)
        assert o is not None


class TestAdd:
    def test(self):
        a = Variable(10)
        b = Variable(20)

        o = add(a, b)

        assert o is not None


class TestMultiply:
    def test(self):
        a = Variable(10)
        b = Variable(20)

        o = multiply(a, b)

        assert o is not None
