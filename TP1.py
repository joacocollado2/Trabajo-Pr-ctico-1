# Inicio de TP 1


# Carga de datos

cp = input("Ingrese el código postal del lugar de destino: ")

reales = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
ban = True

if len(cp) > 9 or len(cp) < 4:
    ban = False
if ban == False:
    print("Otros Países")

else:
    if cp[0] != reales and cp[7] != reales and cp[6] != reales and cp[5] != reales:
        print("Argentina")
    else:
        print("Error")
