import random
import os

RUTA_ACTUAL = os.path.dirname(os.path.abspath(__file__))

class JuegoAdivinanza:
    """
    Clase que representa el juego de adivinar un número.
    """
    def __init__(self):
        """
        Inicializa el juego generando un número aleatorio y configurando los intentos.
        """
        self.numero_secreto = random.randint(1, 100)  # Genera un número secreto entre 1 y 100.
        self.intentos = 0  # Lleva un conteo de los intentos realizados.

    def validar_numero(self, numero: int) -> str:
        """
        Valida si el número ingresado por el jugador es mayor, menor o igual al número secreto.

        Args:
            numero (int): Número ingresado por el jugador.

        Returns:
            str: Mensaje indicando el resultado de la validación.
        """
        if numero < self.numero_secreto:
            return "El número es mayor."
        elif numero > self.numero_secreto:
            return "El número es menor."
        else:
            return "¡Correcto! Adivinaste el número."

    def registrar_intento(self):
        """
        Incrementa el contador de intentos realizados.
        """
        self.intentos += 1

    def reiniciar(self):
        """
        Reinicia el juego generando un nuevo número secreto y reseteando los intentos.
        """
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0


class Jugador:
    """
    Clase que representa a un jugador y su historial de partidas.
    """
    def __init__(self, nombre: str):
        """
        Inicializa al jugador con su nombre y un historial vacío.

        Args:
            nombre (str): Nombre del jugador.
        """
        self.nombre = nombre
        self.historial = []  # Lista para registrar el número de intentos y si ganó o no.

    def registrar_partida(self, intentos: int, gano: bool):
        """
        Registra los datos de una partida en el historial.

        Args:
            intentos (int): Número de intentos realizados en la partida.
            gano (bool): Indicador de si el jugador ganó o no.
        """
        self.historial.append((intentos, gano))

    def mostrar_estadisticas(self):
        """
        Muestra las estadísticas del jugador: porcentaje de aciertos y partidas jugadas.
        """
        partidas_jugadas = len(self.historial)
        partidas_ganadas = sum(1 for _, gano in self.historial if gano)
        porcentaje_ganadas = (partidas_ganadas / partidas_jugadas) * 100 if partidas_jugadas > 0 else 0

        print(f"\nEstadísticas de {self.nombre}:")
        print(f"- Partidas jugadas: {partidas_jugadas}")
        print(f"- Partidas ganadas: {partidas_ganadas}")
        print(f"- Porcentaje de victorias: {porcentaje_ganadas:.2f}%\n")


def cargar_datos() -> Jugador:
    """
    Carga los datos del jugador desde el archivo 'estadisticas.txt'.

    Returns:
        Jugador: Objeto con los datos cargados o un nuevo jugador si no hay datos disponibles.
    """
    archivo_datos = os.path.join(RUTA_ACTUAL, "estadisticas.txt")
    if os.path.exists(archivo_datos):
        with open(archivo_datos, "r") as archivo:
            nombre = archivo.readline().strip()
            historial = [tuple(map(int, linea.split(','))) for linea in archivo]
            jugador = Jugador(nombre)
            jugador.historial = historial
            return jugador
    return None


def guardar_datos(jugador: Jugador):
    """
    Guarda las estadísticas del jugador en el archivo 'estadisticas.txt'.

    Args:
        jugador (Jugador): Objeto con las estadísticas del jugador.
    """
    archivo_datos = os.path.join(RUTA_ACTUAL, "estadisticas.txt")
    with open(archivo_datos, "w") as archivo:
        archivo.write(f"{jugador.nombre}\n")
        for intentos, gano in jugador.historial:
            archivo.write(f"{intentos},{int(gano)}\n")
    print("\nDatos guardados correctamente.")


def interfaz():
    """
    Menú interactivo para jugar, ver estadísticas o salir.
    """
    jugador = cargar_datos()

    if not jugador:
        nombre = input("Ingresa tu nombre: ").strip()
        jugador = Jugador(nombre)

    while True:
        print("\nMenú:")
        print("1. Comenzar una nueva partida")
        print("2. Ver estadísticas")
        print("3. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            juego = JuegoAdivinanza()
            print("\n¡Adivina el número entre 1 y 100!")

            while True:
                try:
                    numero = int(input(f"Intento {juego.intentos + 1}: "))
                    juego.registrar_intento()
                    mensaje = juego.validar_numero(numero)
                    print(mensaje)

                    if mensaje == "¡Correcto! Adivinaste el número.":
                        jugador.registrar_partida(juego.intentos, True)
                        break

                except ValueError:
                    print("Por favor, ingresa un número válido.")

        elif opcion == "2":
            jugador.mostrar_estadisticas()

        elif opcion == "3":
            guardar_datos(jugador)
            print("Gracias por jugar. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    interfaz()
