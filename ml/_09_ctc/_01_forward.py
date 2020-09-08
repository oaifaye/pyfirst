import numpy as np
#https://blog.csdn.net/JackyTintin/article/details/79425866
# np.random.seed(1111)

T, V = 12, 5
m, n = 6, V

x = np.random.random([T, m])  # T x m
w = np.random.random([m, n])  # weights, m x n

def softmax(logits):
    max_value = np.max(logits, axis=1, keepdims=True)
    exp = np.exp(logits - max_value)
    exp_sum = np.sum(exp, axis=1, keepdims=True)
    dist = exp / exp_sum
    return dist

def toy_nw(x):
    y = np.matmul(x, w)  # T x n
    y = softmax(y)
    return y

y = toy_nw(x)
print(y)
print(y.sum(1, keepdims=True))

def forward(y, labels):
    T, V = y.shape
    L = len(labels)
    alpha = np.zeros([T, L])

    # init
    alpha[0, 0] = y[0, labels[0]]
    alpha[0, 1] = y[0, labels[1]]

    for t in range(1, T):
        for i in range(L):
            s = labels[i]

            a = alpha[t - 1, i]
            if i - 1 >= 0:
                a += alpha[t - 1, i - 1]
            if i - 2 >= 0 and s != 0 and s != labels[i - 2]:
                a += alpha[t - 1, i - 2]

            alpha[t, i] = a * y[t, s]

    return alpha

labels = [0, 3, 0, 3, 0, 4, 0]  # 0 for blank
# alpha = forward(y, labels)
# print('alpha:',alpha)
# print('alpha[-1, labels[-1]]:',alpha[-1, labels[-1]])
# print('alpha[-1, labels[-2]]:',alpha[-1, labels[-2]])
# print('alpha[-1, -1]:',alpha[-1, -1])
# print('alpha[-1, -2]:',alpha[-1, -2])
# print('alpha[-1, -1] + alpha[-1, -2]:',alpha[-1, -1] + alpha[-1, -2])
# p = alpha[-1, labels[-1]] + alpha[-1, labels[-2]]
# print('p:',p)
# print('np.sum(alpha[-1]):',np.sum(alpha[-1]))
# print(np.asarray(labels)[np.argmax(alpha,axis=1)])

def backward(y, labels):
    T, V = y.shape
    L = len(labels)
    beta = np.zeros([T, L])

    # init
    beta[-1, -1] = y[-1, labels[-1]]
    beta[-1, -2] = y[-1, labels[-2]]

    for t in range(T - 2, -1, -1):
        for i in range(L):
            s = labels[i]

            a = beta[t + 1, i]
            if i + 1 < L:
                a += beta[t + 1, i + 1]
            if i + 2 < L and s != 0 and s != labels[i + 2]:
                a += beta[t + 1, i + 2]

            beta[t, i] = a * y[t, s]

    return beta

# beta = backward(y, labels)
# print(beta)

def gradient(y, labels):
    T, V = y.shape
    L = len(labels)

    alpha = forward(y, labels)
    beta = backward(y, labels)
    p = alpha[-1, -1] + alpha[-1, -2]

    grad = np.zeros([T, V])
    for t in range(T):
        for s in range(V):
            lab = [i for i, c in enumerate(labels) if c == s]
            for i in lab:
                grad[t, s] += alpha[t, i] * beta[t, i]
            grad[t, s] /= y[t, s] ** 2

    grad /= p
    return grad

grad = gradient(y, labels)
print('grad:',grad)

def check_grad(y, labels, w=-1, v=-1, toleration=1e-3):
    grad_1 = gradient(y, labels)[w, v]

    delta = 1e-10
    original = y[w, v]

    y[w, v] = original + delta
    alpha = forward(y, labels)
    log_p1 = np.log(alpha[-1, -1] + alpha[-1, -2])

    y[w, v] = original - delta
    alpha = forward(y, labels)
    log_p2 = np.log(alpha[-1, -1] + alpha[-1, -2])

    y[w, v] = original
    grad_2 = (log_p1 - log_p2) / (2 * delta)
    if np.abs(grad_1 - grad_2) > toleration:
        print('[%d, %d]：%.2e' % (w, v, np.abs(grad_1 - grad_2)))

for toleration in [1e-5, 1e-6]:
    print('%.e' % toleration)
    for w in range(y.shape[0]):
        for v in range(y.shape[1]):
            check_grad(y, labels, w, v, toleration)