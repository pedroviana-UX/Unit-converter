from src.converter import converter
import pytest

def test_metro_para_quilometro():
    resultado = converter(1, "metro", "quilometro")
    assert resultado == 0.001

def test_quilometro_para_metro():
    resultado = converter(1, "quilometro", "metro")
    assert resultado == 1000

def test_quilograma_para_grama():
    resultado = converter(1, "quilograma", "grama")
    assert resultado == 1000

def test_celsius_para_fahrenheit():
    resultado = converter(1, "celsius", "fahrenheit")
    assert resultado == 33.8

def test_unidades_incompativeis():
    with pytest.raises(ValueError):
        converter(10, "metro", "quilograma")

def test_mesma_unidade():
    resultado = converter(42, "metro", "metro")
    assert resultado == 42      