# obtener la configuración deseada de los Pokemons por parte de cada entrenador. Hay que tener en cuenta, que cada entrenador solamente va a tener tres Pokémons al iniciar la partida.

from tipos import *
from tipos import pokemon
from tipos import ejer2
import csv

def elegir():
    print("\nExamen EDA I 8 de Abril 2022\nEsther Rodríguez García:  ")
    print("\nEjercicio 1: Pokemon")
    print("\nEjercicio 2: 4 tipos de Pokémon diferentes: Tierra, Agua, Aire y Electricidad.")
elegir()



with open('coach_1_pokemos.csv', 'w', newline='') as csvfile:
    fieldnames = ['', '', '', '', '', '']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader() #escribe el nombre de las columnas


with open('coach_2_pokemos.csv', 'w', newline='') as csvfile:
    fieldnames = ['', '', '', '', '', '']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()


def main():
    elegir()

if __name__ == "__main__":
    main()


