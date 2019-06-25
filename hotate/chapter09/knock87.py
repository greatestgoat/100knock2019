from sklearn.metrics.pairwise import cosine_similarity
from sklearn.externals import joblib
import numpy as np


def main():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    united = pca[vocab['United_States'.lower()]]
    us = pca[vocab['U.S'.lower()]]
    cs = cosine_similarity(np.reshape(united, (1, -1)), np.reshape(us, (1, -1)))
    print(cs)


if __name__ == '__main__':
    main()

# [[0.825936]]