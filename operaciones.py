

def menu():#void
    print("######Peliculas######")
    print("1. Guardar pelicula")
    print("2. Mostrar peliculas")
    print("3. Buscar pelicula")
    print("4. Editar pelicula")
    print("4. Salir")

def validar_no_vacio(mensaje,valor_validado):#return
    while True:
        dato = input(mensaje).strip().lower()
        if dato == "":
            print(f"No se permiten valores vacios ('{valor_validado}') , intente nuevamente")
        else:
            return dato
