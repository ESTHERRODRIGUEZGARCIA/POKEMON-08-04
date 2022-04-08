# Pokémon de Aire Este Pokemon tiene el método defensa modificado de tal forma que existe un 50% de posibilidad de que no le afecte un ataque. Este 50% se puede calcular utilizando el módulo random.
import random

class aire():
    def __init__(self, id, nombre, arma, salud, ataque, defensa):
        self.id = id
        self.nombre = nombre
        self.arma = arma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.defensa_modificada = False

    def __str__(self):
        return "Pokemon: {}\nArma: {}\nSalud: {}\nAtaque: {}\nDefensa: {}".format(self.nombre, self.arma, self.salud, self.ataque, self.defensa)

    def atacar(self, pokemon):
        if self.defensa_modificada == False:
            pokemon.salud -= self.ataque - pokemon.defensa
            print("{} atacó a {}".format(self.nombre, pokemon.nombre))
            print("{} tiene {} de salud. ".format(pokemon.nombre, pokemon.salud))
            if pokemon.salud <= 0:
                print("{} ha muerto. ".format(pokemon.nombre))
                return True
            else:
                return False
        else:
            if random.randint(1,2) == 1:
                pokemon.salud -= self.ataque - pokemon.defensa
                print("{} atacó a {}".format(self.nombre, pokemon.nombre))
                print("{} tiene {} de salud. ".format(pokemon.nombre, pokemon.salud))
                if pokemon.salud <= 0:
                    print("{} ha muerto. ".format(pokemon.nombre))
                    return True
                else:
                    return False
            else:
                print("{} no atacó a {}".format(self.nombre, pokemon.nombre))
                return False

    def defender(self, pokemon):
        self.salud -= pokemon.ataque - self.defensa