import random

def es_vocal(letra):
    # estan en lowercase pero por si acaso contempla otros casos
    vocales = "aeiouAEIOU"
    return letra in vocales
 
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", 
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")

# Asignacion de las dificultades
dificultades = ["facil", "media", "dificil"]

# Hasta que no se ingrese el tipo de dato correcto no para de preguntar
while True:
    # Ingresa la dificultad, Checkea si esta en el rango de las dificultades disponibles
    dificultad = input("Ingrese la dificultad deseada, facil, media o dificil: ").lower()

    if dificultad not in dificultades:
        print("El valor ingresado no corresponde con lo pedido \n")
    else:
        break

# Empieza con word_displayed = "" para poder ir agregandole dependiendo de cada caso
word_displayed = ""
if dificultad == dificultades[0]:
    for letra in secret_word:
        if es_vocal(letra):
            word_displayed += letra
        else:
            word_displayed += "_"

elif dificultad == dificultades[1]:
    # primer letra mas las letras del medio mas la ultima letra
    word_displayed += secret_word[0] + ((len(secret_word) - 2) * "_") + secret_word[-1] 

else:
    word_displayed += "_" * len(secret_word)
        
# word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada

print(f"Dificultad: {dificultad}. Comienza el juego. \n Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Palabra: {word_displayed} \n")

i = 0
while i < max_attempts:
#for i in range(max_attempts):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    if letter == "":
        print("Ingresa un caracter valido")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        i += 1

    # Mostrar la palabra parcialmente adivinada 
    letters = []
    for i in range(len(secret_word)):

        if secret_word[i] in guessed_letters or word_displayed[i] != "_":
            letters.append(secret_word[i])
        else:
            letters.append("_")
            
    word_displayed = "".join(letters)


    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break

else: #entra en el else cuando i llega al limite
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")