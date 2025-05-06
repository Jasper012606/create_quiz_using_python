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
load_quiz()