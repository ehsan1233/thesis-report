import nltk
import random 
from nltk.corpus import movie_reviews

from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

documents = [(list(movie_reviews.words(fileid)), category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

def find_features(document):
	words = set (document)
	features ={}
	for w in word_features:
		features[w] =(w in words)

	return features

#print((find_features(movie_reviews.words("neg/cv000_29416.txt"))))

featuresets = [(find_features(rev),category) for (rev,category) in documents]

#starts from here 
training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classirier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Algo accuracy percentage:", (nltk.classify.accuracy(classirier, testing_set))*100)
classirier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB accuracy percentage:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)


# #Gaussian 
# GNB_classifier = SklearnClassifier(GaussianNB())
# GNB_classifier.train(training_set)
# print("GNB accuracy percentage:", (nltk.classify.accuracy(GNB_classifier, testing_set))*100)

#Bernaulli 
BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BNB accuracy percentage:", (nltk.classify.accuracy(BNB_classifier, testing_set))*100)

#LogisticRegression 
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression accuracy percentage:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

#SGDClassifier
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier accuracy percentage:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

#SVC 
SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC accuracy percentage:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

#LinearSVC 
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC accuracy percentage:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

#NuSVC 
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC accuracy percentage:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)



