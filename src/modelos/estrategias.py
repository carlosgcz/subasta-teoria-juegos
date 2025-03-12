import random

class EstrategiaBase:
    """Clase base para todas las estrategias de puja."""
    def hacer_oferta(self, jugador, precio_actual):
        raise NotImplementedError("Implementa este método en la estrategia concreta.")
    
class EstrategiaDummy(EstrategiaBase):
    """Estrategia para pruebas: retorna un valor fijo."""
    def hacer_oferta(self, jugador, precio_actual):
        return 50

class EstrategiaAleatoria(EstrategiaBase):
    """Estrategia que elige un valor aleatorio entre 1 y el presupuesto del jugador."""
    def hacer_oferta(self, jugador, precio_actual):
        return random.randint(1, jugador.presupuesto)
    
class EstrategiaAgresiva(EstrategiaBase):
    """Estrategia que apuesta un porcentaje alto del presupuesto."""
    def hacer_oferta(self, jugador, precio_actual):
        return int(jugador.presupuesto * 0.9)
    
class EstrategiaConservadora(EstrategiaBase):
    """Estrategia que incrementa ligeramente la oferta actual."""
    def hacer_oferta(self, jugador, precio_actual):
        return int(jugador.presupuesto * 1.05)
