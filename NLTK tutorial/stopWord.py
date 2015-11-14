from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentiment_example = " Hello people. today is the day that I told you I am going to talk to you about history."
stop_words = set(stopwords.words("english"))
words = word_tokenize(sentiment_example)

#remove stop words from text
filtered = []
for w in words:
	if w not in stop_words:
		filtered.append(w)

print(filtered)

# does the same functionality
# filtered = [w for w in words if not w in stop_words]
# print(filtered)


#to show stop words on each language
# print(stop_words)


