class pokemon():
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
        print("{} tiene {} de salud".format(pokemon.nombre, pokemon.salud))
        if pokemon.salud <= 0:
            print("{} ha muerto".format(pokemon.nombre))
            return True
        else:
            return False
            
