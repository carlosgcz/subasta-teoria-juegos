from src.simulacion import Simulacion
from src.visualizacion import graficar_resultados

def main():
    simulacion = Simulacion(num_subastas=50)
    resultados = simulacion.ejecutar()
    # Muestra el conteo de victorias en la terminal
    print("Conteo de victorias:", resultados)
    
    # Guarda las estadísticas en CSV
    simulacion.guardar_estadisticas_csv("estadisticas_subastas.csv")

    # Visualiza los resultados con el gráfico de barras
    graficar_resultados(resultados)

if __name__ == "__main__":
    main()

