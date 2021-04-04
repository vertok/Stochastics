# Alexey Obukhov s77673
import math
import statistics
import numpy as np

mouse = [20.7, 32.8, 27.1, 27.4, 23.5, 25.9]
bear = [285600.0, 272100.0, 249800.0, 250000.0, 293900.0, 266600.0]

#define function to calculate cv
cv = lambda x: np.std(x, ddof=1) / np.mean(x) * 100 

# mouse
mean_mouse = sum(mouse) / 6
print("mean mouse: ", mean_mouse)

# bear
mean_bear = sum(bear) / 6
print("mean bear: ", mean_bear)

# variance
sample_mouse = statistics.variance(mouse)
print("variance mouse: ", sample_mouse)
sample_bear = statistics.variance(bear)
print("variance bear: ", sample_bear)

# variance coeficient
print("coefficient variance (cv) for mouse: ", cv(mouse))
print("coefficient variance (cv) for bear: ", cv(bear))