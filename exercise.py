import json

def load_abbreviations():
    try:
        with open('abbreviations.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_abbreviations(abbreviations):
    with open('abbreviations.json', 'w') as file:
        json.dump(abbreviations, file, indent=4)

def translate_abbreviation(abbreviation, abbreviations):
    if abbreviation in abbreviations:
        return abbreviations[abbreviation]
    else:
        return "No meaning found for the abbreviation."

def add_abbreviation(abbreviation, meaning, abbreviations):
    abbreviations[abbreviation] = meaning
    save_abbreviations(abbreviations)
    print(f"Added '{abbreviation}' with meaning '{meaning}'.")

abbreviations = load_abbreviations()

while True:
    user_input = input("Enter an abbreviation (or 'q' to quit): \n")
    if user_input == 'q':
        break
    
    if user_input in abbreviations:
        print(f"Meaning: {abbreviations[user_input]}")
    else:
        meaning = input("Meaning not found. Enter the meaning: ")
        add_abbreviation(user_input, meaning, abbreviations)

    

