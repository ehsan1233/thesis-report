# wordNet is the largest capabilitied corpora 

from nltk.corpus import wordnet

syns = wordnet.synsets("devil")

# synset
print(syns[0].name())

# just the word
print(syns[0].lemmas()[0].name())

#definition
print(syns[0].definition())

#example 
print(syns[0].examples())

#to find synonyms and antonyms of a word
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())

print(synonyms)
print(antonyms)





#similarities 

w1 = wordnet.synset("lion.n.01")
w2 = wordnet.synset("cat.n.01")

# the result is % of similarityof these 2 words
print(w1.wup_similarity(w2))


w1 = wordnet.synset("god.n.01")
w2 = wordnet.synset("car.n.01")

# the result is % of similarityof these 2 words
print(w1.wup_similarity(w2))






