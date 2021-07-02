import pytest
from fibonacci import fibonacci

def teste1():
    if fibonacci(0) == [0] and fibonacci(-1) == []:
        print("Teste OK")
    else: 
        print("Teste Falhou")

def test_inferior_1():
    print("Testa comprotamento com n < 1")
    assert fibonacci(0) == [0]
    assert fibonacci(-1) == []
