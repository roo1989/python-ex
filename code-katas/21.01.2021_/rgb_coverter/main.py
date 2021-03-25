"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:
"""

# Hex: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

def rgb_without_hex_function(r, g, b):
    hex_table  = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F',
    }

    ret = ""
    
    arr = [r, g, b]

    for i in arr:
        a,c = round(i/16, 1)
        first = hex_table[a]
        second = hex_table[c*16]
        ret += f"{first}{second}"

        return ret

import unittest

class RGBTestCase(unittest.TestCase):

    def test_zero_values(self):
        self.assertEquals(rgb_without_hex_function(255,255,255), "000000")

