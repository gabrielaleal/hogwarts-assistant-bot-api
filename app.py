from flask import Flask, make_response, jsonify
import random
import requests

app = Flask(__name__)

wizards = [
  {
    'name':  'Merlin',
    'info': 'Merlin is the most famous wizard of all time. He is sometimes known as the Prince of Enchanters and was part of the Court of King Arthur.'
  },
  {
    'name': 'Harry Potter',
    'info': 'Harry James Potter was one of the most famous wizards of modern times. The first and only known wizard that survived the\
    killing curse, earning him the title of The boy who lived.'
  },
  {
    'name': 'Newt Scamander',
    'info': 'Regarded as the world authority on magical creatures, Newt Scamander is the author of Fantastic Beasts and Where to Find\
    Them, which has been an approved textbook at Hogwarts since its publication in 1927 and can be found in most wizarding households.'
  },
  {
    'name': 'Albus Dumbledore',
    'info': 'Considered by many to be the greatest wizard of modern times, Dumbledore is particularly famous for his defeat of the Dark \
    wizard Grindelwald in 1945, for the discovery of the twelve uses of Dragon\'s blood, and his work on alchemy with his partner, Nicolas Flamel.\
    Professor Dumbledore enjoys chamber music and tenpin bowling.'
  },
  {
    'name': 'Devlin Whitehorn',
    'info': 'Founder of the Nimbus racing broom company.'
  },
    {
    'name': 'Beatrix Bloxam',
    'info': 'Author of the Toadstool Tales, a series of children\'s books since banned because they have been found to cause nausea and vomiting.'
  },
    {
    'name': 'Laverne de Montmorency',
    'info': 'Inventor of many Love Potions.'
  },
  {
    'name': 'Queen Maeve',
    'info': 'This legendary witch trained young sorcerers in Ireland prior to the establishment of Hogwarts School of Witchcraft and Wizardry.'
  },
  {
    'name': 'Alberta Toothill',
    'info': 'Alberta Toothill was the winner of the All-England Wizarding Duelling Competition of 1430. She famously overcame the favourite,\
    Samson Wiblin, with a Blasting Curse.'
  },
  {
    'name': 'Mirabella Plunkett',
    'info': 'Famous for falling in love with a merman in Loch Lomond while on holiday. When her parents forbade her to marry him, she transfigured\
    herself into a haddock and was never seen again.'
  },
  {
    'name': 'Morgan le Fay',
    'info': 'Morgan Le Fay, also known as Morgana, affected many events during the time of King Arthur. She was queen of the island of Avalon,\
    and she had great skill as a healer.'
  },
  {
    'name': 'Godric Gryffindor',
    'info': 'One of the four famous Founders of Hogwarts School of Witchcraft and Wizardry, Godric Gryffindor was the most accomplished dueller of \
    his time, an enlightened fighter against Muggle-discrimination and the first owner of the celebrated Sorting Hat.'
  },
  {
    'name': 'Rowena Ravenclaw',
    'info': 'One of the four famous Founders of Hogwarts School of Witchcraft and Wizardry, Rowena Ravenclaw was the most brilliant witch of her \
    time, though legend has it that a broken heart - cause unknown - contributed to her early demise. Her daughter Helena (the Grey Lady) is the \
    Ravenclaw house ghost at Hogwarts.'
  },
  {
    'name': 'Salazar Slytherin',
    'info': 'One of the four celebrated Founders of Hogwarts School of Witchcraft and Wizardry, Salazar Slytherin was one of the first recorded \
    Parselmouths, an accomplished Legilimens, and a notorious champion of pureblood supremacy. His last remaining heir was Lord Voldemort.'
  },
  {
    'name': 'Helga Hufflepuff',
    'info': 'One of the four celebrated Founders of Hogwarts School of Witchcraft and Wizardry, Hufflepuff was particularly famous for her dexterity \
    at food-related Charms. Many recipes traditionally served at Hogwarts feasts originated with Hufflepuff.'
  },
  {
    'name': 'Donaghan Tremlett',
    'info': 'Donaghan Tremlett was born in 1972 to non-wizarding parents. A graduate of Hogwarts, he plays the bass guitar with the popular \
    wizarding band called the Weird Sisters. Donaghan is a big fan of the Quidditch team called the Kenmare Kestrels.'
  },
  {
    'name': 'Gringott',
    'info': 'Founder of Gringotts wizard bank.'
  },
  {
    'name': 'Leopoldina Smethwyck',
    'info': 'First British witch to referee a Quidditch match'
  },
  {
    'name': 'Paracelsus',
    'info': 'Contemporary of Copernicus and Leonardo Da Vinci, a medical genius whose bold theories Challenged medieval thought. Credited with \
    discovering Parseltongue.'
  },
  {
    'name': 'Goliath',
    'info': 'Mercenary giant used by the Philistines in their war with the Israelites. Was slain by a young boy with a slingshot.'
  },
  {
    'name': 'Babayaga',
    'info' : 'Russia hag who dwelled in a hut that stood on giant chicken legs. Ate children for breakfast - and presumably for lunch and tea.'
  },
  {
    'name': 'Count Vlad Drakul',
    'info' : 'Notorious vampire who inspired the fictional Count Dracula created by Bram Stoker. Father of Vlad the Impaler.'
  }
]

houses = ['5a05e2b252f721a3cf2ea33f',   #Gryffindor
         '5a05da69d45bd0a11bd5e06f',    #Ravenclaw
         '5a05dc8cd45bd0a11bd5e071',    #Slytherin
         '5a05dc58d45bd0a11bd5e070']    #Hufflepuff

key = '$2a$10$nTxqS397nOQ5rnKbsC64K.UtL5RupVMqoVD59oqymkBq5PX9qg9y6'

base_key = '?key=' + key
base_url = 'https://www.potterapi.com/v1/'

@app.route('/') # the method is GET by default
def home():
    return 'Hello, World', 200

@app.route('/chocolate-frog')
def getChocolateFrog():
    return random.choice(wizards)
  

@app.route('/ministry-of-magic')
def getMinistryOfMagic():
    result = requests.get(base_url + 'characters' + base_key + '&ministryOfMagic=true')
    return make_response(jsonify(result.json()))

@app.route('/death-eaters')
def getDeathEat():
    result = requests.get(base_url + 'characters' + base_key + '&deathEater=true')
    return make_response(jsonify(result.json()))

@app.route('/order-of-the-phoenix')
def getOrderOfThePhoenix():
    result = requests.get(base_url + 'characters' + base_key + '&orderOfThePhoenix=true')
    return make_response(jsonify(result.json()))

@app.route('/dumbledores-army')
def getDumbledoresArmy():
    result = requests.get(base_url + 'characters' + base_key + '&dumbledoresArmy=true')
    return make_response(jsonify(result.json()))

@app.route('/hogwarts-house')
def getHogwartsHouse():
    house_id = random.choice(houses)
    result = requests.get(base_url + 'houses/' + house_id + base_key)
    return make_response(jsonify(result.json()))
    

if __name__ == '__main__':
    app.run(debug=True)
