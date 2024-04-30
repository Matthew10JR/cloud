import nltk
from collections import Counter
nltk.download('stopwords')
file_path = "paragraphs.txt"
with open(file_path, 'r') as file:
    text = file.read()
words = [word.lower() for word in text.split()]
stopwords = nltk.corpus.stopwords.words('english')
filtered_words = [word for word in words if word not in stopwords]
word_counts = Counter(filtered_words)
print("Word Frequency Count:")
for word, count in word_counts.items():
    print(f"{word}: {count}")