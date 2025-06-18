def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contactos")
    print("2. Editar contacto existente")
    print("3. Eliminar contacto existente")
    print("4. Buscar contacto")
    print("5. Lista de contactos")
    print("6. Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor introduzca el telefono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")
    agenda[nombre] = {"telefono":telefono, "email":email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def editar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea editar: ")
    if agenda:
        if nombre in agenda:
            nombre_nuevo = input("Introduzca el nuevo nombre del contacto: ")
            telefono_nuevo = input("Introduzca el nuevo telefono del contacto: ")
            email_nuevo = input("Introduzca el nuevo email del contacto: ")
            if nombre_nuevo and telefono_nuevo and email_nuevo:
                agenda[nombre_nuevo] = agenda.pop(nombre)
                nombre = nombre_nuevo
                agenda[nombre]["telefono"] = telefono_nuevo
                agenda[nombre]["email"] = email_nuevo
            print("El contacto ha sido actualizado correctamente")
    else:
        print(f"El contacto {nombre} no esta en la agenda")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de nombre {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos:")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda esta vacia")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opcion: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            editar_contacto(agenda)
        elif opcion == "3":
            eliminar_contacto(agenda)
        elif opcion == "4":
            buscar_contacto(agenda)
        elif opcion == "5":
            listar_contactos(agenda)
        elif opcion == "6":
            print("Saliendo de la agenda de contactos ¡Hasta luego!")
            break
        else:
            print("Por favor seleccione una opcion valida (del 1 al 6)")

agenda_contactos()
