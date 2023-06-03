from Multiply_two_variables import Mul_two_variables

def test_1():
    assert Mul_two_variables(2, 3) == 6
    
def test_2():   
    assert Mul_two_variables(-3, 5) == -15
    
def test_3():
    assert Mul_two_variables(-4, -3) == 12
    