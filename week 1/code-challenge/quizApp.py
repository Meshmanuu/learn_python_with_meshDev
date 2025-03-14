import random
def quiz_game():
    questions={
        "Whos is the president of kenya?": "a",
        "Who is the most corrupt country in Africa?": "b" ,
        "What is kenya capital city?" : "c" ,
        "Who is the opposition leadr in kenya?": "d"

    }
    options={
         "Whos is the president of kenya?": ["a)kasongo yeye","b)El-chapo","c)zakayo","d)Ruto"],
        "Who is the most corrupt country in Africa?": ["a)Meshack","b)Ruto","c)Raila","d)Salasya"],
        "What is kenya capital city?" : ["a)Lodwar","b)Eldoret","c)Nairobi","d)Mlolongo"],
        "Who is the opposition leadr in kenya?": ["a)El-chapo","b)Morara","c)Nuru", "d)Raila"]
    }
    
    score= 0
    for question in questions:
        print(question)
        for option in options[question]:
            print(option)
    answer= input("Your answer (a/b/c/d): ").strip().upper()
    if answer == question[question]:
        score +=1
        print("COrrect!\n")
    else:
        print("wrong youre a fool")
           
    print(f"Your score: {score}/{len(questions)}")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz_game()

quiz_game() 

    