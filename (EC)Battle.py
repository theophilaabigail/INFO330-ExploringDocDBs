import random
import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters
import pymongo
import json
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])

    pokemon1_advantages = []
    pokemon2_advantages = []

    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            pokemon1_advantages.append(stat)
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            pokemon2_advantages.append(stat)
        else:
            print("Both Pokemon have equal " + stat)

    if len(pokemon1_advantages) > len(pokemon2_advantages):
        print("Battle results: " + pokemon1['name'] + " wins!")
    elif len(pokemon2_advantages) > len(pokemon1_advantages):
        print("Battle results: " + pokemon2['name'] + " wins!")
    else:
        print("Battle results: Tie")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()