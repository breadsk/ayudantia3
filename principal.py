from operaciones import menu,validar_no_vacio

peliculas = [
    {
        "nombre":"titanic",
        "año":"1998",
        "categoria":"drama",
        "reparto":["kate winslet","leonardo dicaprio","billy zane"]
    },
    {
        "nombre":"rocky",
        "año":"1976",
        "categoria":"romance",
        "reparto":["sylvester stallone","talia shire","carl weathers","burgess meredith"]        
    },
    {
        "nombre":"alien 2",
        "año":"1986",
        "categoria":"terror",
        "reparto":["sigourney weaver","carrie henn"]
    },
]

salir = False
while not salir:
    actores = []
    menu();
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Solo se permiten numeros en la opcion, intente nuevamente")
    else:
        if opcion == 1:
            nombre_pelicula_a_guardar = validar_no_vacio("Ingrese el nombre de la pelicula: ","nombre")                        
            año_pelicula_a_guardar = validar_no_vacio("Ingrese el año de la pelicula: ","año")        
            categoria_pelicula_a_guardar = validar_no_vacio("Ingrese la categoria de la pelicula: ","categoria")

            cantidad_actores = int(input("Ingrese la cantidad de actores que desea guardar: "))

            for cant in range(cantidad_actores):
                nombre_actor = input("Ingrese el actor: ").strip().lower()
                actores.append(nombre_actor)

            pelicula = {
                "nombre": nombre_pelicula_a_guardar,
                "año": año_pelicula_a_guardar,
                "categoria": categoria_pelicula_a_guardar,
                "reparto":actores
            }
            
            peliculas.append(pelicula)
            print("Pelicula guardada con exito!")
        elif opcion == 2:

            if not peliculas:
                print("No hay peliculas registradas")
                continue
            
            for posicion,pelicula in enumerate(peliculas,1):#Empezamos en 1 en la numneración
                #Formatear el reparto: unir los nombres con " , " y poner cada nombre en titulo
                reparto_formateado = ", ".join([actor.title() for actor in pelicula["reparto"]])

                print(f"{posicion}. {pelicula['nombre'].title()} ({pelicula['año']}) - {pelicula['categoria'].title()}")
                print(f" Reparto: {reparto_formateado}")

            
        elif opcion == 3:
            print("Buscar pelicula")
        elif opcion == 4:
             # EDITAR PELICULA
            if not peliculas:
                print("No hay peliculas registradas para editar")
                continue
            
            # Mostrar las peliculas con su índice
            print("\n--- LISTA DE PELICULAS ---")
            for posicion, pelicula in enumerate(peliculas, 1):
                print(f"{posicion}. {pelicula['nombre'].title()} ({pelicula['año']})")
            
            # Solicitar el índice de la película a editar
            try:
                indice = int(input("\nIngrese el numero de la pelicula que desea editar: "))
                if indice < 1 or indice > len(peliculas):
                    print("Numero de pelicula no valido")
                    continue
                
                # Obtener la pelicula a editar (ajustando índice)
                pelicula_a_editar = peliculas[indice - 1]
                
                print(f"\nEditando: {pelicula_a_editar['nombre'].title()}")
                print("Deje en blanco para mantener el valor actual")
                
                # Editar nombre
                nuevo_nombre = input(f"Nombre actual ({pelicula_a_editar['nombre']}): ")
                if nuevo_nombre.strip():  # Si no está vacío
                    pelicula_a_editar['nombre'] = nuevo_nombre.strip().lower()
                
                # Editar año
                nuevo_año = input(f"Año actual ({pelicula_a_editar['año']}): ")
                if nuevo_año.strip():
                    pelicula_a_editar['año'] = nuevo_año.strip()
                
                # Editar categoría
                nueva_categoria = input(f"Categoria actual ({pelicula_a_editar['categoria']}): ")
                if nueva_categoria.strip():
                    pelicula_a_editar['categoria'] = nueva_categoria.strip().lower()
                
                # Editar reparto
                print(f"\nReparto actual: {', '.join([actor.title() for actor in pelicula_a_editar['reparto']])}")
                opcion_reparto = input("¿Desea editar el reparto? (s/n): ").lower()
                
                if opcion_reparto == 's':
                    actores_editados = []
                    print("Ingrese los nuevos actores (escriba 'fin' para terminar):")
                    
                    while True:
                        actor = input("Actor: ")
                        if actor.lower() == 'fin':
                            break
                        if actor.strip():
                            actores_editados.append(actor.strip().lower())
                    
                    if actores_editados:  # Si se ingresaron actores
                        pelicula_a_editar['reparto'] = actores_editados
                        print("Reparto actualizado!")
                
                print(f"\n¡Pelicula '{pelicula_a_editar['nombre'].title()}' editada con exito!")
                
            except ValueError:
                print("Debe ingresar un numero valido")
        elif opcion == 5:
            salir = True
        else:
            print("Opcion no manejada, intente nuevamente")
    finally:
        print("Ejecutando...")

