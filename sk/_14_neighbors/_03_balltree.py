import numpy as np
import pickle
from sklearn.neighbors import BallTree
import datetime

np.random.seed(0)
X = np.random.random((80000, 2048))  # 10 points in 3 dimensions
print('开始建树')
t = datetime.datetime.now()
tree = BallTree(X, leaf_size=2)
print('建树：',(datetime.datetime.now()-t))

t = datetime.datetime.now()
s = pickle.dumps(tree)
print('存：',(datetime.datetime.now()-t))

t = datetime.datetime.now()
tree_copy = pickle.loads(s)
print('取：',(datetime.datetime.now()-t))

t = datetime.datetime.now()
for i in range(100):
    dist, ind = tree_copy.query([X[0]], k=3)
print('查：',(datetime.datetime.now()-t))
print (ind)  # indices of 3 closest neighbors
print (dist ) # distances to 3 closest neighbors