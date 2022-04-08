# obtener la configuración deseada de los Pokemons por parte de cada entrenador. Hay que tener en cuenta, que cada entrenador solamente va a tener tres Pokémons al iniciar la partida.

from tipos import *
from tipos import pokemon
from tipos import ejer2
if __name__ == "__main__":
    main()



def main():

    elegir()

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


