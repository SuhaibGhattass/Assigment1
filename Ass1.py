import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


nltk.download("stopwords")
nltk.download('punkt')

# Read text file
text_file = open('paragraphs.txt', 'r')
text = text_file.read()
text_file.close()

word = word_tokenize(text)

# lowering each word
lower_words = [word.lower() for word in word]

stop_words = set(stopwords.words("english"))

without_stopwords = [word for word in lower_words if word not in stop_words]

# freq of each word using counter
frequency_word = Counter(without_stopwords)
print(frequency_word)

filtered_text = ' '.join(without_stopwords)