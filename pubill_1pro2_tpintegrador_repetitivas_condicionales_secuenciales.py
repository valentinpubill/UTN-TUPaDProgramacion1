#Pubill Valentín
#Trabajo practico integrador Repetitivas condicionales y secuenciales
#Ejercicio 1 caja del kiosco

nombre = input("Nombre del cliente: ")
while not nombre.isalpha():
    print("Solo letras, ingrese de nuevo")
    nombre = input("Nombre del cliente: ")
cantidad = input("Cuantos productos son: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Ingrese un numero valido")
    cantidad = input("Cuantos productos son: ")
cantidad = int(cantidad)

total = 0
total_desc = 0
for i in range(cantidad):
    print(f"Producto {i + 1}")

    precio = input("Precio: ")
    while not precio.isdigit():
        print("Ingrese un numero valido")
        precio = input("Precio: ")
    precio = int(precio)

    desc = input("Tiene descuento? (s/n): ").lower()
    while desc != "s" and desc != "n":
        print("Responda s o n")
        desc = input("Tiene descuento? (s/n): ").lower()

    total = total + precio

    if desc == "s":
        precio = precio - (precio * 0.10)

    total_desc = total_desc + precio

promedio = total_desc / cantidad

print(f"""
Cliente: {nombre}
Total sin descuento: {total:.2f}
Total con descuento: {total_desc:.2f}
Promedio por producto: {promedio:.2f}
""")

# 2 - Acceso al campus - Acceso al Campus y Menu Seguro

usuario_ok = "admin"
clave_ok = "1234"

acceso = False

for i in range(3):
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_ok and clave == clave_ok:
        acceso = True
        print("Acceso concedido")
        break
    else:
        print("Datos incorrectos")

if acceso == False:
    print("Se bloqueo el acceso, supero los 3 intentos")

if acceso == True:
    while True:
        print("""
1 - Ver perfil
2 - Ver materias
3 - Cambiar clave
4 - Salir
""")

        op = input("Opcion: ")
        while not op.isdigit() or int(op) < 1 or int(op) > 4:
            print("Ingrese un numero entre 1 y 4")
            op = input("Opcion: ")
        op = int(op)

        if op == 1:
            print(f"Usuario: {usuario_ok}")
        elif op == 2:
            print("Materias: Programacion 1, Matematica, Arquitectura")
        elif op == 3:
            nueva = input("Nueva clave (minimo 6 caracteres): ")
            while len(nueva) < 6:
                print("Muy corta, minimo 6 caracteres")
                nueva = input("Nueva clave (minimo 6 caracteres): ")
            clave_ok = nueva
            print("Clave cambiada")
        elif op == 4:
            print("Saliendo")
            break

# Ejercicio 3 - Agenda de turnos

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
martes4 = ""

while True:
    print("""
1 - Reservar
2 - Cancelar
3 - Ver agenda
4 - Resumen
5 - Salir
""")

    op = input("Opcion: ")
    while not op.isdigit() or int(op) < 1 or int(op) > 5:
        print("Ingrese un numero entre 1 y 5")
        op = input("Opcion: ")
    op = int(op)

    if op == 1:
        dia = input("Dia (lunes/martes): ").lower()
        while dia != "lunes" and dia != "martes":
            print("Ingrese lunes o martes")
            dia = input("Dia (lunes/martes): ").lower()

        nom = input("Nombre: ")
        while not nom.isalpha():
            print("Solo letras")
            nom = input("Nombre: ")

        if dia == "lunes":
            if lunes1 == "":
                lunes1 = nom
                print("Reservado lunes 1")
            elif lunes2 == "":
                lunes2 = nom
                print("Reservado lunes 2")
            elif lunes3 == "":
                lunes3 = nom
                print("Reservado lunes 3")
            elif lunes4 == "":
                lunes4 = nom
                print("Reservado lunes 4")
            else:
                print("No hay turnos libres el lunes")
        else:
            if martes1 == "":
                martes1 = nom
                print("Reservado martes 1")
            elif martes2 == "":
                martes2 = nom
                print("Reservado martes 2")
            elif martes3 == "":
                martes3 = nom
                print("Reservado martes 3")
            elif martes4 == "":
                martes4 = nom
                print("Reservado martes 4")
            else:
                print("No hay turnos libres el martes")

    elif op == 2:
        nom = input("Nombre del turno a cancelar: ")

        if lunes1 == nom:
            lunes1 = ""
        elif lunes2 == nom:
            lunes2 = ""
        elif lunes3 == nom:
            lunes3 = ""
        elif lunes4 == nom:
            lunes4 = ""
        elif martes1 == nom:
            martes1 = ""
        elif martes2 == nom:
            martes2 = ""
        elif martes3 == nom:
            martes3 = ""
        elif martes4 == nom:
            martes4 = ""
        else:
            print("No se encontro ese turno")
            continue

        print("Turno cancelado")

    elif op == 3:
        dia = input("Dia (lunes/martes): ").lower()
        while dia != "lunes" and dia != "martes":
            print("Ingrese lunes o martes")
            dia = input("Dia (lunes/martes): ").lower()

        if dia == "lunes":
            h1 = lunes1 if lunes1 != "" else "libre"
            h2 = lunes2 if lunes2 != "" else "libre"
            h3 = lunes3 if lunes3 != "" else "libre"
            h4 = lunes4 if lunes4 != "" else "libre"
        else:
            h1 = martes1 if martes1 != "" else "libre"
            h2 = martes2 if martes2 != "" else "libre"
            h3 = martes3 if martes3 != "" else "libre"
            h4 = martes4 if martes4 != "" else "libre"

        print(f"""
1: {h1}
2: {h2}
3: {h3}
4: {h4}
""")

    elif op == 4:
        ocupados = 0
        libres = 0

        if lunes1 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1
        if lunes2 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1
        if lunes3 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1
        if lunes4 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1
        if martes1 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1
        if martes2 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1
        if martes3 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1
        if martes4 != "":
            ocupados = ocupados + 1
        else:
            libres = libres + 1

        print(f"""
Ocupados: {ocupados}
Libres: {libres}
""")

    elif op == 5:
        print("Chau")
        break

