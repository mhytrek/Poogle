import math
import os
import pickle
import re
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.preprocessing import normalize
# nltk.download('stopwords')

def find_words(content):
    ps = PorterStemmer()
    words = re.split(r'[\s|,|\.|=|;|"|:|\(|\)|\{|\}|\[|\]|?|!]+', content)
    words = list(map(ps.stem, words))
    return words

def all_files_vector():
    voc = set()
    for file_name in os.listdir("test"):
        file_path = os.path.join("test", file_name)
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
    documents = []
    for file_name in os.listdir("test"):
        vec = [0 for _ in range(len(bag_of_word))]
        file_path = os.path.join("test", file_name)
        with open(file_path, 'rb') as file_opened:
            obj = pickle.load(file_opened)
            content = obj.get('content')
            words = find_words(content)
            documents.append({'title': obj.get('title'), 'url': obj.get('url')})
        for word in words:
            if word in bag_of_word:
                if vec[bag_of_word.index(word)] == 0:
                    document_freq[bag_of_word.index(word)] += 1
                vec[bag_of_word.index(word)] += 1
        matrix.append(np.array(vec, dtype=object))
    for col in range(N):
        idf = math.log(len(matrix)/document_freq[col])
        for i in range(len(matrix)):
            matrix[i][col] *= idf
    matrix = np.array(matrix, dtype=object)
    normalized_matrix = normalize(matrix,axis=1, norm='l1')
    normalized_matrix = normalized_matrix.T
    document_freq = np.array(document_freq)

    file_handler = open("Data/Articles_test_data", "wb")
    A = {'matrix': normalized_matrix,
         'frequency': document_freq,
         'bagofwords': bag_of_word,
         'articles': documents,
         }
    pickle.dump(A, file_handler)
    file_handler.close()
    return



def main():
    bag = bag_of_words()
    matrix = find_articles_vector(bag)
    return len(bag)

print(main())