import sys
import os
# Añade la carpeta raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.modelos.jugador import Jugador

class EstrategiaDummy:
    def hacer_oferta(self, jugador, precio_actual):
        return 50

def test_creacion_jugador():
    jugador = Jugador("Test", 100, EstrategiaDummy)
    assert jugador.nombre == "Test"
    assert jugador.presupuesto == 100

def test_hacer_oferta_dummy():
    jugador = Jugador("Test", 100, EstrategiaDummy)
    oferta = jugador.hacer_oferta(10)
    assert oferta == 50
    assert oferta <= jugador.presupuesto

