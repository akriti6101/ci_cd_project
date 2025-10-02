from src.app import add,sub

def test_add():
    assert add(2,3)==5
    assert add(1,9)==10

def test_sub():
    assert sub(2,3)==-1
    assert sub(7,2)==5

def test_mul():
    assert mul(2,3)==6
    assert mul(7,0)==0