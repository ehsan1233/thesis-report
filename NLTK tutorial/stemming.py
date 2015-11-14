# stemming is to finding the root of words. 

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# # having stem of words in list
# example_words = ["Python","pythoning","pythoned"]

# for w in example_words:
# 	print(ps.stem(w))


# to stemming words in a sentence
new_text = "it is very important to be regular and regularity is important like importantly acting like people"
words = word_tokenize(new_text)

for z in words:
	print(ps.stem(z))