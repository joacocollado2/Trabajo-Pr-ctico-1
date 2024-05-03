# Inicio de TP 1


# Carga de datos

cp = input("Ingrese el código postal del lugar de destino: ")

# Establecer una bandera y poner en una tupla los numeros naturales

ban = True
reales = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

if len(cp) > 9 or len(cp) < 4:
    ban = False
    if ban == False:
        print("Otros Países")

else:
    if (cp[0] not in reales and cp[7] not in reales and cp[6] not in reales and cp[5] not in reales and cp[1] in reales
            and cp[2] in reales and cp[3] in reales and cp[4] in reales):
        print("Argentina")
    else:
        print("Error")
