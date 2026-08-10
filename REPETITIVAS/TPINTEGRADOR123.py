# Ejercicio 1— “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total.

def caja_kiosco():
    total_descuento = 0
    total_sin_descuento = 0
    ahorro_total = 0
    productos_info = []

    nombre_cliente = input("Ingrese nombre del cliente: \n")

    if nombre_cliente == "":
        print("El nombre del cliente no puede estar vacio\n")
        nombre_cliente = input("Ingrese nombre del cliente: \n")

    while not nombre_cliente.isalpha():
        print("El nombre de cliente no puede tener numeros ni signos\n")
        nombre_cliente = input("Ingrese nombre del cliente: \n")

    cantidad = input("Ingrese la cantidad de productos a comprar: \n")

    while not cantidad.isdigit() or int(cantidad) <= 0:
        print("Se debe elegir una cantidad valida (numero entero mayor a 0)\n")
        cantidad = input("Ingrese la cantidad de productos a comprar: \n")

    for n in range(1, int(cantidad) + 1):
        precio = input(f"Ingrese precio del producto {n}: \n")

        while not precio.isdigit() or int(precio) <= 0:
            precio = input(f"Ingrese un numero valido para el precio del producto {n}\n: ")

        precio = int(precio)

        tiene_descuento = input(f"¿El producto {n} tiene descuento? (Ingrese S para si, N para no)\n ")

        while tiene_descuento.lower() != "s" and tiene_descuento.lower() != "n":
            tiene_descuento = input(f"Por favor ingrese una opcion valida (S o N). \n ¿El producto {n} tiene descuento? (Ingrese S para si, N para no) ")

        descuento = precio * 10 / 100 if tiene_descuento.lower() == "s" else 0
        precio_con_descuento = precio - descuento

        total_descuento += precio_con_descuento
        total_sin_descuento += precio
        ahorro_total += descuento

        productos_info.append(f"Producto {n} - Precio: {precio} - Descuento (S/N): {tiene_descuento}")

    promedio_descuento = ahorro_total / int(cantidad)

    print(f"Cliente: {nombre_cliente}")
    print(f"Cantidad de productos: {cantidad}\n")

    for prod_msg in productos_info:
        print(prod_msg)

    print(f"Total sin descuentos: {total_sin_descuento}")
    print(f"Total con descuentos: {total_descuento}")
    print(f"Ahorro: {ahorro_total}")
    print(f"Promedio por producto: {promedio_descuento}")

    
# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.

def login_campus():
    user = "root"
    password = "supersecret123"

    intentos = 0
    MAX_INTENTOS = 3

    while intentos < MAX_INTENTOS:
        user_ingreso = input("Ingrese nombre usuario: \n")
        pass_ingreso = input("Ingrese contraseña: \n")

        intentos += 1

        if user != user_ingreso or password != pass_ingreso:
            if intentos == MAX_INTENTOS:
                print("Cuenta bloqueada")
                return 
            print("Error: Usuario o contraseña invalidos.\n")
            continue 

        print("Acceso concedido\n")
        break

    opcion_elegida = 0

    texto_opc = """
        1. Ver estado de inscripción.
        2. Cambiar clave.
        3. Mostrar mensaje motivacional.
        4. Salir.
    """

    while opcion_elegida != "4":
        opcion_elegida = input(f"Ingrese una opcion: \n {texto_opc}")

        while not opcion_elegida.isdigit() or int(opcion_elegida) < 1 or int(opcion_elegida) > 4:
            print("Error: Por favor elegir una opcion valida")
            opcion_elegida = input(f"Ingrese una opcion: \n {texto_opc}\n")

        if opcion_elegida == "1":
            print("Inscripto")
        elif opcion_elegida == "2":
            nueva_clave = input("Ingrese su nueva clave (minimo 6 caracteres de larga): \n")
            confirmacion = input("Ingrese otra vez su nueva clave: \n")

            if nueva_clave != confirmacion:
                print("Error: Las contraseñas deben coincidir.\n")
            else:
                if len(nueva_clave) < 6:
                    print("Error: La nueva contraseña debe tener al menos 6 caracteres.\n")
                else:
                    print("Contraseña cambiada correctamente. \n")


        elif opcion_elegida == "3":
            print("«El ayer es historia, el mañana es un misterio, el hoy es un regalo, por eso se llama presente»\n")


