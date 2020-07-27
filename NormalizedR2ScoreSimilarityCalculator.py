from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler

from SimilarityArrayUtils import fix_shape


class NormalizedR2ScoreSimilarityCalculator:

    def calculate_similarity(self, x, y):
        x, y = fix_shape(x, y)

        x = MinMaxScaler().fit_transform(x.reshape(-1, 1))
        y = MinMaxScaler().fit_transform(y.reshape(-1, 1))
        return r2_score(x, y)
