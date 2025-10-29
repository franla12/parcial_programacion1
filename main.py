from funciones import *
mensaje_menu = """--------- Estacionamiento parking center ---------\n 1- Cargar vehiculo\n 2- Mostrar Lista completa\n 3- Buscar vehiculo por patente\n 4- Ordenar vehiculo por año\n 5- Vehiculo con mas horas de estacionamiento\n 6- Vehiculo con menos horas estacionadas\n 7- Cantidad de vehiculos con mas de 4 horas estacionadas\n 8- Promedio de horas estacionadas \n 9-Cantidad de vehiculos con la marca "Ford"\n 0- Salir del sistema\n Ingrese una opcion:  """
vehiculos = [[]]

menu = True

while menu:
    opciones = input(mensaje_menu)
    match opciones:
        case "1":
            patente = input("Ingrese el numero de la patente: ")
            marca = input("Ingrese la marca del vehiculo: ") 
            modelo = input("Ingrese el modelo del vehiculo: ")
            anio = int(input("Ingrese el año del vehiculo: "))
            horas = int(input("Ingrese las horas estacionadas"))
            cargar_vechiculo(vehiculos, patente, marca, modelo, anio, horas)
        case "2":
            mostrar_lista_vehiculos(vehiculos)
        case "3":
            patente_consulta = input("Ingrese el numero de patente que esta buscando..")
            buscar_por_patente(vehiculos, patente_consulta)
        case "4":
            pass
        case "5":
            print(f"Vehiculo con mas horas de estacionamiento: {buscar_por_hora_maxima(vehiculos)}")
        case "6":
            print(f"Vehiculo con menos horas de estacionamiento: {buscar_por_hora_minima(vehiculos)}")
        case "7":
            print(f"Vehiculos con mas horas de 4 hs de estacionamiento: {vehiculo_mas_cuatro_horas(vehiculos)}")
        case "8":
            print(f"El promedio de horas estacionadas es: {calcular_promedio_estacionamiento(vehiculos)}")
        case "9":
            print(f"Cantidad de vehiculos marca fort: {cantidad_vehiculos_ford(vehiculos)}")
        case "0":
            menu = False
        case _:
            print("Error. Ingrese una opción correcta")