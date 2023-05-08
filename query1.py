from pymongo import MongoClient

# connection
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# filter all pikachu pokemon
pikachu_pokemon = pokemonColl.find({"name": "Pikachu"})

# loop through the result
for pokemon in pikachu_pokemon:
    print(pokemon)