import random

numero_secreto = random.randint(
    1, 101
)  # creamos una variable con numeros aleatoriosNo toma el 101
adivinado = (
    False  # declaramos la variale inicial en false, si la persona logra adivinar
)
cantidad_intentos = 0
cantidad_maxima_intentos = 3

print("Bienvenido al juego de adivinar el número secreto")

while (
    not adivinado and cantidad_intentos < cantidad_maxima_intentos
):  # Mientras no adivines el número, oséa que 'adivinado = false', se repite el bucle hasta que  'adivinado = True'
    numero_entrada = input("Introduce un número del 1 al 100: ")
    numero = int(numero_entrada)
    if numero == numero_secreto:
        print("Felicitaciones, Ganaste")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    cantidad_intentos += 1

if not cantidad_intentos < cantidad_maxima_intentos:
    print("Game Over¡ No has podido adivinar el número")
