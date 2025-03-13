import random
import csv
from collections import Counter
from src.modelos.jugador import Jugador
from src.modelos.subasta import SubastaInglesa
from src.modelos.estrategias import (
    EstrategiaDummy,
    EstrategiaAleatoria,
    EstrategiaAgresiva,
    EstrategiaConservadora
)

class Simulacion:
    def __init__(self, num_subastas=50):
        """
        Inicializa la simulación de subastas.

        Args:
            num_subastas (int): Número de subastas a ejecutar.
        """
        self.num_subastas = num_subastas
        self.resultados = []     # Lista de nombres de estrategias ganadoras
        self.estadisticas = []   # Lista de diccionarios con información detallada

    def ejecutar(self):
        """
        Ejecuta 'num_subastas' subastas y recopila estadísticas.

        Returns:
            dict: Un diccionario con el conteo de victorias por estrategia.
        """
        estrategias = [
            EstrategiaDummy,
            EstrategiaAleatoria,
            EstrategiaAgresiva,
            EstrategiaConservadora
        ]
        
        for i in range(self.num_subastas):
            # Crear 5 jugadores con presupuesto 100 y estrategia aleatoria
            jugadores = [
                Jugador(
                    nombre=f"Jugador {j+1}",
                    presupuesto=100,
                    estrategia=random.choice(estrategias)
                )
                for j in range(5)
            ]
            
            subasta = SubastaInglesa(
                jugadores=jugadores,
                precio_inicial=10,
                incremento=1,
                max_rondas=100
            )
            
            ganador = subasta.ejecutar()
            
            if ganador:
                estrategia_ganadora = type(ganador.estrategia).__name__
                self.resultados.append(estrategia_ganadora)
                self.estadisticas.append({
                    "SubastaID": i + 1,
                    "Ganador": ganador.nombre,
                    "EstrategiaGanadora": estrategia_ganadora,
                    "OfertaGanadora": ganador.oferta_final,
                    "NumRondas": subasta.num_rondas
                    # Proxima versión, incluir: "HistorialOfertas": subasta.historial_ofertas
                })
        
        return self.analizar_resultados()

    def analizar_resultados(self):
        """
        Retorna un diccionario con el número de victorias por estrategia.
        """
        conteo = Counter(self.resultados)
        return dict(conteo)

    def guardar_estadisticas_csv(self, nombre_archivo="estadisticas_subastas.csv"):
        """
        Guarda la lista de estadísticas en un archivo CSV.

        Args:
            nombre_archivo (str): Nombre del archivo CSV a crear.
        """
        if not self.estadisticas:
            print("No hay estadísticas para guardar.")
            return

        fieldnames = list(self.estadisticas[0].keys())

        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for registro in self.estadisticas:
                writer.writerow(registro)
        
        print(f"Estadísticas guardadas en {nombre_archivo}")
