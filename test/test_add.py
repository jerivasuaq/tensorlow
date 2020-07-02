from tensorlow.add import add
from unittest import TestCase

class TestAdd(TestCase):

    def test(self):
        x = []
        y = []
        o = add(x, y)
        self.assertIsNotNone(o)

