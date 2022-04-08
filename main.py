# obtener la configuración deseada de los Pokemons por parte de cada entrenador. Hay que tener en cuenta, que cada entrenador solamente va a tener tres Pokémons al iniciar la partida.

from tipos import *
from tipos import pokemon
from tipos import ejer2

def elegir():
    print("\nExamen EDA I 8 de Abril 2022\nEsther Rodríguez García:  ")
    variable = int(input("\nPor favor, introduzca qué ejercicio desea realizar: \n --> 1: Pokemon\n --> 2: Tipos de pokemons\n --> 3: main\n"))
    if variable == 1:
        from tipos import pokemon
    elif variable == 2:
        from tipos import ejer2
    elif variable == 3:
        from tipos import main
    else:
        print("Sólo son válidos los valores 1,2 y 3.\n")
        elegir()
elegir()

def main():

    elegir()

if __name__ == "__main__":
    main()





import csv



with open('coach_1_pokemos.csv', 'w', newline='') as csvfile:
    fieldnames = ['', '', '', '', '', '']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'id': 'id', 'nombre': 'nombre', 'arma': 'arma', 'salud': 'salud', 'ataque': 'Ataque', 'defensa': 'Defensa'})


with open('coach_2_pokemos.csv', 'w', newline='') as csvfile:
    fieldnames = ['', '', '', '', '', '']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'id': 'id', 'nombre': 'nombre', 'arma': 'arma', 'salud': 'salud', 'ataque': 'Ataque', 'defensa': 'Defensa'})


