import urllib.request
import json
import flask
import random
app = flask.Flask(__name__)
deck=[]

@app.route('/')
def landing():
	return flask.render_template('index.html')
	
@app.route('/<color>Deck')
def monoDeckbuilder(color):
	url = 'http://api.deckbrew.com/mtg/cards?color=' + color + '&multicolor=false&format=modern&type=instant'
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
		rawData = json.loads(the_page.decode('utf-8'))
	random.seed()
	instants=[]
	for i in range(8):
		instants.append(rawData[random.randint(0,len(rawData)-1)])
	
	url = 'http://api.deckbrew.com/mtg/cards?color=' + color + '&multicolor=false&format=modern&type=sorcery'
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
		rawData = json.loads(the_page.decode('utf-8'))
	random.seed()
	sorceries=[]
	for i in range(8):
		sorceries.append(rawData[random.randint(0,len(rawData)-1)])
	
	url = 'http://api.deckbrew.com/mtg/cards?color=' + color + '&multicolor=false&format=modern&type=creature'
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
		rawData = json.loads(the_page.decode('utf-8'))
	random.seed()
	creature=[]
	for i in range(12):
		creature.append(rawData[random.randint(0,len(rawData)-1)])
	
	url = 'http://api.deckbrew.com/mtg/cards?color=' + color + '&multicolor=false&format=modern&type=enchantment'
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
		rawData = json.loads(the_page.decode('utf-8'))
	random.seed()
	enchantment=[]
	for i in range(8):
		enchantment.append(rawData[random.randint(0,len(rawData)-1)])
	global deck
	del deck[:]
	deck.append(instants)
	deck.append(sorceries)
	deck.append(creature)
	deck.append(enchantment)
	return flask.render_template('deck.html',deck=deck, color=color)
	
@app.route('/<color>Deck/list')
def monoDeckbuilderlist(color):
	global deck
	return flask.render_template('names.html',deck=deck)

if __name__ == '__main__':
    app.debug = True
    app.run()
