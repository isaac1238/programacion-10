import random
import os

# Determina la ubicación del script actual para guardar los archivos generados en el mismo directorio.
RUTA_ACTUAL = os.path.dirname(os.path.abspath(__file__))

class AdivinaNumero:
    """
    Clase que representa el juego de adivinar un número.
    """
    def __init__(self):
        """
        Inicializa el juego generando un número aleatorio y configurando los intentos permitidos.
        """
        self.num_secreto = random.randint(1, 100)  # Genera un número secreto entre 1 y 100.
        self.intentos_realizados = 0  # Cuenta los intentos realizados por el jugador.
        self.max_intentos = 10  # Define un límite máximo de intentos.

    def verificarNumero(self, numero):
        """
        Comprueba si el número ingresado es mayor, menor o igual al número secreto.

        Args:
            numero (int): Número proporcionado por el usuario.

        Returns:
            str: Mensaje indicando el estado de la comparación.
        """
        self.intentos_realizados += 1  # Incrementa el contador de intentos.
        if numero < self.num_secreto:
            return "El número es mayor."
        elif numero > self.num_secreto:
            return "El número es menor."
        else:
            return "¡Correcto! Adivinaste el número."

    def limiteAlcanzado(self):
        """
        Comprueba si se han agotado los intentos permitidos.

        Returns:
            bool: True si no quedan más intentos, de lo contrario False.
        """
        return self.intentos_realizados >= self.max_intentos

    def reiniciarJuego(self):
        """
        Reinicia el juego generando un nuevo número y reseteando el contador de intentos.
        """
        self.num_secreto = random.randint(1, 100)
        self.intentos_realizados = 0


class Usuario:
    """
    Clase que gestiona al usuario y su historial de partidas.
    """
    def __init__(self, nombre):
        """
        Constructor para inicializar el jugador y su registro de partidas.

        Args:
            nombre (str): Nombre del jugador.
        """
        self.nombre = nombre
        self.historial = []  # Lista que almacena los intentos y resultados de cada partida.

    def guardarPartida(self, intentos, exito):
        """
        Registra una partida en el historial del usuario.

        Args:
            intentos (int): Cantidad de intentos realizados.
            exito (bool): Indica si la partida fue ganada.
        """
        self.historial.append((intentos, exito))

    def verEstadisticas(self):
        """
        Muestra las estadísticas generales del usuario.
        """
        total_partidas = len(self.historial)
        partidas_ganadas = sum(1 for _, gano in self.historial if gano)
        porcentaje_ganadas = (partidas_ganadas / total_partidas) * 100 if total_partidas > 0 else 0

        print(f"\nEstadísticas de {self.nombre}:")
        print(f"- Total de partidas: {total_partidas}")
        print(f"- Partidas ganadas: {partidas_ganadas}")
        print(f"- Porcentaje de victorias: {porcentaje_ganadas:.2f}%\n")


def cargarDatos():
    """
    Carga los datos del jugador desde el archivo 'datos.txt'.

    Returns:
        Usuario: Objeto con los datos cargados o None si no hay datos disponibles.
    """
    archivo_datos = os.path.join(RUTA_ACTUAL, "datos.txt")
    if os.path.exists(archivo_datos):
        with open(archivo_datos, "r") as archivo:
            nombre = archivo.readline().strip()
            partidas = [tuple(map(int, linea.split(','))) for linea in archivo]
            jugador = Usuario(nombre)
            jugador.historial = partidas
            return jugador
    return None


def guardarDatos(usuario):
    """
    Guarda los datos del jugador en el archivo 'datos.txt'.

    Args:
        usuario (Usuario): Objeto con los datos del jugador.
    """
    try:
        archivo_datos = os.path.join(RUTA_ACTUAL, "datos.txt")
        with open(archivo_datos, "w") as archivo:
            archivo.write(f"{usuario.nombre}\n")
            for intentos, exito in usuario.historial:
                archivo.write(f"{intentos},{int(exito)}\n")
        print("\nDatos guardados correctamente.")
    except Exception as error:
        print(f"\nError al guardar los datos: {error}")


def interfaz():
    """
    Proporciona el menú interactivo para jugar, ver estadísticas o salir.
    """
    jugador = cargarDatos()

    if not jugador:
        nombre = input("Ingresa tu nombre: ").strip()
        jugador = Usuario(nombre)

    while True:
        print("\nMenú:")
        print("1. Jugar una partida")
        print("2. Ver estadísticas")
        print("3. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            juego = AdivinaNumero()
            print("\n¡Adivina el número entre 1 y 100! Tienes 10 intentos.")

            while True:
                try:
                    numero = int(input(f"Intento {juego.intentos_realizados + 1}/10: "))
                    mensaje = juego.verificarNumero(numero)
                    print(mensaje)

                    if mensaje == "¡Correcto! Adivinaste el número.":
                        jugador.guardarPartida(juego.intentos_realizados, True)
                        break

                    if juego.limiteAlcanzado():
                        print(f"¡Intentos agotados! El número era {juego.num_secreto}.")
                        jugador.guardarPartida(juego.intentos_realizados, False)
                        break

                except ValueError:
                    print("Por favor, ingresa un número válido.")

        elif opcion == "2":
            jugador.verEstadisticas()

        elif opcion == "3":
            guardarDatos(jugador)
            print("Gracias por jugar. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    interfaz()
