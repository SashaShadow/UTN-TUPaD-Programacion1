import random

# Práctico 5: Listas
# 1) Crear una lista con las notas de 10 estudiantes.
# ● Mostrar la lista completa.
# ● Calcular y mostrar el promedio.
# ● Indicar la nota más alta y la más baja.

def notasfn():
    notas = [10,8,7,7,5,2,1,8,9,9.5]

    total = 0
    nota_mas_alta = 0
    nota_mas_baja = 0

    for i, note in enumerate(notas):
        if i == 0:
            nota_mas_alta = note 
            nota_mas_baja = note 
        else:
            if note > nota_mas_alta:
                nota_mas_alta = note

            if note < nota_mas_baja:
                nota_mas_baja = note 

        total += note 

    promedio = total / len(notas)

    print(f"Lista completa: {notas}")
    print(f"Promedio: {promedio}")
    print(f"Nota mas baja: {nota_mas_baja}")
    print(f"Nota mas alta: {nota_mas_alta}")

# 2) Pedir al usuario que cargue 5 productos en una lista.
# ● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# ● Preguntar al usuario qué producto desea eliminar y actualizar la lista.

def prods_lista():
    productos = []

    print("A continuacion debera ingresar 5 nombres de productos\n")

    for _ in range(5):
        prod = input("Ingrese por favor un producto:\n")

        while prod.strip() == "":
            prod = input("Ingrese por favor un producto (no puede estar vacio):\n")

        productos.append(prod)

    ordenados = sorted(productos)


    print("Lista actual ordenada alfabeticamente:\n")
    print(", ".join(ordenados))
    print("\n")

    print("¿Que producto desea eliminar?\n")

    prod_elim = input("Ingrese un producto a eliminar de la lista anterior:\n")

    if prod_elim in ordenados:
        ordenados.remove(prod_elim)

        print(f"Lista actualizada: {', '.join(ordenados)}")
    else:
        print("El producto ingresado no esta en la lista.")

# prods_lista()

# 3)​ Generar una lista con 15 números enteros al azar entre 1 y 100.
# ●​ Crear una lista con los pares y otra con los impares.
# ●​ Mostrar cuántos números tiene cada lista.

def lista_pimp():
    #Esto podria haberlo hecho con random y un range pero supuse que habia 
    #que escribirlo asi ya que no vimos random todavia (que recuerde)
    nums = [14, 22, 63, 1, 7, 8, 9, 16, 27, 43, 56, 77, 81, 99, 73]
    #sino seria:
    #nums = [random.randint(1, 100) for n in range(15)]
    print(nums)

    pares = []
    impares = []

    for num in nums:

        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print(f"La lista de numeros pares tiene {len(pares)} elementos\n")

    print(f"La lista de numeros impares tiene {len(impares)} elementos")

# lista_pimp()

# 4)​ Dada una lista con valores repetidos:
# ●​ Crear una nueva lista sin elementos repetidos.
# ●​ Mostrar el resultado.

def repetidos():
    lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]

    lista_sin_repetir = []

    for n in lista: 
        if n not in lista_sin_repetir:
            lista_sin_repetir.append(n)

    print("Lista de numeros sin repetir:\n")

    print(lista_sin_repetir)

# repetidos()

# 5)​ Crear una lista con los nombres de 8 estudiantes presentes en clase.
# ●​ Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# ●​ Mostrar la lista final actualizada.

def lista_estudiantes():

    lista_est = ["Maria", "Pedro", "Matias", "Sasha", "Giselle", "Paloma", "Margarita", "Rebeca"]

    print(f"Lista de estudiantes: {', '.join(lista_est)}\n")

    texto_opc = """
    1. Agregar un nuevo estudiante.
    2. Eliminar un estudiante de la lista.
    """

    estudiante_opc = input(f"Ingrese 1 o 2 segun lo que desea realizar: \n {texto_opc}")

    while estudiante_opc not in ["1", "2"]:
        estudiante_opc = input(f"Por favor ingrese 1 o 2 segun lo que desea realizar: \n {texto_opc}")

    mensaje = "agregar" if estudiante_opc == "1" else "eliminar"

    estudiante = input(f"Ingrese el estudiante que desea {mensaje}:\n") 

    if estudiante_opc == "2" and estudiante not in lista_est:
        print("El estudiante no se encuentra en la lista")
        return 

    if estudiante_opc == "2":
        lista_est.remove(estudiante)
    else:
        lista_est.append(estudiante)

    print(f"Lista actualizada: {', '.join(lista_est)}")

