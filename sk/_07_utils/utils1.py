'''
Created on 2018年12月24日

'''
from sklearn.utils.validation import check_consistent_length
from sklearn.utils.extmath import safe_sparse_dot, randomized_range_finder
import numpy as np

def checkconsistentlength():
    arr = [1,2,3,4,5,6,9]
    arr1 = [1,2,3,4,5,6,9,10]
    res = check_consistent_length(arr,arr1)
    print(res)

def safesparsedot():
    a = np.array([[0,2,3],[4,5,6]])
    b = np.array([[1,0,3],[0,0,6],[0,0,9]])
    c = safe_sparse_dot(a, b, dense_output=True)
    print(c)
# safesparsedot()

def randomizedrangefinder():
    a = np.array([[0,2,3,3,3,3],[4,5,6,6,6,6],[4,5,6,6,6,6]])
    c = randomized_range_finder(a, 3,n_iter=10)
    print(c)
randomizedrangefinder()