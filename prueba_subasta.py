# prueba_subasta.py
from src.modelos.jugador import Jugador
from src.modelos.subasta import SubastaInglesa
from src.modelos.estrategias import EstrategiaAleatoria, EstrategiaAgresiva, EstrategiaConservadora, EstrategiaDummy
from src.visualizacion import graficar_evolucion

# Crea una lista de jugadores con diferentes estrategias
jugadores = [
    Jugador("Jugador 1", 100, EstrategiaAleatoria),
    Jugador("Jugador 2", 100, EstrategiaAgresiva),
    Jugador("Jugador 3", 100, EstrategiaConservadora),
    Jugador("Jugador 4", 100, EstrategiaDummy),
    Jugador("Jugador 5", 100, EstrategiaAleatoria)
]

# Instancia una subasta con los jugadores, precio inicial de 10, incremento de 1 y máximo 100 rondas
subasta = SubastaInglesa(jugadores, precio_inicial=10, incremento=1, max_rondas=100)

# Ejecuta la subasta (esto registrará el historial de ofertas y el número de rondas)
ganador = subasta.ejecutar()

# Imprime el ganador para verificar en la terminal
print(f"El ganador es: {ganador.nombre} con una oferta de ${ganador.oferta_final}")

# Visualiza la evolución de la mejor oferta por ronda
graficar_evolucion(subasta)
