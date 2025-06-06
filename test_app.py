"""
testes de unidade app
"""

from app import soma

def test_soma():
    """ função de teste para o arquivo app"""
    assert soma(2, 3) == 5

def test_main():
    """Teste função principal"""
