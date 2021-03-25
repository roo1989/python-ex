import rgb
import unittest

class RGPTestCase(unittest.TestCase):

    def test_zero_values(self):
        self.assertEquals(rgb(0,0,0), "000000")
        

