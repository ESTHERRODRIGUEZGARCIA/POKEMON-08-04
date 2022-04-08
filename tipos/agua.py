#Pokémon de Agua: Este Pokemon va a tener un índice de ataque que va a estar entre 11 y 20.
import random

class agua():
    def ataque(self):
        return random.randint(11,20)
    
    def __str__(self):
        return "Agua"
    
    def __del__(self):
        print("Agua ha sido eliminado. ")