# lista_estudiantes()

# 6)​ Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
# (el último pasa a ser el primero).

def rotacion_siete_nums():

    lis = [1, 5, 55, 77, 43, 42, 37]

    ultimo_valor = lis[-1]

    for i in range(len(lis) - 2, -1, -1):
        lis[i + 1] = lis[i]

    lis[0] = ultimo_valor 

    print(f"Lista actualizada: {lis}")

# rotacion_siete_nums()

# 7)​ Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de
# una semana.
# ●​ Calcular el promedio de las mínimas y el de las máximas.
# ●​ Mostrar en qué día se registró la mayor amplitud térmica.

def temperaturas():

    matriz = [[2,15], [3, 15], [1,12], [0, 9], [6,17], [5,18], [3,8]]

    total_minimas = 0
    total_maximas = 0
    mayor_amplitud_list = [None, []]

    for i, elem in enumerate(matriz): 
        total_minimas += elem[0]
        total_maximas += elem[1]

        amplitud = elem[1] - elem [0]

        if None in mayor_amplitud_list:
            mayor_amplitud_list[0] = amplitud
            mayor_amplitud_list[1] = [i]
        else: 
            if amplitud > mayor_amplitud_list[0]:
                mayor_amplitud_list[0] = amplitud
                mayor_amplitud_list[1] = [i]
            elif amplitud == mayor_amplitud_list[0]:
                mayor_amplitud_list[1].append(i)

    print(f"Promedio de las temperaturas minimas: {total_minimas / 7}")
    print(f"Promedio de las temperaturas maximas: {total_maximas / 7}\n")

    print(f"Dia/s con mayor amplitud registrada: {mayor_amplitud_list[1]}")

# temperaturas()

# 8)​ Crear una matriz con las notas de 5 estudiantes en 3 materias.
# ●​ Mostrar el promedio de cada estudiante.
# ●​ Mostrar el promedio de cada materia.

def notas_materias():
    nombres_estudiantes = ["Matias", "Sasha", "Jesus", "Maria", "Ramona"]
    matriz_notas = [[6, 6, 6], [8, 7, 8], [7, 7, 7], [9, 5, 9], [10, 7, 10]]

    total_mate = 0
    total_geo = 0
    total_ed_fisica = 0

    for i ,estudiante in enumerate(matriz_notas):
        total_estudiante = 0 

        for j, nota in enumerate(estudiante):
            total_estudiante += nota

            if j == 0:
                total_mate += nota 
            elif j == 1:
                total_geo += nota 
            else:
                total_ed_fisica += nota 

        print(f"Promedio de notas de {nombres_estudiantes[i]}: {total_estudiante / 3:.2f}\n")

    print(f"Promedio de notas para matematica: {total_mate / 5}\n")
    print(f"Promedio de notas para geografia: {total_geo / 5}\n")
    print(f"Promedio de notas para educacion fisica: {total_ed_fisica / 5}\n")

# notas_materias()

# 9)​ Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# ●​ Inicializarlo con guiones "-" representando casillas vacías.
# ●​ Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# ●​ Mostrar el tablero después de cada jugada.

# Quizas la consigna no pedia algo asi pero creo que la cumple y supera llegando a ser el juego completo
def aux_tateti(marcas_ganadoras, marcas_X, marcas_O):
    marca_ganadora = None

    for marca in marcas_ganadoras:
        tiene_todas_x = 0
        tiene_todas_o = 0
        for posicion in marca:
            if posicion in marcas_X:
                tiene_todas_x += 1
            if posicion in marcas_O:
                tiene_todas_o += 1

        if tiene_todas_o == 3 or tiene_todas_x == 3:
            marca_ganadora = "X" if tiene_todas_x == 3 else "O"
            break

    if marca_ganadora:
        print(f"Juego terminado. Se realizo una linea de {marca_ganadora}/s")
        return True

    return False

