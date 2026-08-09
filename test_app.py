import unittest
from app import greet


class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")


if name == "__main__":
    unittest.main()
