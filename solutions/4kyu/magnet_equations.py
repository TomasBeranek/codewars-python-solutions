# Professor Chambouliard hast just discovered a new type of magnet material. He put
# particles of this material in a box made of small boxes arranged in K rows and N
# columns as a kind of 2D matrix K x N where K and N are postive integers. He thinks
# that his calculations show that the force exerted by the particle in the small
# box (k, n) is:
# v(k,n)=1k(n+1)2k \displaystyle v(k,n) = \dfrac{1}{k(n+1)^{2k}}v(k,n)=k(n+1)2k1​

# The total force exerted by the first row with k = 1 is:
# u(1,N)=∑n=1n=Nv(1,n)=11⋅22+11⋅32+⋯+11⋅(N+1)2 \displaystyle u(1, N) =
# \sum_{n=1}^{n=N}v(1, n) = \dfrac{1}{1 \cdot 2^2}+\dfrac{1}{1\cdot 3^2} + \dots + \frac{1}{1 \cdot (N+1)^2} u(1,N)=n=1∑n=N​v(1,n)=1⋅221​+1⋅321​+⋯+1⋅(N+1)21​

# We can go on with k = 2 and then k = 3 etc ... and consider:
# S(K,N)=∑k=1k=Ku(k,N)=∑k=1k=K(∑n=1n=Nv(k,n))→(double(maxk,maxn))\displaystyle S(K, N) =
# \sum_{k=1}^{k=K} u(k, N) = \sum_{k=1}^{k=K} \bigg(\sum_{n=1}^{n=N} v(k, n) \bigg) \to(double(max_k, max_n)) S(K,N)=k=1∑k=K​u(k,N)=k=1∑k=K​(n=1∑n=N​v(k,n))→(double(maxk​,maxn​))
# Task:

# To help Professor Chambouliard can we calculate the function doubles that will
# take as parameter maxk and maxn such that doubles(maxk, maxn) = S(maxk, maxn)?
# Experiences seems to show that this could be something around 0.7 when maxk and
# maxn are big enough.
# Examples:

# doubles(1, 3)  => 0.4236111111111111
# doubles(1, 10) => 0.5580321939764581
# doubles(10, 100) => 0.6832948559787737

# Notes:

#     In u(1, N) the dot is the multiplication operator.
#     Don't truncate or round: Have a look at the testing function in "Sample Tests".
#     link to symbol Sigma


import numpy as np


def doubles(maxk, maxn):
    N = np.arange(1, maxn+1, dtype=float)

    def u(k):
        return np.sum(1/k * (N+1)**(-2*k))

    return np.sum(u(k) for k in range(1, maxk+1))
