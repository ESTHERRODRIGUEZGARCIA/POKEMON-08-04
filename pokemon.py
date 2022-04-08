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

def fight_attack(self, pokemon_to_attack):
    if is_alive(self) and is_alive(pokemon_to_attack):
        self.ataque = self.ataque + self.arma
        pokemon_to_attack.defender(self)
        self.ataque = self.ataque - self.arma
    else:
        print("{} o {} ya no están vivos. ".format(self.nombre, pokemon_to_attack.nombre))

def fight_defense(self, points_of_damage):
    if is_alive(self):
        self.salud = self.salud - points_of_damage
        print("{} ha recibido {} de daño. ".format(self.nombre, points_of_damage))
        if self.salud <= 0:
            print("{} ha muerto. ".format(self.nombre))
            return False
        else:
            return True
    else:
        print("{} ya no está vivo".format(self.nombre))
        return False
