
import csv


class pokemon():
    nombre = csv.reader(open("coach_1_pokemons.csv", "r"))
    for row in nombre:
        print(row)

    def __init__(self, id, nombre, arma, salud, ataque, defensa):
        self.id = id
        self.nombre = nombre
        self.arma = arma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

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

with open('coach_1_pokemos.csv', 'w', newline='') as csvfile:
    fieldnames = ['', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'id': 'id', 'nombre': 'nombre', 'arma': 'arma', 'salud': 'salud', 'ataque': 'Ataque', 'defensa': 'Defensa'})


