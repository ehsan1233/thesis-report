#defining the noun that the sentencec is about it

import nltk
#unsupervised 
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union 

sample_text = state_union.raw("2006-GWBush.txt")
train_text = state_union.raw("2005-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_contect():
	try:
		for i in tokeniz:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			#we use regular expression and POS 
			chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""

			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			chunked.draw()
			
	except Exception as e:
		print(str(e))

process_contect()