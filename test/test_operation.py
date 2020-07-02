from src.operation import Operation
from unittest import TestCase

class TestOperation(TestCase):

    def test(self):
        x = []
        o = Operation(x)
        self.assertIsNotNone(o)

