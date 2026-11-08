# Proyecto: Mision Orbita - Segundo Avance
# Curso: Principios de Programacion 1
# Ejercicio 6: Simulacion del viaje espacial
# Descripcion: Simular el desarrollo del viaje
# y mostrar el estado de la mision.

# CONSTANTES DE CONSUMO DIARIO
COMBUSTIBLE_POR_DIA = 8
OXIGENO_POR_TRIPULANTE = 2
ENERGIA_POR_DIA = 5
PROVISIONES_POR_TRIPULANTE = 1

# ENTRADA DE DATOS
dias_viaje = int(input("Ingrese los dias del viaje: "))
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxigeno disponible: "))
energia = int(input("Ingrese la energia disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# CALCULAR CONSUMOS POR DIA
consumo_combustible = COMBUSTIBLE_POR_DIA
consumo_oxigeno = tripulantes * OXIGENO_POR_TRIPULANTE
consumo_energia = ENERGIA_POR_DIA
consumo_provisiones = tripulantes * PROVISIONES_POR_TRIPULANTE

# VARIABLES DE CONTROL
dias_transcurridos = 0
viaje_puede_continuar = True

print("\n--- INICIO DEL VIAJE ESPACIAL ---")

# REPETIR MIENTRAS QUEDEN DIAS Y RECURSOS SUFICIENTES
while dias_transcurridos < dias_viaje and viaje_puede_continuar:

    # Verificar recursos antes de consumirlos
    if (combustible >= consumo_combustible and
            oxigeno >= consumo_oxigeno and
            energia >= consumo_energia and
            provisiones >= consumo_provisiones):

        # Descontar recursos del dia
        combustible = combustible - consumo_combustible
        oxigeno = oxigeno - consumo_oxigeno
        energia = energia - consumo_energia
        provisiones = provisiones - consumo_provisiones

        # Registrar dia completado
        dias_transcurridos = dias_transcurridos + 1

        print("\nDia completado:", dias_transcurridos)
        print("Combustible restante:", combustible)
        print("Oxigeno restante:", oxigeno)
        print("Energia restante:", energia)
        print("Provisiones restantes:", provisiones)

    else:
        viaje_puede_continuar = False

# RESULTADO FINAL
if dias_transcurridos == dias_viaje:
    print("\nLa nave llego al destino en", dias_transcurridos, "dias.")
    print("Recursos finales:")
    print("Combustible:", combustible)
    print("Oxigeno:", oxigeno)
    print("Energia:", energia)
    print("Provisiones:", provisiones)

else:
    print("\nViaje interrumpido en el dia", dias_transcurridos + 1)
    print("Dias completados:", dias_transcurridos)
    print("Recursos insuficientes:")

    if combustible < consumo_combustible:
        print("- Combustible insuficiente.")

    if oxigeno < consumo_oxigeno:
        print("- Oxigeno insuficiente.")

    if energia < consumo_energia:
        print("- Energia insuficiente.")

    if provisiones < consumo_provisiones:
        print("- Provisiones insuficientes.")
