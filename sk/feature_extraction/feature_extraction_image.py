'''
Created on 2018年12月22日
https://www.jianshu.com/p/f6e5d1cd21b9
字典学习
'''

import numpy as np
from sklearn.feature_extraction import image
from sklearn.decomposition.dict_learning import MiniBatchDictionaryLearning
from sklearn.feature_extraction.image import reconstruct_from_patches_2d
from sklearn.utils.validation import as_float_array
 
one_image = np.arange(4 * 4 * 1).reshape((4, 4))
# one_image = one_image.astype( "float32")
one_image = as_float_array(one_image)
print('one_image:',one_image) 

# patches = image.extract_patches_2d(one_image, (2, 2), max_patches=2,random_state=0)
data = image.extract_patches_2d(one_image, (2,2))
print('data.shape1:',data.shape)

data = data.reshape(data.shape[0], -1)
print('data.shape2:',data.shape)
intercept = np.mean(data, axis=0)
data -= intercept
# patches = np.mean(patches, axis=1)
print('patches.shape:',data.shape)
print('patches:',data)
# print('patches:',patches[:, :, :, 0])

dico = MiniBatchDictionaryLearning(n_components=100, alpha=1, n_iter=500)
V = dico.fit(data).components_  #字典矩阵K*图片维度
print('V:',V.shape)
code = dico.transform(data)     #稀疏表示向量（K维）
print("code:",code.shape)
patches = np.dot(code, V)
print('code.shape：',patches)
patches += intercept
print('patches.shpae1:',patches.shape)
patches = patches.reshape(len(data), *(2,2))
print('patches.shpae2:',patches.shape)
reconstructed = reconstruct_from_patches_2d(patches,(4, 4))

print(reconstructed)

# np.testing.assert_array_equal(one_image, reconstructed)
