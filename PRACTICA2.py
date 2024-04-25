peliculas_vistas = set()
recomendaciones = set()

while True:
    print("\nOpciones:")
    print("1. Añadir película vista")
    print("2. Añadir recomendación de película")
    print("3. Mostrar recomendaciones no vistas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        pelicula = input("Ingrese el título de la película vista: ").strip()
        peliculas_vistas.add(pelicula)
        print(f"Se ha añadido '{pelicula}' a las películas vistas.")
    elif opcion == '2':
        pelicula = input("Ingrese el título de la película recomendada: ").strip()
        recomendaciones.add(pelicula)
        print(f"Se ha añadido '{pelicula}' a las recomendaciones.")
    elif opcion == '3':
        no_vistas = recomendaciones.difference(peliculas_vistas)
        if no_vistas:
            print("Películas recomendadas que no has visto aún:")
            for pelicula in no_vistas:
                print(pelicula)
        else:
            print("No hay nuevas películas recomendadas para ver.")
    elif opcion == '4':
        print("Gracias por utilizar el gestor de películas.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 4.")
