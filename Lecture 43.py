correctAnswer = 18
userAnswer = 0
answerTimes = 0


while userAnswer != correctAnswer:
    userAnswer = int(input("Input Number 0-100 : "))
    if userAnswer > correctAnswer:
        answerTimes +=1
        print("----------")
        print("Too Large")
        print("Answer",answerTimes,"Times")
    elif userAnswer < correctAnswer:
        answerTimes += 1
        print("----------")
        print("Too Small")
        print("Answer", answerTimes, "Times")
    elif userAnswer == correctAnswer:
        answerTimes += 1
        print("----------")
        print("Correct !!")
        print("Answer", answerTimes, "Times")