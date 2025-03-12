import matplotlib.pyplot as plt

GRID_LINESTYLE = "--"
GRID_ALPHA = 0.7
COLOR_SKYBLUE = "skyblue"

def graficar_resultados(resultados):
    """
    Visualiza los resultados de las subastas mediante un gráfico de barras.

    Args:
        resultados (dict): Diccionario donde las claves son nombres de estrategias 
                           y los valores son la cantidad de victorias obtenidas.
                           Ejemplo: {'EstrategiaAleatoria': 10, 'EstrategiaAgresiva': 15, ...}
    """
    estrategias = list(resultados.keys())
    victorias = list(resultados.values())
    
    plt.figure(figsize=(8, 5))
    plt.bar(estrategias, victorias, color=COLOR_SKYBLUE)
    plt.xlabel("Estrategia")
    plt.ylabel("Número de Victorias")
    plt.title("Comparación de Estrategias en Subastas")
    plt.grid(axis="y", linestyle=GRID_LINESTYLE, alpha=GRID_ALPHA)
    plt.show()

def graficar_evolucion(subasta):
    """
    Grafica la evolución de la mejor oferta en cada ronda de la subasta.
    
    Args:
        subasta: Instancia de SubastaInglesa, que debe tener:
                 - subasta.historial_ofertas: lista de diccionarios, cada uno representando las ofertas de una ronda.
                 - subasta.num_rondas: número total de rondas jugadas.
    """
    # Calcula la mejor oferta de cada ronda
    mejores_ofertas = []
    for ofertas in subasta.historial_ofertas:
        # Suponemos que cada 'ofertas' es un diccionario: {jugador: oferta}
        mejor = max(ofertas.values())
        mejores_ofertas.append(mejor)
    
    rondas = list(range(1, len(mejores_ofertas) + 1))
    
    plt.figure(figsize=(8, 5))
    plt.plot(rondas, mejores_ofertas, marker='o', linestyle='-')
    plt.xlabel("Ronda")
    plt.ylabel("Mejor Oferta")
    plt.title("Evolución de la Mejor Oferta en la Subasta")
    plt.grid(axis="y", linestyle=GRID_LINESTYLE, alpha=GRID_ALPHA)
    plt.show()