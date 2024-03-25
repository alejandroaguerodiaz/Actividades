import funciones

def main():
    dbz = [("Dragon Ball: La leyenda de Shenron", 50), 
        ("Dragon Ball Z: Los guerreros de plata", 48),
        ("Dragon Ball Z: La batalla de los dioses", 85),
        ("Dragon Ball Z: La resurrección de Freezer", 93),
        ("Dragon Ball Super: Broly", 100)]
    promedio = funciones.promedio(dbz)

    mayores_al_promedio = funciones.mayor_al_promedio(dbz, promedio)

    print(f"La duracion promedio de las pelis es de: {promedio} Y la cantidad de peliculas que duran mas que el promedio son: {mayores_al_promedio}")

if __name__ == "__main__":
    main()



