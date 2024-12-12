import pandas
import numpy 

# 1. Loading data 
# a - load iris dataset 
data = pandas.read_csv('./iris/iris.data', header=None)
# b - display first 5 rows of df 
N_ROWS = 5
print(data.head(N_ROWS))
# c - fix column headers
HEADERS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
rename_dict = {0: HEADERS[0], 1: HEADERS[1], 2: HEADERS[2], 3: HEADERS[3], 4: HEADERS[4]}
data.rename(columns=rename_dict, inplace=True)
print(data.head(N_ROWS))
# d - index first 10 rows 
print(data.iloc[0:10, :])

# 2. Data Extraction 
# a - extract sepal length
sepal_length = data['sepal_length']
# b - retrieve rows 5 to 15 of dataset 
print(data.iloc[5:16, :])
# c - rows 5 to 9, with all column (:) of df 
# d - first two columns and all rows 
print(data.iloc[:, 0:2])

# 3. Indexing data 
# a - logically index all Iris-setosa rows 
print(data.loc[data['class'] == 'Iris-setosa', :])
# b - find and print all rows with petal length larger than 4 
PETAL_LENGTH_LIMIT = 4.0
print(data.loc[data['petal_length'] > PETAL_LENGTH_LIMIT, :])
# c - new df only with sepal length larger than 3.5
SEPAL_WIDTH_LIMIT = 3.5    
small_sepal_widths = data.loc[data['sepal_width'] < SEPAL_WIDTH_LIMIT, :]
print(small_sepal_widths.head(5))

# 4. Incorporating NumPy
# a - sepal length to numpy array and calculate mean 
sepal_length = numpy.array(data['sepal_length'])
avg_sepal_length = sepal_length.mean()
print(f'Average sepal length = {avg_sepal_length: .2f}')

# b - median petal length 
med_petal_length = data['petal_length'].median()
print(f'Median petal length = {med_petal_length: .2f}')

# c - sepal width standard deviation 
sepal_width = numpy.array(data['sepal_width'])
std_sepal_width = sepal_width.std()
print(f'Standard deviation of sepal width = {std_sepal_width: .2f}')

# d - calculate mean and std of each numeric column in data set
numeric_data = data.iloc[:, 0:4]
avgs = numeric_data.mean()
print('Averages:')
print(avgs)
stds = numeric_data.std()
print('Standard deviations: ')
print(stds)

# 5. More Numpy!!!!
# a = convert dataframe to numpy array and verify shape 
data_np = data.to_numpy()
print('New shape = ')
print(data_np.shape)

# b - numpy array with only sepal length and width and print shape
sepal_info = data.iloc[:, 0:2].to_numpy()
print(sepal_info[145:150, :])
print('Sepal info shape = ')
print(sepal_info.shape)

# c - calculate mean of each sepal info column
SEPAL_INFO_DIM = 1 
avg_sepal_info = sepal_info.mean(axis=SEPAL_INFO_DIM)
print(f'Average speal length = {avg_sepal_info[0]: .2f}')
print(f'Average speal width = {avg_sepal_info[1]: .2f}')

# d - 3d array [instance x sepal/petal length/width x class]
iris_types = data['class'].unique()
setosa = data.loc[data['class'] == iris_types[0], :].to_numpy()
versicolour = data.loc[data['class'] == iris_types[1], :].to_numpy()
virginica = data.loc[data['class'] == iris_types[2], :].to_numpy()

new_data = numpy.empty((50, 4, 3))
new_data[:, :, 0] = setosa[:, 0:-1]
new_data[:, :, 1] = versicolour[:, 0:-1]
new_data[:, :, 2] = virginica[:, 0:-1]
print(new_data.shape)

# e - calculate mean and std of petal length for each species 
PETAL_LENGTH_IDX = 2
petal_length_avgs = new_data[:, PETAL_LENGTH_IDX, :].mean(axis=0)
print(f'Avarege petal lengths = {petal_length_avgs}')
petal_length_stds = new_data[:, PETAL_LENGTH_IDX, :].mean(axis=0)
print(f'Standard deviation of petal lengths = {petal_length_stds}')

# f - function to calculate average sepal length for a given species
def average_sepal_length(df: pandas.DataFrame, species: str) -> float:
    species_df = df.loc[df['class'] == 'Iris-' + species, :]
    return species_df['sepal_length'].mean()

print(f'setosa average sepal length = {average_sepal_length(data, "setosa"): .2f}')
print(f'versicolour average sepal length = {average_sepal_length(data, "versicolor"): .2f}')
print(f'virginica average sepal length = {average_sepal_length(data, "virginica"): .2f}')
