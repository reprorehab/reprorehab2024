import numpy 
import scipy.stats as stats
# Data Generation 
# a 
normal_data = numpy.random.normal(loc=50, scale=5, size=(1000,))
# b 
uniform_data = numpy.random.uniform(low=10, high=20, size=(1000,))

# Conducting Statistical Tests
# a 
t_stat, p_value = stats.ttest_ind(normal_data, uniform_data)
print(f'Results: t = {t_stat: .2f}, p = {p_value: .4f}')

# b
N_SAMPLES, MEAN, SD = 100, 10, 2
sample1 = numpy.random.normal(MEAN, SD, N_SAMPLES)
sample2 = numpy.random.normal(MEAN, SD, N_SAMPLES)
t_stat, p_value = stats.ttest_rel(sample1, sample2)
print(f'Results: t = {t_stat: .2f}, p = {p_value: .4f}')

# Linear Regression and Correlation
# a 
x = numpy.arange(0, 100)
intercept_true, slope_true = 0, 1
noise = numpy.random.standard_normal(len(x))
y = intercept_true + slope_true * x + noise
slope_est, intercept_est, _, p_value, _ = stats.linregress(x, y)
print('Results | True | Estimated')
print(f' Intercept | {intercept_true: .2f} | {intercept_est: .2f}')
print(f' Slope | {slope_true: .2f} | {slope_est: .2f}')

# b 
stat, p_value = stats.pearsonr(x, y)
print(f'Results: r = {stat: .2f}, p = {p_value:.4f}')

# Applying Statistical Tests in a Loop
# a 
N_SAMPLES, MEAN, SD, N_DATASETS = 1000, 50, 5, 5
datasets = numpy.random.normal(MEAN, SD, (N_SAMPLES, N_DATASETS))
t_stat, p_value = stats.ttest_ind(datasets, numpy.column_stack((uniform_data, uniform_data, uniform_data, uniform_data, uniform_data)))
for idx, i_t_stat, i_p_value in zip(range(len(t_stat)), t_stat, p_value):
    print(f'Results from {idx+1} comparison: t = {i_t_stat: .2f}, p = {i_p_value: .4f}')