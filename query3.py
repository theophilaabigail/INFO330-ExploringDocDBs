from pymongo import MongoClient

# connection
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# find all Pokemon with the "Overgrow" ability
overgrow = pokemonColl.find({"abilities": "Overgrow"})

# print result
for pokemon in overgrow:
    print(pokemon)

