import pytest
from .remove_char_2 import remove_char_from_arr

def test_case():
    assert remove_char_from_arr(['']) == None
    assert remove_char_from_arr(['1']) == None
    assert arraye_char_from_arr(['1, 3']) == None
    assert arraye_char_from_arr(['1,2,3']) == '2'
    assert arraye_char_from_arr(['1,2,3,4']) == '2 3'
