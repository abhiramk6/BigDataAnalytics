from scipy.stats import ttest_1samp
import numpy as np

ages = [32, 34, 29, 29, 22, 39, 38, 37, 38, 36, 30, 26, 22, 22]
print(ages)
ages_mean = np.mean(ages)
print(ages_mean)
tset, pval = ttest_1samp(ages, 30)
print("p-values", pval)
if pval < 0.05:  # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")
