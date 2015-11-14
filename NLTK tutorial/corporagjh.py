from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample_text = gutenberg.raw("bible-kjv.txt")
tokenized = sent_tokenize(sample_text)

print(tokenized[5:15])

#address of nltk corpus is C:\Users\User\AppData\Roaming\nltk_data\corpora
