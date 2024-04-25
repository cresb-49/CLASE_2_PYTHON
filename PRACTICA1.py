# Diccionario para almacenar los libros y una breve descripción
libros = {}

while True:
    print("\nOpciones:")
    print("1. Añadir libro")
    print("2. Buscar libro")
    print("3. Ver todos los libros")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            # Añadir libro
            titulo = input("Ingrese el título del libro: ").strip()
            descripcion = input(
                "Ingrese una breve descripción del libro: ").strip()
            libros[titulo] = descripcion
            print(f"Libro '{titulo}' añadido con éxito.")
        elif opcion == 2:
            # Buscar libro
            titulo = input("Ingrese el título del libro que busca: ").strip()
            if titulo in libros:
                print(f"Libro encontrado: {titulo}")
                print(f"Descripción: {libros[titulo]}")
            else:
                print("El libro no está disponible.")
        elif opcion == 3:
            # Ver todos los libros
            if libros:
                print("Libros disponibles en la librería:")
                for titulo, descripcion in libros.items():
                    print(f"{titulo}: {descripcion}")
            else:
                print("No hay libros disponibles.")
        elif opcion == 4:
            print("Gracias por utilizar el sistema de librería.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")
    except ValueError:
        print("Por favor, introduzca un número válido.")
