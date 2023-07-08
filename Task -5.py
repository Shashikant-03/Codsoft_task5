import random

# Quiz Questions
questions = [
    {
        "question": "Which of the country won FIFA world cop maximum times",
        "options": ["A. Germany", "B. Italy", "C. Argentina", "D. Brazil"],
        "answer": "D"
    },
    {
        "question": " Which programming language is used to create web pages?",
        "options": ["A. Python", "B.HTML", "C. C++", "D.Java"],
        "answer": "B"
    },
    {
        "question": " Which Indian athlete has won the most number of medals in the history of the Asian Games?",
        "options": ["A. Milkha Singh", "B. P.T. Usha", "C.Abhinav Bindra", "D. P.V. Sindhu"],
        "answer": "D"
    }
]

# Display Welcome Message and Rules
def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions.")

# Present Quiz Questions
def present_quiz_questions():
    score = 0
    for i, question in enumerate(questions):
        print(f"Question {i + 1}:")
        print(question["question"])
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ")
        user_answer = user_answer.upper()

        # Evaluate the User's Answer
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("The correct answer is:", question["answer"])
        print()

    return score

# Display Final Results
def display_final_results(score):
    print("Quiz completed!")
    print("Your score:", score)
    if score == len(questions):
        print("Congratulations! You got a perfect score!")
    elif score >= len(questions) / 2:
        print("Well done! You did a good job!")
    else:
        print("Keep practicing! You can do better next time.")
    

# Play Again
def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == "yes"

# Main game loop
def quiz_game():
    display_welcome_message()
    while True:
        score = present_quiz_questions()
        display_final_results(score)
        if not play_again():
            break

# Start the quiz game
quiz_game()
