"""
1. Cargar Vehículos
● Permitir ingresar la cantidad de vehículos a cargar.
● Guardar los datos en el array bidimensional.
2. Mostrar Lista Completa
● Mostrar todos los vehículos con sus datos, uno por línea o en formato tabla.
3. Buscar Vehículo por Patente
● Solicitar la patente al usuario.
● Si se encuentra, mostrar todos sus datos.
● Si no, mostrar “Vehículo no encontrado”.
4. Ordenar Vehículos por Año (Descendente)
● Implementar un algoritmo de ordenamiento a elección (sin usar funciones integradas tipo sorted()).
5. Vehículo con Más Horas Estacionado
● Calcular y mostrar los datos del vehículo con mayor cantidad de horas estacionado.
6. Vehículo con Menos Horas Estacionado
● Calcular y mostrar los datos del vehículo con menor cantidad de horas estacionado.
7. Cantidad de Vehículos con Más de 4 Horas Estacionados
● Recorrer el arreglo y contar cuántos cumplen esta condición.
8. Promedio de Horas Estacionadas
● Calcular el promedio de horas de todos los vehículos ingresados.
9. Cantidad de Vehículos con Marca “Ford”
● Contar cuántos vehículos tienen como marca "Ford".
"""


def cargar_vechiculo(matriz, dato1, dato2, dato3, dato4, dato5):
    """
    Funcion que agrega 5 elementos en formato lista a una matriz
    Args:
        Matriz: objeto de tipo list que recibe una matriz dada
        dato1, dato2.. dato3: datos que recibe la funcion que luega seran sumadas la matriz
    """
    lista = [dato1, dato2, dato3, dato4, dato5]
    for i in range(len(matriz)):
        matriz[-1:] += [lista]
    return matriz

def mostrar_lista_vehiculos(matriz):
    """
    Funcion que imprime cada valor de la matriz a traves del indice
    Args:
        matriz:
    """
    for i in range(len(matriz)):
        print(matriz[i])

def buscar_por_patente(matriz, patente):
    """
    Funcion que filtra una lista dentro de una matriz a traves de un argumento de tipo entero
    Args:
        matriz: matriz de datos donde filtraremos la lista
        patente: argumento de tipo string que compara cada valor hasta encontrar el coincidente 
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][0] == patente:
                return matriz[i]
            else:
                return "Vehiculo no encontrado"
            
#def ordenar_por_anio(matriz):
#   n = len(matriz)
#   for i in range(n - 1):
#       for j in range(n - 1 - i):
#           if matriz[i][j] > matriz[i][j + 1]:
#               aux = matriz[i][j]
#               matriz[i][j] = matriz[i][j + 1]
#               matriz[i][j + 1] = aux

def buscar_por_hora_maxima(matriz):
    """
    Funcion que filtra a partir de un numero maximo
    Args:
        Matriz: Matriz que utilizamos para encontrar los datos deseados
    """
    maximo = matriz[0][4]
    for i in range(len(matriz)):
        for j in range(1, len(matriz[i])):
            if matriz[i][4] > maximo:
                maximo = matriz[i][4]
    return maximo

def buscar_por_hora_minima(matriz):
    """
    Funcion que filtra a partir de un numero minimo
    Args:
        Matriz: Matriz que utilizamos para encontrar los datos deseados
    """
    minimo = matriz[0][4]
    for i in range(len(matriz)):
        for j in range(1, len(matriz[i])):
            if matriz[i][4] < minimo:
                minimo = matriz[i][4]
    return minimo

def vehiculo_mas_cuatro_horas(matriz):
    """
    Funcion que filtra dentro de una matriz los elementos mayores a 4
    Args: Matriz que utilizamos para encontrar los datos deseados
    """
    contador = 0
    for i in range(len(matriz)):
        for j in range(4, len(matriz[i])):
            if matriz[i][4] > 4:
                contador += 1
    return contador

def calcular_promedio_estacionamiento(matriz):
    cantidad = len(matriz) + 1
    suma = 0
    promedio = (suma / cantidad)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][4]
    return promedio

def cantidad_vehiculos_ford(matriz):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i]), 6):
            if matriz[i][1] == "Ford":
                contador += 1
    return contador
    

    


