import sys


def getQuestions():
    # questions, answers = [], []
    with open('quiz.txt') as f:
        lines = f.readlines()
        # for i, line in enumerate(f):
        #   answers.append(line.strip()) if i % 2 else questions.append(line.strip())
        # return zip(questions, answers)

    return [(lines[i], lines[i + 1].strip()) for i in range(0, len(lines), 2)]


try:
    questions = getQuestions()
except IOError:
    print 'Error : Question file not found.'
    sys.exit()
except IndexError as ie:
    print 'Error :  Reading questions file :  %s' % ie
    sys.exit()


def within2Characters(s1, s2):
    if len(s1) != len(s2):
        return False;

    difference = 0
    for x, y in zip(s1, s2):
        if x != y:
            difference += 1

    return False if difference > 2 else True


score = 0
total = len(questions)

for question, answer in questions:
    tries = 3

    while tries > 0:
        guess = raw_input(question)
        tries -=1
        if guess == "":
            print 'Enter was hit'
            guess = raw_input(question)

        # if guess == answer:
        if within2Characters(guess, answer):
            score += 1
            break
        elif tries > 0:
            print 'Nope. %s more tries' % tries

print 'You got %s out of %s questions correct' % (score, total)
