import math
import os
import pickle
import re
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')

def find_words(content):
    ps = PorterStemmer()
    words = re.split(r'[\s|,|\.|=|;|"|:|\(|\)|\{|\}|\[|\]]+', content)
    words = map(ps.stem, words)
    return words

def all_files_vector():
    voc = set()
    for file_name in os.listdir("wiki_articles"):
        file_path = os.path.join("wiki_articles", file_name)
        with open(file_path, 'rb') as file_opened:
            obj = pickle.load(file_opened)
            content = obj.get('content')
            voc = voc.union(find_words(content))
    return voc

def bag_of_words():
    all_words = set(all_files_vector())
    stopwords_set = set(stopwords.words('english'))
    return list(all_words - stopwords_set)

def find_articles_vector(bag_of_word):
    N = len(bag_of_word)
    matrix = []
    document_freq = [0 for _ in range(len(bag_of_word))]
    for file_name in os.listdir("wiki_articles"):
        vec = [0 for _ in range(len(bag_of_word))]
        file_path = os.path.join("wiki_articles", file_name)
        with open(file_path, 'rb') as file_opened:
            obj = pickle.load(file_opened)
            content = obj.get('content')
            words = find_words(content)
        for word in words:
            if word in bag_of_word:
                if vec[bag_of_word.index(word)] == 1:
                    document_freq[bag_of_word.index(word)] += 1
                vec[bag_of_word.index(word)] += 1
        matrix.append(np.array(vec, dtype=object))
    for col in range(len(bag_of_word[0])):
        idf = math.log(N/document_freq[col])
        for i in range(N):
            matrix[i][col] *= idf
    pickle.dump(matrix, "Matrix", "wb")
    return np.array(matrix, dtype=object)



def main():
    bag = bag_of_words()
    matrix = find_articles_vector(bag)
    return len(bag)

print(main())



