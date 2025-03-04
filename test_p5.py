import pytest
from p5 import sakne

def test_sakne():
    assert sakne(2,4) == 2
    assert sakne(6,3) == 0.5
    
    
def test_nav_nulle():
    assert sakne(0, 4) == 0
    assert sakne(0, 16) == 0
    
    
def test_datu_tips():
    assert sakne("hello", 2) == 0 
    assert sakne(2, "hfeh") == 0