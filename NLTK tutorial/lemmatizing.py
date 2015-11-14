 #same as stemming but the end result is real word. 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("better",pos="a"))
# the defult for lemmatize is pos="n" = noun
# more powerfull than stemming

