import unittest
from app import greet


class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")


if _ _name_ _ == "_ _main_ _":
    unittest.main()
