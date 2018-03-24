def writeQuestion():
    with open('quiz.txt', 'a') as qFile:
        newQuestion = raw_input("What is your question?")
        qFile.writelines(newQuestion + "\n")

        newAnswer = raw_input("What is your answer?")
        qFile.writelines(newAnswer + "\n")


try:
    writeQuestion()
except IOError as ioe:
    print 'File Error : %s' % ioe
except IndexError as ioe:
    print 'Index Error : %s' % ioe

