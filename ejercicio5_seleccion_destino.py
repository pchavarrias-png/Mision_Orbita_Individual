# Proyecto: Mision Orbita - Segundo Avance
# Curso: Principios de Programacion 1
# Ejercicio 5: Seleccion del destino y autorizacion
# Descripcion: Seleccionar el destino de la mision
# y verificar si la nave cumple los requisitos.

# CONSTANTES
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10

OXIGENO_POR_TRIPULANTE = 2
RESERVA_OXIGENO = 5

ENERGIA_POR_DIA = 5
RESERVA_ENERGIA = 10

RESERVA_PROVISIONES = 3

# ENTRADA DE DATOS DE LA MISIÓN
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))

print("Seleccione el destino:")
print("1. Luna")
print("2. Marte")
print("3. Europa")

opcion_destino = int(input("Ingrese una opción: "))

# SELECCIÓN Y VALIDACIÓN DEL DESTINO
destino_valido = False

match opcion_destino:
    case 1:
        destino = "Luna"
        dias_viaje = 3
        destino_valido = True

    case 2:
        destino = "Marte"
        dias_viaje = 5
        destino_valido = True

    case 3:
        destino = "Europa"
        dias_viaje = 7
        destino_valido = True

    case _:
        destino_valido = False

# PLANIFICACIÓN DE LA MISIÓN
if destino_valido:

    # ENTRADA DE RECURSOS DISPONIBLES
    combustible_disponible = int(input("Ingrese el combustible disponible: "))
    oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
    energia_disponible = int(input("Ingrese la energía disponible: "))
    provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

    # CÁLCULO DE RECURSOS REQUERIDOS
    combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
    combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA

    combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

    oxigeno_requerido = dias_viaje * tripulantes * OXIGENO_POR_TRIPULANTE + RESERVA_OXIGENO

    energia_requerida = dias_viaje * ENERGIA_POR_DIA + RESERVA_ENERGIA

    provisiones_requeridas = dias_viaje * tripulantes + RESERVA_PROVISIONES

    # RESUMEN DE LA MISIÓN
    print("\n--- RESUMEN DE LA MISIÓN ---")
    print("Nombre de la misión:", nombre_mision)
    print("Destino:", destino)
    print("Tripulantes:", tripulantes)
    print("Días de viaje de ida:", dias_viaje)

    print("Combustible de ida:", combustible_ida)
    print("Combustible de regreso:", combustible_regreso)
    print("Reserva de combustible:", RESERVA_COMBUSTIBLE)
    print("Combustible total requerido:", combustible_total)

    print("Oxígeno requerido:", oxigeno_requerido)
    print("Energía requerida:", energia_requerida)
    print("Provisiones requeridas:", provisiones_requeridas)

    # AUTORIZACIÓN DEL LANZAMIENTO
    if (combustible_disponible >= combustible_total and
        oxigeno_disponible >= oxigeno_requerido and
        energia_disponible >= energia_requerida and
        provisiones_disponibles >= provisiones_requeridas):

        print("Lanzamiento autorizado.")

    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")

else:
    print("Opción de destino no válida. La misión no puede planificarse.")
