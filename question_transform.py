import vectors_of_words
import numpy

def create_vector(content, bag_of_words):
    words = vectors_of_words.find_words(content)
    vector = [0 for _ in range(len(bag_of_words))]
    for word in words:
        if word in bag_of_words:
            vector[bag_of_words.index(word)] += 1
    return vector

def calc_corelation(content,matrix):

