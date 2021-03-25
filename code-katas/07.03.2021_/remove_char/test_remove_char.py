import pytest
from .remove_char import remove_char

def basic_test_case():
   assert remove_char('eloquent') == 'loquen'
   assert remove_char('country') == 'ountr'
   assert remove_char('person') == 'erso'
   assert remove_char('place') == 'lac'
   assert remove_char('ok') == ''
   assert remove_char('ooopsss') == 'oopss'
