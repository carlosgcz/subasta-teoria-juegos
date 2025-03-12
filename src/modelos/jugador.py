# src/modelos/jugador.py
from .estrategias import EstrategiaBase, EstrategiaAleatoria, EstrategiaAgresiva, EstrategiaConservadora

class Jugador:
    def __init__(self, nombre, presupuesto, estrategia):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.estrategia = estrategia()  # Instancia de la estrategia
        self.oferta_final = 0

    def hacer_oferta(self, precio_actual):
        oferta = self.estrategia.hacer_oferta(self, precio_actual)
        self.oferta_final = min(oferta, self.presupuesto)
        return self.oferta_final
