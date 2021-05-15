'''
    LSHash(局部敏感哈希)
https://blog.csdn.net/sinat_26917383/article/details/70243066
'''

from sklearn.neighbors import LSHForest


# X_train = [[5, 5, 99], [21, 5, 5], [1, 1, 1]]
# X_train1 = [ [8, 9, 1], [6, 10, 2]]
# X_test = [[9, 1, 6], [3, 1, 10], [7, 10, 3]]
X_train = [[1,1], [2,3], [3,2]]
X_test = [[3,3]]
lshf = LSHForest(random_state=42)
lshf.fit(X_train)
# lshf.partial_fit(X_train1)
distances, indices = lshf.kneighbors(X_test, n_neighbors=2)

print('distances',distances)
print('indices',indices)

X_train1 = [[1,1], [3,2], [3,3]]
lshf.partial_fit(X_train1)
distances1, indices1 = lshf.kneighbors(X_test, n_neighbors=2)
# lshf.partial_fit(X_test)
print('distances1',distances1)
print('indices1',indices1)