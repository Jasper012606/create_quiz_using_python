#make a function that asks user for a question, choices for the question, and the answer
def quiz_maker():
    while True:
        question = input("Enter the question: ").capitalize()
        
        #check if the question is too short or empty
        if len(question) < 10:
            print("Question is too short. Please enter a longer question.")
            continue
        if question.strip() == "":
            print("Please enter a question.")
            continue
        
        choices = {}
        labels = ['a', 'b', 'c', 'd']
        
        #Ask the user for choices
        for label in labels:
            choice = input(f"Enter choice {label}: ")
            choices[label] = choice
        
        #Ask the user for the correct answer
        while True:
            correct_answer = input("Enter the correct answer(a/b/c/d): ").strip().lower()
            #check if the answer is valid
            if correct_answer not in choices:
                print("Invalid answer. Please enter a valid choice (a/b/c/d).")
                continue
            else:
                break
            
    #save the question, choices, and answer to a text file
        #create or open a text file
        with open("quiz.txt", "a") as file:
            #write the question and choices to the file
            file.write(f"Question: {question}\n")
            for label in labels:
                file.write(f"{label}. {choices[label]}\n")
            index = labels.index(correct_answer)
            file.write(f"Correct Answer: {labels[index]}. {choices[labels[index]]}\n")
            file.write("------------------------------\n")
            
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