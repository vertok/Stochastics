import math
import statistics
import numpy as np

#define function to calculate cv
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100 

# a
vector_x = [2, -3, 5, 7, 8, 6, 5, 6, 9, 12]
vector_y = [4, 7, 6, 9, 14, 17, 23, 20, 17, 30]
# b
mean_x = sum(vector_x) / 10
mean_y = sum(vector_y) / 10
print("mean: ", mean_x)
sample_x = statistics.variance(vector_x)
print("variance: ", sample_x)
# c
print("covariance Sxy: ", np.cov(vector_x, vector_y)[0][1])
# d
print("CV:",cv(vector_x))
