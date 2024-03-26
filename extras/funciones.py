
def promedio(pelis):
    """ Ingresa una lista donde el segundo indice sea tipo numero y calcula el promedio de la lista """
    promedio = 0
    for peli in pelis:
        promedio += peli[1] #En el indice 1 estaria la duracion
    promedio /= len(pelis)
    return promedio

def mayor_al_promedio(pelis, promedio):
    """ Recibe una lista donde el segundo indice sea tupo numero y un promedio, con eso, calcula cuantas peliculas son mayores al promedi """
    mayores = 0
    for peli in pelis:
        if peli[1] > promedio:
            mayores += 1
    return mayores
    

if __name__ == "__main__":
    print("Este modulo no posee una ejecucion principal")