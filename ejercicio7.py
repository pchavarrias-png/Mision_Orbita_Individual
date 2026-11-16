
# Proyecto: Mision Orbita - Segundo Avance
# Curso: Principios de Programacion 1
# Ejercicio 7: Actividades de exploracion cientifica

# 1. ENTRADA DE DATOS

energia_disponible = int(input("Ingrese la energia disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))


# 2. INICIALIZACION DE VARIABLES

puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0

exploracion_activa = True


# 3. CICLO PRINCIPAL WHILE

while exploracion_activa:

    # 4. MOSTRAR MENU

    print("MENU DE EXPLORACION CIENTIFICA")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observacion")
    print("4. Finalizar exploracion")

    opcion = int(input("Seleccione una opcion: "))


    # 5. CONDICIONAL MULTIPLE

    match opcion:

        case 1:
            nombre_actividad = "Analizar terreno"
            energia_actividad = 8
            provisiones_actividad = 0
            puntos_actividad = 10

        case 2:
            nombre_actividad = "Recolectar muestra"
            energia_actividad = 12
            provisiones_actividad = 2
            puntos_actividad = 20

        case 3:
            nombre_actividad = "Realizar observacion"
            energia_actividad = 5
            provisiones_actividad = 0
            puntos_actividad = 8

        case 4:
            exploracion_activa = False

        case _:
            print("Opcion no valida.")


    # 6. VALIDACION DE RECURSOS

    if opcion == 1 or opcion == 2 or opcion == 3:

        if energia_disponible >= energia_actividad and provisiones_disponibles >= provisiones_actividad:

            # 7. DESCONTAR RECURSOS

            energia_disponible = energia_disponible - energia_actividad
            provisiones_disponibles = provisiones_disponibles - provisiones_actividad

            # 8. ACTUALIZAR CONTADORES Y ACUMULADOR

            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad

            if opcion == 2:
                muestras_recolectadas = muestras_recolectadas + 1

            print("Actividad realizada:", nombre_actividad)
            print("Puntos obtenidos:", puntos_actividad)

        else:
            print("Recursos insuficientes para realizar la actividad.")
            print("La exploracion finaliza.")
            exploracion_activa = False


# 9. RESUMEN FINAL

print("RESUMEN DE LA EXPLORACION")
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos cientificos:", puntos_cientificos)
print("Energia restante:", energia_disponible)
print("Provisiones restantes:", provisiones_disponibles)
