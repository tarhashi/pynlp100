# -*- coding:utf-8 -*-
from scipy import sparse, io
from sklearn.decomposition import TruncatedSVD

X = io.loadmat('ppmi_matrix')['X']
pca = TruncatedSVD(n_components=300)
X_300 = pca.fit_transform(X)
io.savemat('X_300', {'X_300':X_300})
