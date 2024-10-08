import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# Initialize the WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

def tokenize(sentence):
    """
    Split sentence into an array of words/tokens
    """
    return nltk.word_tokenize(sentence)

def stem(word):
    """
    Lemmatize a word using WordNet Lemmatizer
    """
    return lemmatizer.lemmatize(word.lower())

def bag_of_words(tokenized_sentence, words):
    """
    Return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    """
    # Lemmatize each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # Initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
