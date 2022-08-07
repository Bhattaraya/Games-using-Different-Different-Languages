
print('Welcome to Python  Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Do you have basic concept of python? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of your favourite website for learning Python?')
    if answer.lower()=='greatlearning':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: How many Datatypes are there in java?')
    if answer.lower()=='2':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
    answer=input('Question 3: What does Boolean Datatypes means ?')
    if answer.lower()=='True or false':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')