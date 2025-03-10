# Simulación de Subastas con Teoría de Juegos

Este proyecto implementa diferentes tipos de subastas (Inglesa, Holandesa, Primer Precio, Vickrey) utilizando teoría de juegos y estrategias de puja en Python.

## Estructura del Proyecto

subasta-teoria-juegos/
│── src/                     # Código fuente
│   ├── __init__.py
│   ├── modelos/             # Módulo para clases de dominio
│   │   ├── __init__.py
│   │   ├── jugador.py       # Clase Jugador y estrategias
│   │   ├── subasta.py       # Clases base y tipos de subasta
│   │   ├── estrategias.py   # Estrategias avanzadas de puja
│   ├── simulacion.py        # Múltiples rondas y análisis
│   ├── visualizacion.py     # Gráficos de los resultados
│── data/                    # Datos de simulaciones
│── notebooks/               # Experimentos en Jupyter Notebook
│── tests/                   # Pruebas unitarias con pytest
│── main.py                  # Punto de entrada para ejecutar todo
│── README.md                # Explicación del proyecto
│── requirements.txt         # Librerías necesarias
