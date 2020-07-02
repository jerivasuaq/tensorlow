from tensorlow.multiply import multiply
from unittest import TestCase

class TestAdd(TestCase):

    def test(self):
        x = []
        y = []
        o = multiply(x, y)
        self.assertIsNotNone(o)

