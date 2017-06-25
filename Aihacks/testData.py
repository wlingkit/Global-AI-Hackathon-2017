from sklearn.datasets import fetch_20newsgroups
categories = ['alt.atheism', 'soc.religion.christian',
               'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories)
print(twenty_train.data)
