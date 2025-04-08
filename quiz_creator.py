#make a function that asks user for a question, choices for the question, and the answer
def quiz_maker():
    while True:
        question = input("Enter the question: ")
        choices = {}
        labels = ['a', 'b', 'c', 'd']
        for label in labels:
            choice = input(f"Enter choice {label}: ")
            choices[label] = choice
        while True:
            correct_answer = input("Enter the correct answer: ").strip().lower()
            if correct_answer not in choices and correct_answer not in choices.values():
                print("Invalid answer. Please enter a valid choice (a/b/c/d).")
                continue
            else:
                break
#save the question, choices, and answer to a text file
#ask the user if they want to add another question 
    #repeat until the user says no          
        while True:
            another_question = input("Do you want to add another question? (y/n): ").strip().lower()
            if another_question == 'y':
                break
            elif another_question == 'n':
                print("Exiting the quiz maker.")
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue
#call the function
quiz_maker()