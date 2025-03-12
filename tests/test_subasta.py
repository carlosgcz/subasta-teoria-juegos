# tests/test_subasta.py
import sys
import os
# Añade la carpeta raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.modelos.jugador import Jugador
from src.modelos.subasta import SubastaInglesa

# Definimos una estrategia dummy para controlarlo en la prueba
class DummyEstrategia:
    def hacer_oferta(self, jugador, precio_actual):
        # Retorna un valor fijo para facilitar la prueba (por ejemplo, 50)
        return 50

def test_subasta_inglesa_ganador():
    """
    En esta prueba:
    - Creamos 3 jugadores, cada uno con el DummyEstrategia, por lo que siempre ofertan 50.
    - Ejecutamos la subasta inglesa a partir de un precio inicial de 10.
    - Verificamos que la subasta retorne un ganador, y que su oferta final sea 50.
    """
    # Creamos una lista de jugadores con la estrategia dummy
    jugadores = [Jugador(f"Jugador {i}", 100, DummyEstrategia) for i in range(3)]
    
    # Creamos la subasta inglesa con un precio inicial de 10
    subasta = SubastaInglesa(jugadores, precio_inicial=10)
    
    # Ejecutamos la subasta y obtenemos el ganador
    ganador = subasta.ejecutar()
    
    # Verificamos que se haya obtenido un ganador
    assert ganador is not None, "La subasta debe retornar un ganador"
    # Verificamos que la oferta final sea 50 (la fija que retorna la estrategia dummy)
    assert ganador.oferta_final == 50, "La oferta final debe ser 50"
    # (Opcional) Si la implementación de la subasta mantiene el orden, podríamos esperar que el primer jugador gane:
    assert ganador.nombre == "Jugador 0", "Se espera que el primer jugador gane en empate"
