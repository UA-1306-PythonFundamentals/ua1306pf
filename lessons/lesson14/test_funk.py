import unittest
from funk import f


class TestF(unittest.TestCase):


    def test1(self):
        actual = f(1, 1, 1)
        self.assertIn(actual, ('NoRoots', "55"))
        self.assertEqual(actual, 'No roots')
    def test2(self):
        actual = f(1, 5, 1)
        self.assertEqual(actual, (-4.7912878474779195, -0.20871215252208009))
    def test3(self):
        actual = f(1, 2, 1)
        self.assertEqual(actual, -1.0)
    def test4(self):
        actual = f(1, 3, 2)
        self.assertEqual(actual, -1.0)



if __name__ == '__main__':
    unittest.main()

