from bankOfQuestions import Questions
print("\nHello! You Are Here To A True Or False Quiz! You Will Have To Answer 5 Questions Correctly To Win! Good Luck!\n")
correctAnswers = 0

print("\n",Questions.question1)
inputQuestion1 = input("\nAnswer Using True Or False : ")
if inputQuestion1 == "False":
    print("Correct! ",Questions.answer1)
    correctAnswers =correctAnswers+1
if inputQuestion1 == "True":
    "Incorrect! ",Questions.answer1

print("\n",Questions.question2)
inputQuestion2 = input("\nAnswer Using True Or False : ")
if inputQuestion2 == "False":
    print("Correct! ",Questions.answer2)
    correctAnswers =correctAnswers+1
if inputQuestion2 == "True":
    "Incorrect! ",Questions.answer2
    
print("\n",Questions.question3)    
inputQuestion3 = input("\nAnswer Using True Or False : ")
if inputQuestion3 == "False":
    print("Correct! ",Questions.answer3)
    correctAnswers =correctAnswers+1
if inputQuestion3 == "True":
    "Incorrect! ",Questions.answer3
    
print("\n",Questions.question4)
inputQuestion4 = input("\nAnswer Using True Or False : ")
if inputQuestion4 == "True":
    print("Correct! ",Questions.answer4)
    correctAnswers=correctAnswers +1
if inputQuestion4 == "False":
    "Incorrect! ",Questions.answer4
    
print("\n",Questions.question5)    
inputQuestion5 = input("\nAnswer Using True Or False : ")
if inputQuestion5 == "True":
    print("Correct! ",Questions.answer5)
    correctAnswers =correctAnswers+1
    print("Good Job, You Got ",correctAnswers,"/5 Correct Answers")
if inputQuestion5 == "False":
    "Incorrect! ",Questions.answer5
    print("Good Job, You Got ",correctAnswers,"/5 Correct Answers")