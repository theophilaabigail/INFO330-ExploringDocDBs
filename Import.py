import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters
import pymongo
import json
from pymongo import MongoClient

# connection
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# connect to db
connection = sqlite3.connect("pokemon.sqlite")
cursor = connection.cursor()

# query
query = """
    SELECT p.name, p.pokedex_number, t.type1, t.type2, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, a.name
    FROM pokemon AS p
    LEFT JOIN pokemon_types_view AS t ON p.name = t.name
    LEFT JOIN pokemon_abilities AS pa ON p.id = pa.pokemon_id
    LEFT JOIN ability AS a ON pa.ability_id = a.id
"""

# execute query
cursor.execute(query)
rows = cursor.fetchall()

# loop through rows to fetch data
pokemon_json = {}
for row in rows:
    pokedex_number = row[1]
    if pokedex_number not in pokemon_json:
        pokemon_json[pokedex_number] = {
             "name": row[0],
            "pokedex_number": row[1],
            "types": [t for t in [row[2], row[3]] if t],
            "hp": row[4],
            "attack": row[5],
            "defense": row[6],
            "speed": row[7],
            "sp_attack": row[8],
            "sp_defense": row[9],
            "abilities": [row[10]]
        }
    else:
        pokemon_json[pokedex_number]["abilities"].append(row[10])

# insert data into MongoDB
pokemon_list = [pokemon_json[key] for key in pokemon_json]
pokemonColl.insert_many(pokemon_list)


# close connection
mongoClient.close()



