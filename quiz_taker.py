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
    
    while number_of_lines < len(lines):
        line = lines[number_of_lines].strip()
        #check if the line starts with "Question:", proceed if true
        if line.startswith("Question:"):
            #add 1 to the total questions
            total_questions += 1
            #print the question
            question = line.strip().replace("Question:", f"Question {total_questions}:").strip()
            print(f"\n{question}")
            break
        
load_quiz()