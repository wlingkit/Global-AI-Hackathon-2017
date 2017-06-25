import Aihacks.JokeParser as jp
import Aihacks.SnippletsParser as sp
import csv
from sklearn.ensemble import RandomForestClassifier

# jokes = jp.GetJokes()
# print(jokes)

# tags = sp.GetTags()
questions, QAs = [], []
# with open('questions.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     for tag in tags:
#         if str(tag) == "relationships\\": continue
#         question = sp.GetQuestionLinksFromTag(str(tag))
#         questions = questions + question
#         for quest in question:
#             if quest.endswith('.htm'):
#                 writer.writerow([quest])

# with open('snipplets.csv', 'w') as csvfile2:
#     writer = csv.writer(csvfile2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     with open('questions.csv') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             if len(row) == 0: continue
#             Q,A = sp.GetQuestionAndAnswer(row[0])
#             writer.writerow([Q,A])

allQuestions = []
with open('snipplets.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) == 0: continue
        question = [row[0], row[1]]
        allQuestions.append(question)

model = RandomForestClassifier(n_estimators=100, max_features=2)
model.fit(allQuestions, ["true"]*len(allQuestions))

predictions = model.predict(allQuestions[-10:])
print(predictions)


            # with open('snipplets.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     for qa in QAs:
#         writer.writerow(qa)


# for question in questions:
#     QA = sp.GetQuestionAndAnswer(question)
#     QAs.append(QA)
#
# print(QAs)