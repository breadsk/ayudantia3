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

            # for cant i in range(cantidad_actores):
            #     #

            pelicula = {
                "nombre": nombre_pelicula_a_guardar,
                "año": año_pelicula_a_guardar,
                "categoria": categoria_pelicula_a_guardar
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
            salir = True
        else:
            print("Opcion no manejada, intente nuevamente")
    finally:
        print("Ejecutando...")

