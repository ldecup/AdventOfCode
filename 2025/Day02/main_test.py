import unittest

from main import hasRangeInvalidIDs

class test_hasRangeInvalidIDs(unittest.TestCase):
    def testA(self):
        self.assertEqual(hasRangeInvalidIDs(("11","22")), 33)
    def testB(self):
        self.assertEqual(hasRangeInvalidIDs(("95","115")), 99)
    def testC(self):
        self.assertEqual(hasRangeInvalidIDs(("998","1012")), 1010)
    def testD(self):
        self.assertEqual(hasRangeInvalidIDs(("1188511880","1188511890")), 1188511885)
    def testE(self):
        self.assertEqual(hasRangeInvalidIDs(("2121212118","2121212124")), 0)



if __name__ == '__main__':
    unittest.main()