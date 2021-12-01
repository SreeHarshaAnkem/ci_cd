from multiplier import multiply
import unittest


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3), 9)
        self.assertEqual(multiply(-1), -3)
    

if __name__ == "__main__":
    unittest.main()