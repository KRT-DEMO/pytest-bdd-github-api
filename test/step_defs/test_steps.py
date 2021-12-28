import pytest

def test_something(x=5):
    x = x+1
    assert (x>5)