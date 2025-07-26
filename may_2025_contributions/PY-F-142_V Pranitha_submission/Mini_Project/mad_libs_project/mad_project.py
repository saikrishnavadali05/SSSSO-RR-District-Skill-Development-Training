from flask import Flask, render_template, request, redirect, url_for, session
import random
import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)
app.secret_key = 'madlibs_secret'

funny_templates = [
    "{name} slipped on a {food}, launched {plural_noun}, screamed '{exclamation}'!",
    "At the zoo, a {animal} stole my {object} and danced.",
    "{name} did the {silly_dance}, fell into a {place}, laughing.",
    "He opened the door, saw {plural_noun}, and yelled '{exclamation}'!",
    "{name} cooked spaghetti with a {animal}, wore {object}, won MasterChef.",
    "{name} rode a {vehicle} into a {place}, yelling '{exclamation}'!"
]

def is_animal(word):
    return any("animal" in lemma.name() for syn in wn.synsets(word, pos=wn.NOUN)
               for hyper in syn.closure(lambda s: s.hypernyms()) for lemma in hyper.lemmas())

def is_food(word):
    return any("food" in lemma.name() or "nutrient" in lemma.name() for syn in wn.synsets(word, pos=wn.NOUN)
               for hyper in syn.closure(lambda s: s.hypernyms()) for lemma in hyper.lemmas())

def is_object(word):
    return any("artifact" in lemma.name() for syn in wn.synsets(word, pos=wn.NOUN)
               for hyper in syn.closure(lambda s: s.hypernyms()) for lemma in hyper.lemmas())

def is_place(word):
    return True  

def is_vehicle(word):
    return any("vehicle" in lemma.name() or "conveyance" in lemma.name() for syn in wn.synsets(word, pos=wn.NOUN)
               for hyper in syn.closure(lambda s: s.hypernyms()) for lemma in hyper.lemmas())

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/madlibs', methods=['GET', 'POST'])
def madlibs():
    error = None
    if request.method == 'POST':
        data = request.form
        animal = data.get('animal', '')
        food = data.get('food', '')
        object_ = data.get('object', '')
        place = data.get('place', '')
        vehicle = data.get('vehicle', '')

        if not is_animal(animal):
            error = "Please enter a valid animal."
        elif not is_food(food):
            error = "Please enter a valid food."
        elif not is_object(object_):
            error = "Please enter a valid object."
        elif not is_place(place):
            error = "Please enter a valid place."
        elif not is_vehicle(vehicle):
            error = "Please enter a valid vehicle."

        if error:
            return render_template('madlibs.html', error=error)

        template = random.choice(funny_templates)
        story_text = template.format(
            name=data.get('name', 'Someone'),
            food=food,
            plural_noun=data.get('plural_noun', 'cats'),
            exclamation=data.get('exclamation', 'Wow'),
            animal=animal,
            object=object_,
            silly_dance=data.get('silly_dance', 'floss'),
            place=place,
            vehicle=vehicle
        )

        session['story'] = story_text
        return redirect(url_for('story_page'))  

    return render_template('madlibs.html', error=error)

@app.route('/story')
def story_page():  
    story = session.get('story', "No story found.")
    return render_template('story.html', story=story)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
