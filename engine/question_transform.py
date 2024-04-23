import vectors_of_words
import numpy as np
import pickle

def create_vector(content, bag_of_words):
    words = vectors_of_words.find_words(content)
    vector = [0 for _ in range(len(bag_of_words))]
    for word in words:
        if word in bag_of_words:
            vector[bag_of_words.index(word)] += 1
    return np.array(vector)

def calc_corelation(q,A):
    similarity = q.T @ A
    return similarity

def calc_corelation_with_svd(g,svd):
    return g @ svd.get('S') @ svd.get('D') @ svd.get('V')

def get_most_similar(cor, doc,n):
    result = sorted(doc, key=lambda x: cor[doc.index(x)], reverse=True)
    table = []
    for i in range(min(n,len(doc))):
        table.append(result[i])
    return table



