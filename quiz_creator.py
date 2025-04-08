#make a function that asks user for a question, choices for the question, and the answer
def quiz_maker():
    while True:
        question = input("Enter the question: ")
        choices = {}
        labels = ['a', 'b', 'c', 'd']
        for label in labels:
            choice = input(f"Enter choice {label}: ")
            choices[label] = choice
#save the question, choices, and answer to a text file
#ask the user if they want to add another question           
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
#repeat until the user says no
#call the function
quiz_maker()