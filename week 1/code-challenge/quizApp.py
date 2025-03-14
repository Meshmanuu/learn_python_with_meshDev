def quiz_game():
    questions = {
        "Who is the president of Kenya?": "a",
        "Who is the most corrupt country in Africa?": "b",
        "What is Kenya's capital city?": "c",
        "Who is the opposition leader in Kenya?": "d"
    }

    options = {
        "Who is the president of Kenya?": ["a) Kasongo Yeye", "b) El-chapo", "c) Zakayo", "d) Ruto"],
        "Who is the most corrupt country in Africa?": ["a) Meshack", "b) Ruto", "c) Raila", "d) Salasya"],
        "What is Kenya's capital city?": ["a) Lodwar", "b) Eldoret", "c) Nairobi", "d) Mlolongo"],
        "Who is the opposition leader in Kenya?": ["a) El-chapo", "b) Morara", "c) Nuru", "d) Raila"]
    }

    score = 0
    
    # Define the order of questions
    question_list = [
        "Who is the president of Kenya?",
        "Who is the most corrupt country in Africa?",
        "What is Kenya's capital city?",
        "Who is the opposition leader in Kenya?"
    ]

    # Loop through each question in the predefined order
    for question in question_list:
        print(question)  # Print the question
        
        # Print options for the question
        for option in options[question]:  # Use the specific question to access options
            print(option)
        
        answer = input("Your answer (a/b/c/d): ").strip().lower()  # Get user's answer
        
        # Check if the answer is correct
        correct_answer = questions[question]
        if answer == correct_answer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was '{correct_answer}'.\n")
        
        # Print current score after each question
        print(f"Current score: {score}/{len(questions)}\n")

    # Print final score at the end
    print(f"Final score: {score}/{len(questions)}")
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz_game()  # Restart the game if user wants to play again

quiz_game()  # Start the quiz game
