import random

puntuaciones = []



def menu_principal():
    print("Bienvenido al juego de adivinar el número secreto")
    print("1. Nivel fácil, 0-100") 
    print("2. Nivel intermedio, 0-1000") 
    print("3. Nivel avanzado, 0-1000000")  
    print("4. Nivel experto, 0-1000000000000")

def jugar(numero_secreto,intentos):
    while intentos > 0:
        try:
          numero_jugador = int(input("Ingresa tu número"))
        except ValueError:
            print("Por favor, ingresa un número válido")
            continue
        
        if numero_jugador == numero_secreto:
            print ("Felicidades,",numero_secreto,"Era el número que estaba pensando")
            return
        elif numero_jugador > numero_secreto:
            print("Te pasaste, prueba un número más pequeño")
        else:
            print("Te quedaste corto, le número que estoy pensanso es mayor")
        intentos -=1 
        print("Te quedan",intentos,"intentos")

    print("NOOOOOO, te has quedado sin intentos, lo siento")
    def guardar_puntuaciones(intentos):
      nombre_jugador = int(input("Por favor ingrese su nombre"))
      puntuaciones.append((nombre_jugador,intentos))

    def tabla_de_puntuaciones():
        print("Estas son las mejores puntuaciones")
        for i, (nombre, puntuacion) in enumerate (puntuaciones, start=1):
            print(f"{i} {nombre}:{puntuacion} intentos")


    

def juego():
    while True:
        menu_principal()
        opcion = int(input("Selecciona una dificultad entre 1 y 4:"))
        if opcion == 1:
            numero_secreto = random.randint(0,100)
            intentos = 10
            jugar(numero_secreto,intentos)
        elif opcion == 2:
            numero_secreto = random.randint(0,1000)
            intentos = 15
            jugar(numero_secreto,intentos)
        elif opcion == 3:
            numero_secreto = random.randint(0,1000000)
            intentos = 30
            jugar(numero_secreto,intentos)
        elif opcion == 4:
            numero_secreto = random.randint(0,1000000000000)
            intentos = 60
            jugar(numero_secreto,intentos)
            break     
        else:
            print("Opción no válida")
if __name__ == "__main__":
    juego()  


