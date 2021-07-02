import pytest
from aritimetica import sume, subtraction, multiplication, division, rest, sqrt  
 

def test_sum():
    assert sume(1,1) == 2
    assert sume(-5, -8) == -13

def test_subtraction():
    assert subtraction(1, 0) == 1
    assert subtraction(3, 8) == -5

def test_multiplication():
    assert multiplication(3, 2) == 6
    assert multiplication(-6, 4) == -24
    assert multiplication(1.3, 1.6) == 2.08
    assert multiplication(-2,-3) == 6

def test_division():
    assert division(10,5) == 2
    assert division(2, 3) == 0.67

def test_rest():
    assert rest(3, 2) == 1
    assert rest(2, 3) == 2

def test_sqrt():
    assert sqrt(4) == 2

    
