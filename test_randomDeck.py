import pytest
import randomDeck


def test_getCards():
    colors = ['red', 'blue', 'black', 'green', 'white']
    types = ['creature', 'instant', 'sorcery', 'enchantment']
    for color in colors:
        for type in types:
            cards = randomDeck.getCards(color,type,8)
            assert len(cards) == 8
            assert randomDeck.getCards(color,type,8) != randomDeck.getCards(color,type,8)
