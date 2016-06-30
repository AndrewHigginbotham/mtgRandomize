import urllib.request
import json
import flask
import random
app = flask.Flask(__name__)
deck = []

@app.route('/')
def landing():
    return flask.render_template('index.html')
def getCards(color, myType, amount):
    url = 'http://api.deckbrew.com/mtg/cards?color=' + color + \
        '&multicolor=false&format=modern&type=' + myType
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        rawData = json.loads(the_page.decode('utf-8'))
    random.seed()
    cards = []
    for i in range(amount):
        cards.append(rawData[random.randint(0, len(rawData)-1)])
    return cards

@app.route('/<color>Deck')
def monoDeckbuilder(color):

    instants = getCards(color, 'instant', 8)
    creature = getCards(color, 'creature', 12)
    sorceries = getCards(color, 'sorcery', 8)
    enchantment = getCards(color, 'enchantment', 8)

    global deck
    del deck[:]
    deck.append(instants)
    deck.append(sorceries)
    deck.append(creature)
    deck.append(enchantment)
    return flask.render_template('deck.html', deck=deck, color=color)

@app.route('/<color>Deck/list')
def monoDeckbuilderlist(color):
    global deck
    return flask.render_template('names.html', deck=deck)

if __name__ == '__main__':
    app.debug = True
    app.run()
