# coding=utf-8
#================================================================
#
#   File name   : faiss_demo.py
#   Author      : Faye
#   Created date: 2021/4/17 16:23 
#   Description :
#
#================================================================

import numpy as np
import faiss
import time

def demo1():
    d = 2048  # dimension
    nb = 2  # database size
    nq = 1  # nb of queries

    np.random.seed(1234)  # make reproducible
    xb = np.random.random((nb, d)).astype('float32')
    xb[:, 0] += np.arange(nb) / 1000.

    xq = np.random.random((nq, d)).astype('float32')
    xq[:, 0] += np.arange(nq) / 1000.

    index = faiss.IndexFlatL2(d)
    print(index.is_trained)

    index.add(xb)
    xb1 = np.random.random((nb, d)).astype('float32')
    xb1[:, 0] += np.arange(nb) / 1000.
    # index.add(xb1)
    print(index.ntotal)
    k = 4  # we want to see 4 nearest neighbors
    D, I = index.search(xq, k)  # sanity check
    print("I: ", I)

def demo2():
    data = [
        [1.,1.,1.,1.],
        [2.,2.,2.,2.],
        [3.,3.,3.,3.]
    ]
    data = np.asarray(data).astype('float32')

    data1 = [
        [4., 4., 4., 4.]
    ]
    data1 = np.asarray(data1).astype('float32')

    index = faiss.IndexFlatL2(4)
    print(index.is_trained)
    index.add(data)
    D, I = index.search(data1, 2)  # sanity check
    print("d:", D)
    print("I: ", I)

    ri = [1,2]
    ri = np.asarray(ri)
    index.remove_ids(np.arange(1).astype('int64'))
    D, I = index.search(data1, 2)  # sanity check
    print("d:", D)
    print("I: ", I)

def demo3():
    d = 512
    data = np.random.random((1000000, d)).astype('float32')
    index = faiss.IndexFlatL2(d)
    print(index.is_trained)
    t = time.time()
    for i in data:
        index.add(i[np.newaxis, :])
    print('add:', time.time() - t)
    t = time.time()
    D, I = index.search(data[0:1, :], 10)  # sanity check
    print('search:', time.time() - t)
    print("d:", D)
    print("I: ", I)

if __name__ == '__main__':
    demo3()