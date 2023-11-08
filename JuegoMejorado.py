import random


numerito = random.randint(0, 99)
intentos = 0

while True:
        numerito2 = int(input("Intenta adivinar el número (entre 0 y 99): "))
        intentos = intentos + 1

        if numerito2 < numerito:
            print("Te quedaste corto. ¡Intenta con un número más grande!")
        elif numerito2 > numerito:
            print("Te pasaste. Intenta con un número más pequeño.")
        else:
            print(f"¡Felicitaciones! ¡Has adivinado el número en {intentos} intentos!")
            break