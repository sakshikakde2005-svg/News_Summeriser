import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))

def clean_text(text):
    """
    Remove punctuation and convert text to lowercase
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def tokenize_words(text):
    """
    Tokenize words from text
    """
    words = word_tokenize(text)
    filtered_words = []

    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    return filtered_words


def tokenize_sentences(text):
    """
    Tokenize sentences
    """
    sentences = sent_tokenize(text)
    return sentences