# login_campus()       


# Ejercicio 3 (Alta) — “Agenda de Turnos con
# Nombres (sin listas)”
# Comentario:
# Aca me imagino que ustedes querian que nosotros declaremos y usemos una variable por turno de cada dia.
# Inicialmente se me ocurrio asi como lo hice a continuacion usando replace para quitar los placeholders #libre#,
# aprovechando que la persona no puede ingresar simbolos. Los replace tambien se hace siempre con simbolos para evitar
# que la persona escriba "libre" como nombre.

def agenda_turnos():
    agenda_lunes = """
    Turno 1: #libre#
    Turno 2: #libre#
    Turno 3: #libre#
    Turno 4: #libre#
    """
    agenda_martes = """
    Turno 1: #libre#
    Turno 2: #libre#
    Turno 3: #libre#
    """

    nombre_operador = input("Ingrese nombre del operador (solo letras): \n")

    while not nombre_operador.isalpha():
        nombre_operador = input("Ingrese nombre del operador (solo letras): \n")

    print(f"Bienvenido {nombre_operador}")

    texto_opc = """
    1. Reservar turno
    2. Cancelar turno (por nombre)
    3. Ver agenda del día
    4. Ver resumen general
    5. Cerrar sistema\n"""

    opcion_elegida = ""

    while opcion_elegida != "5":
        opcion_elegida = input(f"Ingrese una opcion: \n {texto_opc}")

        while not opcion_elegida.isdigit() or int(opcion_elegida) < 1 or int(opcion_elegida) > 5:
            print("Error: Por favor elegir una opcion valida")
            opcion_elegida = input(f"Ingrese una opcion: \n {texto_opc}\n")

        if opcion_elegida == "1":
            dia_elegido = input("Elegir día (1=Lunes, 2=Martes)\n")

            while dia_elegido != "1" and dia_elegido != "2":
                print("Error: Elegir 1 (lunes) o 2 (martes)\n")
                dia_elegido = input("Elegir día (1=Lunes, 2=Martes)\n")

            if dia_elegido == "1":
                if "#libre#" not in agenda_lunes:
                    print("No hay turnos disponibles el lunes")
                    continue
            else:
                if "#libre#" not in agenda_martes:
                    print("No hay turnos disponibles el martes")
                    continue

            nombre_paciente = input("Ingrese nombre del paciente (solo letras): \n")
            
            while not nombre_paciente.isalpha():
                nombre_paciente = input("Ingrese nombre del paciente (solo letras): \n")

            agenda_dia = agenda_lunes if dia_elegido == "1" else agenda_martes
            nombre_dia = "lunes" if dia_elegido == "1" else "martes"

            while f"!#{nombre_paciente}#!" in agenda_dia:
                print(f"El paciente ya esta agendado para el dia {nombre_dia}")
                nombre_paciente = input("Ingrese nombre de otro paciente (solo letras): \n")

                while not nombre_paciente.isalpha():
                    nombre_paciente = input("Ingrese nombre del paciente (solo letras): \n")

            if dia_elegido == "1":
                agenda_lunes = agenda_lunes.replace("#libre#", f"!#{nombre_paciente}#!", 1)
            else:
                agenda_martes = agenda_martes.replace("#libre#", f"!#{nombre_paciente}#!", 1)
        elif opcion_elegida == "2":
            dia_elegido = input("Elegir día (1=Lunes, 2=Martes)\n")

            while dia_elegido != "1" and dia_elegido != "2":
                print("Error: Elegir 1 (lunes) o 2 (martes)\n")
                dia_elegido = input("Elegir día (1=Lunes, 2=Martes)\n")

            nombre_paciente = input("Ingrese nombre del paciente (solo letras): \n")
                        
            while not nombre_paciente.isalpha():
                nombre_paciente = input("Ingrese nombre del paciente (solo letras): \n")

            agenda_dia = agenda_lunes if dia_elegido == "1" else agenda_martes

            if f"!#{nombre_paciente}#!" in agenda_dia:
                if dia_elegido == "1":
                    agenda_lunes = agenda_lunes.replace(f"!#{nombre_paciente}#!", "#libre#", 1)
                else:
                    agenda_martes = agenda_martes.replace(f"!#{nombre_paciente}#!", "#libre#", 1)
            else:
                print("El paciente no tenia turno para el dia elegido\n")
        elif opcion_elegida == "3":
            dia_elegido = input("Elegir día (1=Lunes, 2=Martes)\n")
            
            while dia_elegido != "1" and dia_elegido != "2":
                print("Error: Elegir 1 (lunes) o 2 (martes)\n")
                dia_elegido = input("Elegir día (1=Lunes, 2=Martes)\n")

            agenda_dia = agenda_lunes if dia_elegido == "1" else agenda_martes

            agenda_formateada = agenda_dia.replace("!#", "")
            agenda_formateada = agenda_formateada.replace("#!", "")
            agenda_formateada = agenda_formateada.replace("#libre#", "libre")

            print(agenda_formateada)
        elif opcion_elegida == "4":
            libres_lunes = agenda_lunes.count("#libre#")
            libres_martes = agenda_martes.count("#libre#")

            print(f"Turnos libres en la agenda del lunes: {libres_lunes}")
            print(f"Turnos ocupados en la agenda del lunes: {4 - libres_lunes}\n")

            print(f"Turnos libres en la agenda del martes: {libres_martes}")
            print(f"Turnos ocupados en la agenda del martes: {3 - libres_martes}\n")

            dia_mas_turnos = "lunes" if (4 - libres_lunes) > (3 - libres_martes) else "martes" if (4 - libres_lunes) < (3 - libres_martes) else "empate entre ambos dias"

            print(f"Dia con mas turnos ocupados: {dia_mas_turnos}")

            
            
