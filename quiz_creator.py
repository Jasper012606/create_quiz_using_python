#make a function that asks user for a question, choices for the question, and the answer
def quiz_maker():
    while True:
        question = input("Enter the question: ")
        choices = {}
        labels = ['a', 'b', 'c', 'd']
#save the question, choices, and answer to a text file
#ask the user if they want to add another question
#repeat until the user says no
#call the function
quiz_maker()