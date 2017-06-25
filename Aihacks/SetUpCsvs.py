import Aihacks.JokeParser as jp
import Aihacks.SnippletsParser as sp
import csv


from nltk.corpus import stopwords
stop = stopwords.words("english")


jokes = jp.GetJokes()
print(jokes)

tags = sp.GetTags()
questions, QAs = [], []
with open('questions.csv', 'w') as csvfile:
    writer = csv.writer(csvfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for tag in tags:
        if str(tag) == "relationships\\": continue
        question = sp.GetQuestionLinksFromTag(str(tag))
        questions = questions + question
        for quest in question:
            if quest.endswith('.htm'):
                writer.writerow([quest])

with open('snipplets.csv', 'w') as csvfile2:
    writer = csv.writer(csvfile2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    with open('questions.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 0: continue
            Q,A = sp.GetQuestionAndAnswer(row[0])
            writer.writerow([Q,A])

allQuestions = []
with open('snipplets.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) == 0: continue
        words = row[0].lower().split()
        words = [w for w in words if not w in stopwords.words("english")]
        allQuestions.append(words)

print(allQuestions)
