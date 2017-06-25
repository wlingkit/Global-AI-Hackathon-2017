import csv
from nltk.corpus import stopwords
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


stop = stopwords.words("english")

rows = []
ranks = []

with open('trainerdatav2.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == ' ' or row[0] == '': continue
        ranks.append(row[1])
        words = row[0].lower().split()
        words = [w for w in words if not w in stopwords.words("english")]
        rows.append(" ".join(words))



# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.
vectorizer = CountVectorizer(analyzer = "word",
                             tokenizer = None,
                             preprocessor = None,
                             stop_words = None,
                             max_features = 5000)

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of
# strings.

train_data_features = vectorizer.fit_transform(rows)

# Numpy arrays are easy to work with, so convert the result to an
# array
train_data_features = train_data_features.toarray()
print(train_data_features.shape)

# vocab = vectorizer.get_feature_names()
#
#
# # Sum up the counts of each vocabulary word
# dist = np.sum(train_data_features, axis=0)
#
# # For each, print the vocabulary word and the number of times it
# # appears in the training set
# for tag, count in zip(vocab, dist):
#     print count, tag

forest = RandomForestClassifier(n_estimators = 100)
forest.fit( train_data_features, ranks)

## now we have fitted and to test the data
with open('testdatav2.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == ' ' or row[0] == '': continue
        ranks.append(row[1])
        words = row[0].lower().split()
        words = [w for w in words if not w in stopwords.words("english")]
        rows.append(" ".join(words))

# Get a bag of words for the test set, and convert to a numpy array
print(rows)
test_data_features = vectorizer.transform(rows)
test_data_features = test_data_features.toarray()

# Use the random forest to make sentiment label predictions
print(test_data_features)
result = forest.predict(test_data_features)
print(result)