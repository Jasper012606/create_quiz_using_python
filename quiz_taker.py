#make a function that loads and runs the quiz file
def load_quiz():
    #check if the file exists
    try:
        #if true, proceed to load the file
        with open("quiz.txt", "r") as quiz_file:
            #read the file line by line
            lines = quiz_file.readlines()
            
    #else, notice the user that the file does not exist
    except FileNotFoundError:
        print("Quiz file not found. Please Create a Quiz first.")
        return
    #initialize the score, total questions and number of lines to 0
    score = 0
    total_questions = 0
    number_of_lines = 0
    
    #look for the line that starts with "Question:"
    while number_of_lines < len(lines):
        line = lines[number_of_lines].strip()
        #check if the line starts with "Question:", proceed if true
        if line.startswith("Question:"):
            #add 1 to the total questions
            total_questions += 1
            #print the question
            question = line.strip().replace("Question:", f"Question {total_questions}:").strip()
            print(f"{question}")
        
        #make an empty dictionary to store the choices and labels
            choices = {}
            for i in range(1, 5):
                labels, choice = lines[number_of_lines + i].strip().split(".", 1)
                choices[labels.lower()] = choice
                print(f"{labels}. {choice}")
            
            #look for the correct answer in the file
            correct_answer = lines[number_of_lines + 5]
            correct_label = correct_answer.split(":")[1].strip().split(".")[0]
            correct_choice = correct_answer.split(".")[1]

        #ask the user for the answer
            #check if the answer is valid
            while True:
                ask_user = input ("Enter your answer (a/b/c/d): ").strip().lower()
                #if answer is not in choices, ask the user to enter a valid answer
                if ask_user not in choices:
                    print("Invalid answer. Please choose among the choices (a/b/c/d) only.")
                    continue
                #if answer is valid and correct, add 1 to the score and prooceed to the next question
                if ask_user == correct_label:
                    print(f"Correct!✅\n")
                    score += 1
                    break
                #if answer is wrong, print the correct answer and proceed to the next question
                else:
                    print(f"Wrong!❌ The correct answer is {correct_label}.{correct_choice}")
                    break
                
            #Add 5 to the number of lines to move to the next question
            number_of_lines += 5
            
        #if the line does not start with "Question:", skip the line
        else:
            number_of_lines += 1
load_quiz()