from sklearn.metrics.pairwise import cosine_similarity

from SimilarityArrayUtils import fix_shape


class CosineSimilarityCalculator:

    def calculate_similarity(self, x, y):
        x, y = fix_shape(x, y)
        return cosine_similarity(x.reshape(1, -1), y.reshape(1, -1))
