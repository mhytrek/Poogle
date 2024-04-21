import vectors_of_words
import numpy as np
import pickle

def create_vector(content, bag_of_words):
    words = vectors_of_words.find_words(content)
    print(words)
    vector = [0 for _ in range(len(bag_of_words))]
    for word in words:
        if word in bag_of_words:
            vector[bag_of_words.index(word)] += 1
    return np.array(vector)

def calc_corelation(q,A):
    similarity = q.T @ A
    return similarity

def get_most_similar(cor, doc,n):
    result = sorted(doc, key=lambda x: cor[doc.index(x)], reverse=True)
    for i in range(min(n,len(doc))):
        print(result[i].get('title'))


def search(q):
    file_handler = open("Data/Articles_test_data", "rb")
    data = pickle.load(file_handler)
    bag_of_words = data.get('bagofwords')
    matrix = data.get('matrix')
    documents = data.get('articles')
    q_vec = create_vector(q, bag_of_words)
    cos = calc_corelation(q_vec, matrix)
    get_most_similar(cos, documents, 10)

search("What is Polka?")


