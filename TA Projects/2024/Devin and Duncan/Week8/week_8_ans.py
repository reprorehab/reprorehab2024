import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


# Data for plots
normal_data = np.random.normal(loc=50, scale=5, size=(1000,))
uniform_data = np.random.uniform(low=0, high=100, size=(1000,))

## Basic Plotting ###
# Visualize normal_data using a histogram. Experiment with different numbers of bins (e.g., 10, 20, 50)
# Add a grid to the plot and adjust its style, such as using dashed lines.

n_bins_ranges = [10, 20, 50]
for n_bins in n_bins_ranges:
    plt.hist(normal_data, bins = n_bins)
    plt.title("Number of bins: " + str(n_bins))
    plt.grid(linestyle = "--")
    plt.show()

# Create a histogram of uniform_data in a separate figure. Add a title and label the x-axis and y-axis
# Customize the font size and color of the title and axis labels.

plt.hist(uniform_data)
plt.title("Simulated Uniform Data - Histrogram")
plt.xlabel("Simulated Data")
plt.ylabel("Frequency")
plt.show()

## Subplots and Multi-Panel Figures ###
# Visualize normal_data and uniform_data using two subplots within the same figure.
# Place one histogram above the other in a stacked layout.
# Add a shared x-axis label and y-axis label for the whole figure.

fig_1, (axs_normal, axs_uniform) = plt.subplots(nrows= 2,ncols= 1, sharex=True, sharey=True)
axs_normal.hist(normal_data)
axs_uniform.hist(uniform_data)
fig_1.supxlabel("Data")
fig_1.supylabel("Frequency")
plt.show()

# Visualize normal_data and uniform_data using two subplots arranged side by side.
# Ensure each subplot has a different style for its grid, such as adjusting transparency or line style.

fig_2, (axs_normal, axs_uniform) = plt.subplots(nrows= 2,ncols= 1, sharex=True, sharey=True)
axs_normal.hist(normal_data)
axs_normal.grid(alpha = .25, linestyle = '--', color = 'red')
axs_uniform.hist(uniform_data)
axs_uniform.grid(alpha = .95, linestyle = ":", color = 'blue')
plt.show()

## Create a single figure with four subplots arranged in 2 rows and 2 columns. ##
# Assign one of the following visualizations to each subplot.
# 1. Histogram of normal_data (top left)
# 2. Histogram of uniform_data (top right)
# 3. Boxplot of the first 100 samples of normal_data (bottom left)
# 4. Boxplot of the first 100 samples of uniform_data (bottom right)

# Adjust the sizing between each plot to avoid overlap.
# For all boxplots, update the tick labels on the x axis with "Normal Data" and "Uniform Data".
# Add a shared y axis for the boxplots, and then for the histograms.
# Add a shared x axis only for the histograms
# Set the color of normal data in histogram and boxplot. Do the same with uniform data
# Add a single y label for the histograms
# Add a single y label for the boxplots

# Choose colors
data_colors = ["blue", "green"]
# set up figure and sub plots
fig_3, ((axs_normal_hist, axs_uniform_hist), (axs_normal_box, axs_uniform_box)) = (
    plt.subplots(nrows=2, ncols=2, sharey="row")
)
# plot histograms
axs_normal_hist.hist(normal_data, color=data_colors[0])
axs_uniform_hist.hist(uniform_data, color=data_colors[1])
# spruce up histograms
axs_normal_hist.sharex(axs_uniform_hist)
axs_normal_hist.set_ylabel("Frequency")
# plot boxplots
normal_boxplot = axs_normal_box.boxplot(normal_data, patch_artist=True)
uniform_boxplot = axs_uniform_box.boxplot(uniform_data, patch_artist=True)
# spruce up boxplots
for boxplot, color in zip([normal_boxplot, uniform_boxplot], data_colors):
    boxplot['boxes'][0].set_facecolor(color)
axs_normal_box.set_xticklabels(["Normal Data"])
axs_uniform_box.set_xticklabels(["Uniform Data"])
axs_normal_box.set_ylabel("Data Range")
# adjust spacing between all subplots
plt.tight_layout()
plt.show()

## Customization and Advanced Axes Manipulation
# Visualize the first 100 samples of normal_data and uniform_data using boxplots on the same axes.
# Add individual data points on top of the boxplots.
# Use different marker shapes for normal_data and uniform_data and adjust their transparency for better visibility.
# Explore jittering the data points in the previous boxplots to better separate overlapping points.
# Add horizontal and vertical lines at specific locations on the boxplot:
# Add a horizontal line at the median of the x-data for each box plot
# Add a vertical line at the median of the y-data for each boxplot
n_samples = 100
all_data = [normal_data[:n_samples], uniform_data[:n_samples]]
noise_level = .075
data_markers = ['o', 'd']
all_colors = ['purple', 'black']
# matplotlib example
fig_4, ax = plt.subplots()
ax.boxplot(all_data)

x_data_values = np.ones((2, n_samples)) * [[1],[2]] + np.random.normal(loc=0, scale = noise_level, size = (n_samples,))
for x_values, y_values, markers, scatter_color in zip(x_data_values, all_data, data_markers, all_colors):
    ax.scatter(x = x_values, y=y_values, marker=markers, alpha=.5, c= scatter_color)
    ax.axhline(np.median(y_values), color = scatter_color)
    ax.axvline(np.median(x_values), color = scatter_color)
    
ax.set_xticklabels(["Normal Data", "Uniform Data"])
plt.show()

# Scatter Plots and Lines
# Using a scatter plot, visualize linear data (e.g., generate x as an array from 0 to 99, Create y as a linear function of x with added noise.).
# Add a line of best fit to the scatter plot.
# Customize the scatter plot by changing the marker size, marker color, and layering order of the points and lines. Add a legend to differentiate the data and the line.

x = np.arange(0, 99)
noise_level = 5
intercept_true, slope_true = 0, 1
noise = np.random.normal(loc=0, scale = noise_level, size = (len(x),))
y = intercept_true + slope_true * x + noise
slope_est, _, _, _, _ = stats.linregress(x, y)
plt.scatter(x,y, facecolor= 'blue', edgecolors='black', label = 'Scattered data', marker='s',s = 100, zorder = -1)
plt.axline(xy1=[0,0], slope=slope_est, color = 'red', label = 'Line of best fit', zorder = 1, linewidth = 5, alpha = .5)
plt.legend()
plt.show()