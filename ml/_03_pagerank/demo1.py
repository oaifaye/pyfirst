'''
Created on 2018年11月25日

'''

import numpy as np

P=[
   [0.0,1/2,1/2,1/2],
   [1/3,0.0,0.0,0.0],
   [1/3,0.0,0.0,1/2],
   [1/3,1/2,1/2,0.0]
   ]

P=[
   [0.0,0.0,1/2,0.0],
   [1/3,0.0,0.0,1.0],
   [1/3,0.0,0.0,0.0],
   [1/3,1.0,1/2,0.0]
   ]

P=[
[0.0,1/2,1/2,1/2,1/2,0.0],
[0.0,0.0,1/2,0.0,0.0,0.0],
[0.0,1/2,0.0,0.0,0.0,0.0],
[1/3,0.0,0.0,0.0,1/2,0.0],
[1/3,0.0,0.0,1/2,0.0,0.0],
[1/3,0.0,0.0,0.0,0.0,0.0],
]
P = np.array(P)

# A=[[1],[1],[1],[1]]

alapha = 0.85
N = P.shape[0]

A=[[1/N],[1/N],[1/N],[1/N],[1/N],[1/N]]
A= np.array(A)

A1=[[1/N],[1/N],[1/N],[1/N],[1/N],[1/N]]
A1= np.array(A1)

print(N)
I = np.identity(N) #单位矩阵
for i in range(10):
    # A = [(alapha/N)*I + (1-alapha)*P]*A
#     A = np.dot(np.dot(alapha/N,I) + np.dot((1 - alapha) , P),A)
    A = alapha * np.dot(P,A) + (1-alapha)*A
    A1= np.dot(P,A1)
print(A)
print(A1)