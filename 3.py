import unittest

def getAverage(array):
    if not array:
        return None
    return sum(array) / len(array)

class GetAverageTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(getAverage([]))

    def test_positive_numbers(self):
        self.assertEqual(getAverage([1, 2, 3, 4, 5]), 3)

    def test_negative_numbers(self):
        self.assertEqual(getAverage([-1, -2, -3, -4, -5]), -3)

    def test_float_numbers(self):
        self.assertAlmostEqual(getAverage([1.5, 2.5, 3.5]), 2.5)

    def test_mixed_numbers(self):
        self.assertEqual(getAverage([-2, -0.5, 0, 0.5, 2]), 0)

if __name__ == '__main__':
    unittest.main()
