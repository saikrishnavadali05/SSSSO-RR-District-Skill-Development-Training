import json
import random

DB='Flashcards.json'

class FlashCard:
    def __init__(self,term,definition):
        self.term = term
        self.definition=definition

    def to_dict(self):
        return {"term": self.term, "definition": self.definition}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['term'], data['definition'])
    
def load_cards():
    try:
        with open( DB, 'r') as f:
            data=json.load(f)
            return [FlashCard(c["term"],c["definition"]) for c in data]
    except FileNotFoundError:
        return []

def save_cards(cards):
    with open(DB, 'w') as f:
        json.dump([c.to_dict() for c in cards ], f, indent=2)

def add_card(term,definition):
    cards= load_cards()
    cards.append(FlashCard(term,definition))
    save_cards(cards)

def get_all_cards():
    return load_cards()

def get_shuffled_cards():
    cards=load_cards()
    random.shuffle(cards)
    return cards