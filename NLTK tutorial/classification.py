#text classification useful for situation when we have 2 cases. like positive or negative 
import nltk
import random 
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
			for category in movie_reviews.categories()
			for fileid in movie_reviews.fileids(category)]

#same like above
# documents = []
# for category in movie_reviews.categories():
# 	for fileid in movie_reviews.fileids(category):
# 		documents.append(list(movie_reviews.words(fileid)),category)

random.shuffle(documents)
#print(documents[1])


#to show most common words
all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))

#show how many times the word has written
print(all_words["stupid"])

