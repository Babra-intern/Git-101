import calculator

def test_add():
    assert calculator.add(10, 5) == 15
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-3, -1) == -4

def test_subtract():
    assert calculator.subtract(10, 5) == 5
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(-1, -1) == 0

def test_multiply():
    assert calculator.multiply(10, 5) == 50
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1

def test_divide():
    assert calculator.divide(10, 5) == 2
    assert calculator.divide(-1, 1) == -1
    assert calculator.divide(-1, -1) == 1
    assert calculator.divide(5, 2) == 2.5

    try:
        calculator.divide(10, 0)
    except ValueError:
        pass  

if __name__ == '__main__':
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")
