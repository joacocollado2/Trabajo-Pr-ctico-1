# Inicio de TP 1


# Carga de datos

cp = input("Ingrese el código postal del lugar de destino: ")

# Establecer una bandera y poner en una tupla los numeros naturales

ban = True
reales = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
provincia = ("Salta", "Provincia de Buenos Aires", "Ciudad Autónoma de Buenos Aires", "San Luis", "Entre Ríos",
             "La Rioja", "Santiago del Estero", "Chaco", "San Juan", "Catamarca", "La Pampa", "Mendoza", "Misiones",
             "Formosa", "Neuquén", "Río Negro", "Santa Fe", "Tucumán", "Chubut", "Tierra del Fuego", "Corrientes",
             "Córdoba", "Jujuy", "Santa Cruz")

if len(cp) > 9 or len(cp) < 4:
    ban = False
    if ban == False:
        print("Otros Países")

else:

    if len(cp) == 4:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales:
            print("Bolivia")
        else:
            print("Otros países")

    if len(cp) == 5:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales:
            print("Uruguay")
        else:
            print("Otros países")

    if len(cp) == 6:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
            5] in reales:
            print("Paraguay")
        else:
            print("Otros países")

    if len(cp) == 7:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
            5] in reales and cp[6] in reales:
            print("Chile")
        else:
            print("Otros países")

    if len(cp) == 9:
        if cp[0] in reales and cp[1] in reales and cp[2] in reales and cp[3] in reales and cp[4] in reales and cp[
            5] in reales and cp[6] in reales and cp[7] in reales and cp[8] in reales:
            print("Brasil")
        else:
            print("Otros países")
    if len(cp) == 8:
        if (cp[0] not in reales and cp[7] not in reales and cp[6] not in reales and cp[5] not in reales and cp[1] in reales
            and cp[2] in reales and cp[3] in reales and cp[4] in reales):
            print("Argentina")
        else:
            print("Otros países")


