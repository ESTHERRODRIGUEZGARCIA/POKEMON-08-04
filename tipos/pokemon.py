
import csv


class pokemon():
    nombre = csv.reader(open("coach_1_pokemons.csv", "r"))
    for row in nombre:
        print(row)

    def __init__(self, id, nombre, arma, salud, ataque, defensa):
        self.id = id
        self.nombre = nombre
        self.arma = arma #Puñetazo, Patada, Codazo, Cabezazo
        self.salud = salud #entre 1 y 100
        self.ataque = ataque #entre 1 y 10
        self.defensa = defensa #entre 1 y 10


    def __str__(self):
        return "Pokemon: {}\nArma: {}\nSalud: {}\nAtaque: {}\nDefensa: {}".format(self.nombre, self.arma, self.salud, self.ataque, self.defensa)

    def atacar(self, pokemon):
        pokemon.salud -= self.ataque - pokemon.defensa
        print("{} atacó a {}".format(self.nombre, pokemon.nombre))
        print("{} tiene {} de salud. ".format(pokemon.nombre, pokemon.salud))
        if pokemon.salud <= 0:
            print("{} ha muerto. ".format(pokemon.nombre))
            return True
        else:
            return False

    def defender(self, pokemon):
        self.salud -= pokemon.ataque - self.defensa
        print("{} atacó a {}".format(pokemon.nombre, self.nombre))
        print("{} tiene {} de salud. ".format(self.nombre, self.salud))
        if self.salud <= 0:
            print("{} ha muerto. ".format(self.nombre))
            return True
        else:
            return False


    def __del__(self):
        print("{} ha sido eliminado. ".format(self.nombre))

def is_alive(self):
    if self.salud <= 0:
        return False
    else:
        return True

