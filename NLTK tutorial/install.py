import nltk

#nltk.download()

from nltk.tokenize import sent_tokenize, word_tokenize

sentiment_text = "Hello Ehsan. How are you? What are you doing today? Lets play game!!!"
# print(sent_tokenize(sentiment_text))
# print(word_tokenize(sentiment_text))

for i in word_tokenize(sentiment_text):
	print(i)