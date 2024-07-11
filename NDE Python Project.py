import random
import json
import tqdm
import time

# List of funny sayings for wrong answers
funny_sayings = [
    "Oops! Looks like you laid an egg.",
    "Wrong answer, but at least you tried to wing it!",
    "Not quite! Are you just winging it?",
    "That's a foul guess!",
    "Peck again, bird brain!"
]


def print_welcome():
    welcome_message = """
    *******************************************************
           Welcome to the State Symbol Guessing Game! 
    *******************************************************
    Let's explore the state symbols of the United States!
    """
    print(welcome_message)


# Dictionary of state birds with short facts
def bird_data():
    with open('state_birds.txt', 'r') as file:
        return json.loads(file.read())


def get_data_for_question(nest):
    state = random.choice(list(nest.keys()))
    bird_info = nest.get(state)
    correct_bird = bird_info.get("bird")
    fact = bird_info.get("fact")
    return state, bird_info, correct_bird, fact


def get_multiple_choice_options(correct_bird, nest):
    all_birds = [info["bird"] for info in nest.values()]
    options = random.sample(all_birds, 4)
    if correct_bird not in options:
        options[random.randint(0, 2)] = correct_bird
    random.shuffle(options)
    return options


def main():
    print_welcome()
    nest = bird_data()

    while True:
        state, bird_info, correct_bird, fact = get_data_for_question(nest)
        options = get_multiple_choice_options(correct_bird, nest)

        print(f"What is the state bird of {state}?")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        guess = input("Enter the number of your choice: ")

        for i in tqdm.tqdm(range(2)):
            time.sleep(0.5)

        if options[int(guess) - 1] != correct_bird:
            print(random.choice(funny_sayings))
        else:
            print(f"Correct! The state bird of {state} is the {correct_bird}. Fun Fact: {fact}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    main()