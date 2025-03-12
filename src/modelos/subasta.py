import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

MAX_OFERTA = 100

class SubastaInglesa:
    def __init__(self, jugadores, precio_inicial=10, incremento=1, max_rondas=100):
        """
        Inicializa una subasta inglesa.

        Args:
            jugadores (list): Lista de jugadores participantes (objetos Jugador).
            precio_inicial (int, optional): Precio inicial de la subasta. Por defecto es 10.
            incremento (int, optional): Incremento mínimo de cada puja. Por defecto es 1.
            max_rondas (int, optional): Número máximo de rondas permitidas para evitar bucles infinitos. Por defecto es 100.
        """
        self.jugadores = jugadores
        self.precio_actual = precio_inicial
        self.incremento = incremento
        self.ganador = None
        self.max_rondas = max_rondas
        
        # Estadísticas:
        self.num_rondas = 0
        self.historial_ofertas = []  # Lista para guardar las ofertas de cada ronda

    def ejecutar(self):
        """
        Ejecuta la subasta inglesa con el enfoque híbrido:
          - Cada ronda, los jugadores hacen su oferta (>= precio_actual).
          - Si la mejor oferta es MAX_OFERTA (100), se filtran los jugadores que también ofrecen 100.
          - De lo contrario, se filtran los jugadores que ofrecen al menos precio_actual + incremento.
          - Se detiene si:
              * Todas las ofertas son iguales (sin progreso).
              * Nadie o todos ofrecen la mejor oferta (sin eliminación).
              * Se llega al número máximo de rondas.
        Retorna el jugador ganador o None si no se encontró un ganador.
        """
        logger.info(f"Inicio de la subasta con precio inicial de ${self.precio_actual}")
        ronda = 0

        while len(self.jugadores) > 1 and ronda < self.max_rondas:
            ronda += 1
            logger.info(f"Ronda {ronda}:")

            # Diccionario de ofertas para esta ronda
            ofertas_ronda = {}
            for jugador in self.jugadores:
                oferta = jugador.hacer_oferta(self.precio_actual)
                ofertas_ronda[jugador] = oferta

            # Guardamos las ofertas de esta ronda en el historial
            self.historial_ofertas.append(ofertas_ronda)

            # Calculamos la mejor oferta de la ronda
            mejor_oferta = max(ofertas_ronda.values())
            logger.info(f"Ofertas: {[ (j.nombre, o) for j, o in ofertas_ronda.items() ]} -> Mejor oferta: {mejor_oferta}")

            # Si todas las ofertas son iguales, se termina la subasta
            if len(set(ofertas_ronda.values())) == 1:
                logger.info("Todas las ofertas son iguales; terminando la subasta.")
                break

            # Actualizamos el precio actual
            self.precio_actual = mejor_oferta

            # Caso especial: mejor oferta = 100
            if mejor_oferta == MAX_OFERTA:
                jugadores_filtrados = [j for j in self.jugadores if ofertas_ronda[j] == MAX_OFERTA]
                if not jugadores_filtrados:
                    logger.info("Nadie pudo mantener la oferta de 100; terminando la subasta.")
                    break
                if len(jugadores_filtrados) == len(self.jugadores):
                    logger.info("Varios jugadores ofrecieron 100 y no se elimina a nadie; terminando la subasta.")
                    break
            else:
                # Regla general: para continuar, la oferta debe ser al menos precio_actual + incremento
                jugadores_filtrados = [
                    j for j in self.jugadores
                    if ofertas_ronda[j] >= self.precio_actual + self.incremento
                ]
                if not jugadores_filtrados:
                    logger.info("Ningún jugador pujó lo suficiente para continuar; terminando la subasta.")
                    break
                if len(jugadores_filtrados) == len(self.jugadores):
                    logger.info("Ningún jugador fue eliminado en esta ronda; terminando la subasta.")
                    break

            self.jugadores = jugadores_filtrados

        # Número de rondas realmente jugadas
        self.num_rondas = ronda

        # Determinamos el ganador (si queda al menos un jugador)
        if self.jugadores:
            self.ganador = self.jugadores[0]
            logger.info(f"Ganador final: {self.ganador.nombre} con oferta de ${self.ganador.oferta_final} (en {ronda} ronda(s))")
        else:
            logger.info("No se encontró ganador en la subasta.")
            self.ganador = None

        return self.ganador

