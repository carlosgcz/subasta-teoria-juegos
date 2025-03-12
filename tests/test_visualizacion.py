import os
import sys
import pytest
import matplotlib.pyplot as plt

# Aseguramos que la raíz del proyecto esté en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.visualizacion import graficar_resultados

def test_graficar_resultados(monkeypatch):
    """
    Verifica que la función graficar_resultados invoque plt.show()
    sin abrir realmente la ventana (usando monkeypatch).
    """
    show_called = False

    def fake_show():
        nonlocal show_called
        show_called = True

    # Reemplaza plt.show con fake_show para que no se abra la ventana
    monkeypatch.setattr(plt, "show", fake_show)

    # Datos de ejemplo para la prueba
    datos_ejemplo = {"EstrategiaA": 3, "EstrategiaB": 5, "EstrategiaC": 2}
    
    # Llamamos a la función; no es necesario capturar la salida, solo asegurarnos de que se llame a plt.show()
    graficar_resultados(datos_ejemplo)
    
    assert show_called, "La función plt.show() no fue llamada"
    
