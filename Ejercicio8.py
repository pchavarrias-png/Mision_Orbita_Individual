
# Proyecto: Mision Orbita - Segundo Avance
# Curso: Principios de Programacion 1
# Ejercicio 8: Evaluacion del regreso y supervivencia
# Descripcion: Evaluar si la tripulacion puede regresar
# a la Tierra o calcular sus dias de supervivencia.

# CONSTANTES DE CONSUMO DIARIO
COMBUSTIBLE_POR_DIA = 8
OXIGENO_POR_TRIPULANTE = 2
ENERGIA_POR_DIA = 5
PROVISIONES_POR_TRIPULANTE = 1

# ENTRADA DE DATOS
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los dias del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxigeno disponible: "))
energia = int(input("Ingrese la energia disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# CALCULAR RECURSOS NECESARIOS
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA
consumo_oxigeno = tripulantes * OXIGENO_POR_TRIPULANTE
consumo_provisiones = tripulantes * PROVISIONES_POR_TRIPULANTE

# INICIALIZAR VARIABLES DE CONTROL
dias_transcurridos = 0
regreso_activo = True

print("--- EVALUACION DEL REGRESO ---")

# DECISION: VERIFICAR COMBUSTIBLE
if combustible >= combustible_regreso:

    print("La nave tiene combustible suficiente para regresar.")

    # CICLO DE REGRESO
    while dias_transcurridos < dias_viaje and regreso_activo:

        # VERIFICAR RECURSOS ANTES DEL CONSUMO
        if (combustible >= COMBUSTIBLE_POR_DIA
            and oxigeno >= consumo_oxigeno
            and energia >= ENERGIA_POR_DIA
            and provisiones >= consumo_provisiones):

            # DESCONTAR RECURSOS
            combustible = combustible - COMBUSTIBLE_POR_DIA
            oxigeno = oxigeno - consumo_oxigeno
            energia = energia - ENERGIA_POR_DIA
            provisiones = provisiones - consumo_provisiones

            # ACTUALIZAR CONTADOR
            dias_transcurridos = dias_transcurridos + 1

            # MOSTRAR ESTADO ACTUAL
            print("Dia completado:", dias_transcurridos)
            print("Combustible restante:", combustible)
            print("Oxigeno restante:", oxigeno)
            print("Energia restante:", energia)
            print("Provisiones restantes:", provisiones)

        else:
            regreso_activo = False

            print("\nEl regreso se interrumpio en el dia",
                  dias_transcurridos + 1)

            print("Recursos insuficientes:")

            if combustible < COMBUSTIBLE_POR_DIA:
                print("- Combustible insuficiente")

            if oxigeno < consumo_oxigeno:
                print("- Oxigeno insuficiente")

            if energia < ENERGIA_POR_DIA:
                print("- Energia insuficiente")

            if provisiones < consumo_provisiones:
                print("- Provisiones insuficientes")

    # RESULTADO DEL REGRESO
    if dias_transcurridos == dias_viaje:
        print("\nLa tripulacion regreso exitosamente a la Tierra.")
    else:
        print("\nLa tripulacion no completo el regreso.")

# CASO B: LA TRIPULACION QUEDA VARADA
else:

    print("La tripulacion quedo varada en el destino.")

    # CALCULAR DIAS DE SUPERVIVENCIA
    dias_oxigeno = oxigeno // consumo_oxigeno
    dias_energia = energia // ENERGIA_POR_DIA
    dias_provisiones = provisiones // tripulantes

    print("Dias por oxigeno:", dias_oxigeno)
    print("Dias por energia:", dias_energia)
    print("Dias por provisiones:", dias_provisiones)

    # DETERMINAR EL MENOR VALOR MEDIANTE CONDICIONALES
    if dias_oxigeno <= dias_energia and dias_oxigeno <= dias_provisiones:
        supervivencia = dias_oxigeno

    elif dias_energia <= dias_oxigeno and dias_energia <= dias_provisiones:
        supervivencia = dias_energia

    else:
        supervivencia = dias_provisiones

    print("Supervivencia estimada:", supervivencia, "dias")

    # IDENTIFICAR TODOS LOS RECURSOS LIMITANTES
    print("Recurso(s) limitante(s):")

    if dias_oxigeno == supervivencia:
        print("- Oxigeno")

    if dias_energia == supervivencia:
        print("- Energia")

    if dias_provisiones == supervivencia:
        print("- Provisiones")

# FIN DEL PROGRAMA
