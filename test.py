import unittest


def list_sum(lst):
    return sum(lst)


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = list_sum(data)
        self.assertEqual(result, 6)

    def test_list_float(self):
        """
        Test that it can sum a list of integers
        """
        data = [1.1, 2.2, 3.3]
        result = list_sum(data)
        self.assertEqual(result, 6.6)


if __name__ == '__main__':
    unittest.main()