# Ejercicio 4 - Escape Room

agente = input("Nombre del agente: ")
while not agente.isalpha():
    print("Solo letras")
    agente = input("Nombre del agente: ")

energia = 100
tiempo = 100
cerraduras = 0
alarma = False
contador_forzar = 0

codigo = "CLAU"

while energia > 0 and tiempo > 0 and cerraduras < 3 and not alarma:
    print(f"""
Energia: {energia}  Tiempo: {tiempo}  Cerraduras: {cerraduras}
1 - Forzar cerradura
2 - Hackear panel
3 - Abandonar
""")

    op = input("Opcion: ")
    while not op.isdigit() or int(op) < 1 or int(op) > 3:
        print("Ingrese un numero entre 1 y 3")
        op = input("Opcion: ")
    op = int(op)

    if op == 1:
        contador_forzar = contador_forzar + 1
        if contador_forzar >= 3:
            print("Forzaste 3 veces seguidas, salto la alarma")
            alarma = True
        else:
            cerraduras = cerraduras + 1
            energia = energia - 20
            tiempo = tiempo - 10
            print("Cerradura forzada")

    elif op == 2:
        contador_forzar = 0
        intento = ""
        for i in range(4):
            letra = input("Letra: ")
            intento = intento + letra

        tiempo = tiempo - 15

        if intento.upper() == codigo:
            cerraduras = cerraduras + 1
            print("Panel hackeado")
        else:
            energia = energia - 10
            print("Codigo incorrecto")

    elif op == 3:
        print("El agente abandona")
        energia = 0

if cerraduras >= 3:
    print(f"Ganaste, {agente} abrio la boveda")
elif alarma:
    print("Perdiste, salto la alarma")
elif energia <= 0:
    print("Perdiste, te quedaste sin energia")
else:
    print("Perdiste, se acabo el tiempo")

# Ejercicio 5 - Escape Room: La Arena del Gladiador

nombre = input("Nombre del gladiador: ")
while not nombre.isalpha():
    print("Solo letras")
    nombre = input("Nombre del gladiador: ")

vida = 100
vida_enemigo = 100
pociones = 3

while vida > 0 and vida_enemigo > 0:
    print(f"""
Tu vida: {vida}  Vida enemigo: {vida_enemigo}  Pociones: {pociones}
1 - Ataque
2 - Rafaga veloz
3 - Curar
""")

    op = input("Opcion: ")
    while not op.isdigit() or int(op) < 1 or int(op) > 3:
        print("Ingrese un numero entre 1 y 3")
        op = input("Opcion: ")
    op = int(op)

    if op == 1:
        daño = 10
        if vida_enemigo < 20:
            daño = daño * 1.5
            print("Golpe critico")
        vida_enemigo = vida_enemigo - daño

    elif op == 2:
        for i in range(3):
            vida_enemigo = vida_enemigo - 5

    elif op == 3:
        if pociones > 0:
            vida = vida + 30
            pociones = pociones - 1
            print("Usaste una pocion")
        else:
            print("No tenes pociones, perdiste el turno")

    if vida_enemigo > 0:
        vida = vida - 8
        print("El enemigo te ataca")

if vida <= 0 and vida_enemigo <= 0:
    print("Empate")
elif vida <= 0:
    print(f"Perdiste, {nombre} cayo en la arena")
else:
    print(f"Ganaste, {nombre} gano el combate")