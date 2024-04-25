tareas_pendientes = []
tareas_completadas = []

while True:
    print("\nOpciones:")
    print("1. Añadir tarea")
    print("2. Completar tarea")
    print("3. Mostrar tareas pendientes")
    print("4. Mostrar tareas completadas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        tarea = input("Ingrese la descripción de la tarea: ").strip()
        tareas_pendientes.append(tarea)
        print(f"Se ha añadido '{tarea}' a las tareas pendientes.")
    elif opcion == '2':
        if tareas_pendientes:
            for index, tarea in enumerate(tareas_pendientes, start=1):
                print(f"{index}. {tarea}")
            seleccion = int(
                input("Seleccione el número de la tarea a completar: "))
            if 1 <= seleccion <= len(tareas_pendientes):
                tarea_completada = tareas_pendientes.pop(seleccion - 1)
                tareas_completadas.append(tarea_completada)
                print(f"La tarea '{tarea_completada}' ha sido completada.")
            else:
                print("Selección inválida.")
        else:
            print("No hay tareas pendientes.")
    elif opcion == '3':
        if tareas_pendientes:
            print("Tareas pendientes:")
            for tarea in tareas_pendientes:
                print(tarea)
        else:
            print("No hay tareas pendientes.")
    elif opcion == '4':
        if tareas_completadas:
            print("Tareas completadas:")
            for tarea in tareas_completadas:
                print(tarea)
        else:
            print("No hay tareas completadas.")
    elif opcion == '5':
        print("Gracias por utilizar el gestor de tareas.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 5.")
