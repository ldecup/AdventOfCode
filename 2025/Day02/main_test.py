import unittest

from main import hasRangeInvalidIDsP1
from main import hasRangeInvalidIDsP2

class test_hasRangeInvalidIDsP1(unittest.TestCase):
    def testA(self):
        self.assertEqual(hasRangeInvalidIDsP1(("11","22")), 33)
    def testB(self):
        self.assertEqual(hasRangeInvalidIDsP1(("95","115")), 99)
    def testC(self):
        self.assertEqual(hasRangeInvalidIDsP1(("998","1012")), 1010)
    def testD(self):
        self.assertEqual(hasRangeInvalidIDsP1(("1188511880","1188511890")), 1188511885)
    def testE(self):
        self.assertEqual(hasRangeInvalidIDsP1(("2121212118","2121212124")), 0)

class test_hasRangeInvalidIDsP2(unittest.TestCase):
    def testA(self):
        self.assertEqual(hasRangeInvalidIDsP2(("11","22")), 33)
    def testB(self):
        self.assertEqual(hasRangeInvalidIDsP2(("95","115")), 210)
    def testC(self):
        self.assertEqual(hasRangeInvalidIDsP2(("998","1012")), 2009)
    def testD(self):
        self.assertEqual(hasRangeInvalidIDsP2(("1188511880","1188511890")), 1188511885)
    def testE(self):
        self.assertEqual(hasRangeInvalidIDsP2(("2121212118","2121212124")), 2121212121)
    def testF(self):
        self.assertEqual(hasRangeInvalidIDsP2(("565653","565659")), 565656)



if __name__ == '__main__':
    unittest.main()