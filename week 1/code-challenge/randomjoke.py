import random

def random_joke_generator():
    jokes = [
        "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "How do you comfort a JavaScript bug? You console it!",
        "Why do Python programmers prefer using snakes? Because they can handle exceptions!",
        "Why was the developer unhappy at their job? They wanted arrays!"
    ]

    joke = random.choice(jokes)
    print("Here's a joke for you:")
    print(joke)

    play_again = input("Do you want to hear another joke? (yes/no): ").strip().lower()
    if play_again == "yes":
        random_joke_generator()

random_joke_generator()
