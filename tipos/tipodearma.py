# hay 4 tipos de arma: Puñetazo, Patada, Codazo, Cabezazo
def tipo_arma():
    arma_usar = input("\nPor favor, introduzca qué arma desea usar: \n --> 1: Puñetazo\n --> 2: Patada\n --> 3: Codazo\n --> 4: Cabezazo\n")
    if arma_usar == "1":
        return "Puñetazo"
    elif arma_usar == "2":
        return "Patada"
    elif arma_usar == "3":
        return "Codazo"
    elif arma_usar == "4":
        return "Cabezazo"
    else:
        print("Sólo son válidos los valores 1,2,3 y 4.\n")
        tipo_arma()

def __str__(self):
    return self.name