# Ejercicio 4 — “Escape Room: La Bóveda”

def la_boveda():
    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""

    ultima_eleccion = None
    contador_forzado_cerradura = 0

    nombre_agente = input("Ingrese nombre del agente (solo letras): \n")

    while not nombre_agente.isalpha():
        nombre_agente = input("Ingrese nombre del agente (solo letras): \n")

    print(f"Bienvenido {nombre_agente}")

    texto_menu = """
    1. Forzar cerradura
    2. Hackear panel
    3. Descansar\n"""

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

        bloqueo_alarma = alarma and tiempo <= 3

        if bloqueo_alarma:
            print("Perdiste! Razon: Se bloqueó la alarma")
            return  

        estado_descripcion = f"""
        Tiempo restante: {tiempo}
        Energia restante: {energia}
        Cerraduras abiertas: {cerraduras_abiertas}
        Alarma: {"sonando" if alarma else "apagada"}\n
        """
        print(estado_descripcion)

        opcion_elegida = input(f"Ingrese una opcion: \n {texto_menu}")

        while not opcion_elegida.isdigit() or int(opcion_elegida) < 1 or int(opcion_elegida) > 3:
            print("Error: Por favor elegir una opcion valida")
            opcion_elegida = input(f"Ingrese una opcion: \n {texto_menu}\n")

        if opcion_elegida == "1":
            print("Forzando...\n")

            energia -= 20
            tiempo -= 2

            if (ultima_eleccion == "1" or ultima_eleccion is None) and contador_forzado_cerradura < 3:
                contador_forzado_cerradura += 1

            if contador_forzado_cerradura == 3 and not alarma:
                alarma = True  
                print("Se encendio la alarma al trabarse la cerradura!")
                continue

            if not alarma:
                if energia < 40:
                    print("Riesgo de alarma...\n")
                    num_elegido = input(f"Ingrese 1, 2 o 3:\n")
                    
                    while not num_elegido.isdigit() or int(num_elegido) < 1 or int(num_elegido) > 3:
                        print("Error: Por favor elegir una opcion valida\n")
                        num_elegido = input(f"Ingrese una opcion (1, 2 o 3):\n")

                    if num_elegido == "3":
                        print("Se ha encendido la alarma!\n")
                        alarma = True 

                if cerraduras_abiertas < 3 and not alarma:
                    print("Muy bien, abriste una cerradura!\n")
                    cerraduras_abiertas += 1
            else:
                print("La cerradura esta bloqueada! No se puede abrir")
                continue

            ultima_eleccion = opcion_elegida 

        elif opcion_elegida == "2":
            energia -= 10
            tiempo -= 3

            contador_forzado_cerradura = 0 

            for n in range(4):
                print(f"Paso numero {n}")

                letra = input("Ingrese una letra: \n")

                if letra == "":
                    print("Lo ingresado no puede estar vacio\n")
                    letra = input("Ingrese una letra: \n")

                if len(letra) != 1:
                    print("SOLO ingrese una letra, no mas\n")
                    letra = input("Ingrese una letra: \n")

                while not letra.isalpha():
                    print("Lo ingresado no es una letra\n")
                    letra = input("Ingrese una letra: \n")

                codigo_parcial += letra 

                print(f"Codigo parcial: {codigo_parcial}")
            
            if len(codigo_parcial) >= 8:
                if cerraduras_abiertas < 3:
                    print("Muy bien, abriste una cerradura!\n")
                    cerraduras_abiertas += 1

            ultima_eleccion = opcion_elegida 

        else:
            print("Descansando...")

            contador_forzado_cerradura = 0 
            energia += 15
            energia = energia if energia < 100 else 100 

            tiempo -= 1

            if alarma:
                energia -= 10

            ultima_eleccion = opcion_elegida 

    if cerraduras_abiertas == 3:
        print("Victoria! Has logrado abrir todas las cerraduras y escapar. Felicitaciones.")
        return
    elif energia <= 0 or tiempo <= 0:
        razon_derrota = "Te quedaste sin tiempo." if tiempo <= 0 else "Te quedaste sin energia."
        print(f"Perdiste! Razon: {razon_derrota}")
        return

# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

def arena_gladiador():
    print("--- BIENVENIDO A LA ARENA ---")
    nombre_jugador = input("Ingrese nombre del jugador (solo letras, no numeros ni simbolos): \n")
    
    while not nombre_jugador.isalpha():
        nombre_jugador = input("Ingrese nombre del jugador (solo letras, sin simbolos ni numeros): \n")

    hp_jugador = 100
    hp_enemigo = 100
    pociones_vida = 3
    daño_atk_pesado = 15
    daño_enemigo = 12
    turno_gladiador = True

    print("=== INICIO DEL COMBATE ===")

    while hp_jugador > 0 and hp_enemigo > 0:

        if turno_gladiador:
            estado_vida = f"""
            HP {nombre_jugador} (¡vos!): {hp_jugador}
            HP Enemigo: {hp_enemigo}\n

            Pociones restantes: {pociones_vida}
            """

            print(estado_vida)

            opciones = """
            Elegi una de las siguientes opciones (1, 2 o 3):\n
            1. Ataque pesado.
            2. Ráfaga Veloz.
            3. Curar.\n
            """

            opc_elegida = input(opciones)
                                
            while not opc_elegida.isdigit() or int(opc_elegida) < 1 or int(opc_elegida) > 3:
                print("Error: Por favor elegir una opcion valida\n")
                opc_elegida = input(opciones)

            if opc_elegida == "1":
                daño_final = daño_atk_pesado * 1.5 if hp_enemigo < 20 else daño_atk_pesado

                hp_enemigo -= daño_final 

                print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!\n") 
            elif opc_elegida == "2":
                for _ in range(3):
                    hp_enemigo -= 5

                    print("> Golpe conectado por 5 de daño")
            elif opc_elegida == "3":
                if pociones_vida:
                    print("Curandose...\n")
                    hp_jugador += 30
                    pociones_vida -= 1
                else:
                    print("¡No quedan pociones!\n")

            turno_gladiador = False
        else:
            hp_jugador -= daño_enemigo
            print("¡El enemigo te atacó por 12 puntos de daño!\n")

            turno_gladiador = True

    if hp_jugador > 0:
        print(f"¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
    else:
        print("DERROTA. Has caído en combate.")


#Elegir aca que funcion ejecutar:
#################################

# caja_kiosco()
# agenda_turnos()
# la_boveda()
# arena_gladiador()


            
            











