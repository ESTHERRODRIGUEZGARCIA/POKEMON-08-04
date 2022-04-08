#Earth Pokemon Este Pokemon va a tener un índice de defensa que va a estar entre 11 y 20.
import random
class tierra():
    def defensa(self):
        return random.randint(11,20)
    
    def __str__(self):
        return "Tierra"
    
    def __del__(self):
        print("Tierra ha sido eliminado. ")

    