import pytest
from ..__main__ import *

def test_case_1():
    assert count([2,3,4,5,6,8,7,6,5,18], [[6,55],[6,45],[6,55],[4,40],[18,60],[10,50]]) == 200
