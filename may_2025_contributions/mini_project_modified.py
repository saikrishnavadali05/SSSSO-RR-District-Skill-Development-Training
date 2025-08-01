import random

def mad_libs():
    funny_templates = [
        "{name} slipped on a {food}, launched {plural_noun}, screamed '{exclamation}'!",
        "At the zoo, a {animal} stole my {object} and danced.",
        "{name} did the {silly_dance}, fell into a {place}, laughing.",
        "He opened the door, saw {plural_noun}, and yelled '{exclamation}'!",
        "{name} cooked spaghetti with a {animal}, wore {object}, won MasterChef.",
        "{name} rode a {vehicle} into a {place}, yelling '{exclamation}'!"
    ]

    selected_template = random.choice(funny_templates)

    
    inputs = {}

    if '{name}' in selected_template:
        inputs['name'] = input("Enter a name: ")

    if '{food}' in selected_template:
        inputs['food'] = input("Enter a food: ")

    if '{plural_noun}' in selected_template:
        inputs['plural_noun'] = input("Enter a plural noun: ")

    if '{exclamation}' in selected_template:
        inputs['exclamation'] = input("Enter an exclamation (e.g., Yikes!): ")

    if '{animal}' in selected_template:
        inputs['animal'] = input("Enter an animal: ")

    if '{object}' in selected_template:
        inputs['object'] = input("Enter an object: ")

    if '{silly_dance}' in selected_template:
        inputs['silly_dance'] = input("Enter a silly dance: ")

    if '{place}' in selected_template:
        inputs['place'] = input("Enter a place: ")

    if '{vehicle}' in selected_template:
        inputs['vehicle'] = input("Enter a vehicle: ")

    story = selected_template.format(**inputs)

    print("\n Your Mad Libs Story:\n")
    print(story)

mad_libs()

