import pickle
from question_transform import *
class Search_engine:
    def __init__(self):
        file_handler = open("Data/Articles_data_polandk=100", "rb")
        data = pickle.load(file_handler)
        self.matrix = data.get('matrix')
        self.documents = data.get('articles')
        self.bag_of_words = data.get('bagofwords')
        self.svd_matrix = data.get('svd')
        print(len(self.bag_of_words))
        file_handler.close()

    def search(self, q, n=10, svd=True):
        q_vec = create_vector(q, self.bag_of_words)
        if svd:
            cos = calc_corelation_with_svd(q_vec, self.svd_matrix)
        else:
            cos = calc_corelation(q_vec, self.matrix)
        return get_most_similar(cos, self.documents, n)



def main():
    engine = Search_engine()
    while(True):
        question = input("Ask me question about Poland:\n")
        engine.search(question)

if __name__ == '__main__':
    main()
