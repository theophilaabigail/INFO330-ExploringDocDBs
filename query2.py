from pymongo import MongoClient

# connection
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# find all pokemmon with attach > 150
high_attack_pokemon = pokemonColl.find({"attack": {"$gt": 150}})

# loop through the result
for pokemon in high_attack_pokemon:
    print(pokemon)

