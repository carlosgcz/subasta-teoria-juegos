import os
import sys
import pytest

# Aseguramos que la raíz del proyecto esté en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.simulacion import Simulacion

def test_guardar_estadisticas_csv(tmp_path):
    """
    Ejecuta una simulación pequeña y verifica que el archivo CSV se genera y contiene contenido.
    """
    # Crea una simulación con un número reducido de subastas para la prueba
    sim = Simulacion(num_subastas=2)
    sim.ejecutar()
    
    # Usa el fixture tmp_path de pytest para generar un archivo temporal
    csv_file = tmp_path / "estadisticas_test.csv"
    sim.guardar_estadisticas_csv(str(csv_file))
    
    # Verifica que el archivo CSV fue creado
    assert csv_file.exists(), "El archivo CSV no fue creado."
    
    # Lee el contenido del archivo y verifica que no esté vacío (debe tener al menos la cabecera y una fila)
    with open(csv_file, "r", encoding="utf-8") as f:
        contenido = f.read()
        assert len(contenido) > 0, "El archivo CSV está vacío."
        # Opcional: verificar que contenga alguna de las claves esperadas (por ejemplo, "SubastaID")
        assert "SubastaID" in contenido, "El encabezado del CSV no contiene la clave 'SubastaID'."
