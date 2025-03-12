## Proyecto: Simulación de Subastas con Teoría de Juegos

**Descripción:**  
Este proyecto simula subastas utilizando conceptos de teoría de juegos y estrategias de puja. Se integran las siguientes funcionalidades:

- **Lógica de Subastas:**  
  Una implementación de la subasta inglesa (con enfoque híbrido) que permite realizar múltiples rondas de puja, eliminando jugadores según reglas definidas y registrando estadísticas (número de rondas, oferta ganadora, evolución de ofertas, etc.).

- **Estrategias de Puja:**  
  Varias estrategias de puja (Aleatoria, Agresiva, Conservadora, Dummy) implementadas con el patrón de diseño Strategy para permitir comparar su eficacia.

- **Simulación y Análisis:**  
  Un módulo que ejecuta múltiples subastas, recopila estadísticas y exporta la información a un archivo CSV para su posterior análisis.

- **Visualización:**  
  Funciones que generan gráficos (por ejemplo, gráfico de barras y gráfico de evolución de la mejor oferta por ronda) para visualizar los resultados de la simulación.

---
## Requisitos Previos

**Python 3.11+:**  
Asegúrate de tener Python 3.11 o superior instalado.

**Entorno Virtual (Recomendado):**  
Es ideal usar un entorno virtual (por ejemplo, Conda o virtualenv) para aislar las dependencias del proyecto.

**Dependencias Python:**  
Instala las siguientes bibliotecas en tu entorno:
```bash
pip install matplotlib pytest
```
---
## Instalación y Configuración

**Clonar el Repositorio:**
```bash
git clone https://github.com/tu_usuario/subasta-teoria-juegos.git  
cd subasta-teoria-juegos
```

---
**Crear y Activar el Entorno Virtual (opcional pero recomendado):**

- **Con Conda:**
```bash
conda create -n subasta-env python=3.11  
conda activate subasta-env  
pip install matplotlib pytest
```

- **O con virtualenv:**
```bash
python -m venv env
```
**En Windows:**
```bash
env\Scripts\activate  
pip install matplotlib pytest
```
---
## Uso del Proyecto

**Ejecutar la Simulación:**  
Para correr la simulación y ver el resultado, ejecuta:
```bash
python main.py
```
Este comando:
- Ejecuta múltiples subastas (definidas en src/simulacion.py).
- Exporta las estadísticas a un archivo CSV (estadisticas_subastas.csv).
- Genera gráficos que muestran la comparación de estrategias (en src/visualizacion.py).

---
**Ejecutar Scripts de Prueba:**

- **Script de Prueba de Subasta Individual:**  
  Puedes ejecutar el script prueba_subasta.py para probar una subasta en forma aislada y ver la evolución de las ofertas:
```bash
  python prueba_subasta.py
```
- **Pruebas Unitarias con Pytest:**  
  Para correr todas las pruebas unitarias, usa:
```bash
  python -m pytest -v
```
---
## Estructura del Proyecto

subasta-teoria-juegos/  
│  
├── src/                        # Código fuente  
│   ├── __init__.py             # Marca el paquete 'src'  
│   ├── modelos/                # Módulo para las clases de dominio  
│   │   ├── __init__.py         # Marca el subpaquete 'modelos'  
│   │   ├── jugador.py          # Clase Jugador y lógica de pujas  
│   │   ├── subasta.py          # Implementación de la subasta inglesa  
│   │   └── estrategias.py      # Estrategias de puja (Aleatoria, Agresiva, Conservadora, Dummy)  
│   ├── simulacion.py           # Orquesta la ejecución de múltiples subastas y exporta estadísticas a CSV  
│   └── visualizacion.py        # Funciones para generar gráficos (barras, evolución, etc.)  
│  
├── tests/                      # Pruebas unitarias  
│   ├── test_jugador.py         # Tests para la clase Jugador  
│   ├── test_subasta.py         # Tests para la lógica de la subasta  
│   └── test_simulacion_csv.py  # Test para la exportación a CSV (opcional)  
│  
├── main.py                     # Punto de entrada principal del proyecto  
├── README.md                   # Documentación del proyecto (este archivo)  
├── pytest.ini                  # Configuración de Pytest  
├── requirements.txt            # Archivo para dependencias (actualizado según sea necesario)  
├── prueba.py                   # Script de prueba simple (opcional)  
└── prueba_subasta.py           # Script para probar una subasta individual (con visualización)

Cada carpeta y archivo tiene un rol específico para mantener el código modular, escalable y fácil de probar.

---
## Exportación de Estadísticas a CSV

La simulación genera un archivo CSV llamado estadisticas_subastas.csv que contiene:

- SubastaID: Identificador de cada subasta.  
- Ganador: Nombre del jugador ganador.  
- EstrategiaGanadora: Estrategia usada por el ganador.  
- OfertaGanadora: Oferta final ganadora.  
- NumRondas: Número de rondas que duró la subasta.  

Este archivo sirve para análisis estadísticos posteriores y para evaluar el comportamiento de las estrategias de puja.

---
## Visualización de Resultados

Se incluyen funciones para:

**Gráfico de Barras:**  
Compara el número de victorias por estrategia.

**Gráfico de Evolución:**  
Muestra la evolución de la mejor oferta a lo largo de las rondas de una subasta individual (consulta graficar_evolucion en src/visualizacion.py).

---
## Documentación Interna

- **Docstrings:**  
  Cada clase y función del proyecto tiene docstrings que explican su propósito, parámetros y valores de retorno.

- **Comentarios:**  
  Se han añadido comentarios en el código para facilitar la comprensión de la lógica.

---
## Contribuciones

Si deseas contribuir:

1. Haz un fork del repositorio.  
2. Crea una rama para tus cambios.  
3. Realiza tus mejoras y añade pruebas unitarias.  
4. Envía un Pull Request describiendo tus cambios.

---
## Próximos Pasos

- Refinar la lógica de la subasta: Agregar nuevos tipos de subastas (Holandesa, Primer Precio, Vickrey) y estrategias avanzadas.  
- Ampliar la visualización: Crear dashboards interactivos o gráficos adicionales para un análisis más profundo.  
- Análisis de datos: Exportar y analizar las estadísticas con pandas o Jupyter Notebook.

---
## Instrucciones Finales

**Instalación:**  
Sigue las instrucciones de la sección de Instalación para configurar tu entorno.

**Ejecución:**  
Corre el proyecto con ```python main.py``` y ejecuta los tests con python ```-m pytest -v```.

**Exportación CSV:**  
Revisa el archivo estadisticas_subastas.csv para ver los resultados de las subastas.