def tateti():
    tablero = [["-", "-", "-"],
               ["-", "-", "-"],
               ["-", "-", "-"]]
    
    turno = True

    marcas_ganadoras = [["0,0", "1,1", "2,2"],["0,0","1,0","2,0"],
                        ["0,1", "1,1", "2,1"], ["0,2", "1,2", "2,2"],
                        ["0,2", "1,1", "2,0"], ["0,0", "0,1", "0,2"],
                        ["1,0", "1,1", "1,2"],["2,0", "2,1", "2,2"]]

    marcas_X = []

    marcas_O = []

    while "-" in tablero[0] or "-" in tablero[1] or "-" in tablero[2]:

        print(f"Marcas X: {marcas_X}\n")
        print(f"Marcas O: {marcas_O}\n")

        nombre_jugador = "1" if turno else "2"
        marca_jugador = "X" if turno else "O"

        for f in tablero:
            print(f)

        fin = aux_tateti(marcas_ganadoras=marcas_ganadoras, marcas_O=marcas_O, marcas_X=marcas_X)

        if fin:
            return

        valor_encontrado = 0

        while valor_encontrado != "-":
            fila = input(f"Jugador {nombre_jugador} elija fila para marcar {marca_jugador}, (opciones posibles: 1, 2 o 3):\n")
            
            while fila not in ["1", "2", "3"]:
                fila = input(f"Jugador {nombre_jugador} elija fila correcta para marcar {marca_jugador}, (opciones posibles: 1, 2 o 3):\n")
    
            columna = input(f"Jugador {nombre_jugador} elija columna para marcar {marca_jugador}, (opciones posibles: 1, 2 o 3):\n")
    
            while columna not in ["1", "2", "3"]:
                columna = input(f"Jugador {nombre_jugador} elija columna correcta para marcar {marca_jugador}, (opciones posibles: 1, 2 o 3):\n")
                    
            valor_encontrado = tablero[int(fila) - 1][int(columna) - 1]

            if valor_encontrado != "-":
                print(f"En esa posicion ya hay un {valor_encontrado} marcado. Elija otra posicion. \n")
            else:
                tablero[int(fila) - 1][int(columna) - 1] = marca_jugador

                if marca_jugador == "X":
                    marcas_X.append(f"{int(fila) - 1},{int(columna) - 1}")
                else:
                    marcas_O.append(f"{int(fila) - 1},{int(columna) - 1}")

                valor_encontrado = "-"
                turno = not turno

    for f in tablero:
        print(f)

    fin = aux_tateti(marcas_ganadoras=marcas_ganadoras, marcas_O=marcas_O, marcas_X=marcas_X)

    if not fin:
        print("¡Empate!\n")

# tateti()

# 10)​Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# ●​ Mostrar el total vendido por cada producto.
# ●​ Mostrar el día con mayores ventas totales.
# ●​ Indicar cuál fue el producto más vendido en la semana.

def tienda():
    matriz_productos = [
        #Arroz
        [5, 6, 7, 8, 9, 4, 2],
        #Fideos
        [10, 5, 5, 5, 7, 7, 9],
        #Leche
        [2, 2, 3, 3, 4, 4, 7],
        #Huevos
        [1, 1, 2, 1, 5, 6, 5]
    ]

    productos = ["Arroz", "Fideos", "Leche", "Huevos"]
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    producto_mas_vendido = None 

    for i, producto in enumerate(matriz_productos):
        total_producto = 0 

        for dia in producto:
            total_producto += dia 

        if producto_mas_vendido is None:
            producto_mas_vendido = [i, total_producto]
        else:
            if total_producto > producto_mas_vendido[1]:
                producto_mas_vendido = [i, total_producto]

        print(f"Total de ventas en la semana para {productos[i]}: {total_producto}\n")     

    ventas_dias = []

    for j in range(7):
        total_dia = 0

        for p in matriz_productos:
            total_dia += p[j]

        ventas_dias.append(total_dia)

    maxima_venta = max(ventas_dias)

    dia_con_mayor_venta = ventas_dias.index(maxima_venta)

    print(f"Dia con mayores ventas: {dias[dia_con_mayor_venta]}")

    print(f"Producto mas vendido: {productos[producto_mas_vendido[0]]} con {producto_mas_vendido[1]} unidades vendidas")  

# tienda() 
        



    