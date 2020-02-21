# https://codeforces.com/gym/102517/problem/C
import math


def manhattan_dist(a, b):
    return sum([abs(a[i] - b[i]) for i in range(len(a))])


def euclidean_dist(a, b):
    return sum([(a[i] - b[i]) * (a[i] - b[i]) for i in range(len(a))]) ** 0.5


def chebyshev_dist(a, b):
    return max([abs(a[i] - b[i]) for i in range(len(a))])


def uniform_kernel(d):
    return 1


def triangular_kernel(d):
    return 1 - d


def epanechnikov_kernel(d):
    return 1 - d * d


def quartic_kernel(d):
    return (1 - d * d) * (1 - d * d)


def triweight_kernel(d):
    return (1 - d * d) ** 3


def tricube_kernel(d):
    return (1 - d ** 3) ** 3


def gaussian_kernel(d):
    return math.e ** (-d * d / 2)


def cosine_kernel(d):
    return math.cos(math.pi * d / 2)


def logistic_kernel(d):
    return 1 / (math.e ** d + 2 + math.e ** -d)


def sigmoid_kernel(d):
    return 1 / (math.pi * (math.e ** d + math.e ** -d))


n, m = [int(i) for i in input().split()]
x, y = [], []
for i in range(n):
    x.append([int(i) for i in input().split()])
    y.append(x[i].pop())

object_x = [int(i) for i in input().split()]
dist_type, kernel_type, wind_type, window = input(), input(), input(), int(input())
dist, kernel = globals()[dist_type + '_dist'], globals()[kernel_type + '_kernel']
obj_dists = list(map(dist, x, [object_x for i in range(n)]))
if wind_type == 'fixed':
    h = window
else:
    # k = window + 1
    # min_dists = sorted(obj_dists[:k], reverse=True)
    # for i in obj_dists[k:]:
    #     for j in range(k):
    #         if i < min_dists[j]:
    #             if j > 0:
    #                 min_dists[j - 1] = min_dists[j]
    #             min_dists[j] = i
    #         else:
    #             break
    # h = min_dists[0]

    h = sorted(obj_dists)[window]
    h = max(obj_dists) if h == 0 else h

res = sum_w = 0
for i, obj_dist in enumerate(obj_dists):
    w = kernel(obj_dist / h) if obj_dist < h or kernel_type in ('gaussian', 'logistic', 'sigmoid') else 1 \
        if h == obj_dist == 0 else 0
    sum_w += w
    res += w * y[i]
res = res / sum_w if sum_w != 0 else sum(y) / len(y)
print(res)
