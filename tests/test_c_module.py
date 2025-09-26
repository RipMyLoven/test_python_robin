import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_fibonacci_small():
    """Test Fibonacci arvude arvutamist."""
    assert [fibonacci(i) for i in range(6)] == [0,1,1,2,3,5]
    assert fibonacci(10) == 55

def test_prime_factors_basic():
    """Test algtegurite leidmist."""
    assert prime_factors(12) == [2,2,3]
    assert prime_factors(97) == [97]def test_bankaccount():
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 50)
    acc1.deposit(50)
    acc1.withdraw(30)
    acc1.transfer_to(acc2, 20)
    assert acc1.balance() == 100
    assert acc2.balance() == 70
    assert isinstance(acc1.balance(), int)

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8

def test_prime_factors():
    assert prime_factors(2) == [2]
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(28) == [2, 2, 7]

def test_moving_average():
    vals = [1, 2, 3, 4, 5]
    assert moving_average(vals, 1) == [1, 2, 3, 4, 5]
    assert moving_average(vals, 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average(vals, 3) == [2.0, 3.0, 4.0]

def test_normalize_scores():
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize_scores([25, 75]) == [0.25, 0.75]
