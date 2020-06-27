from sklearn import datasets
import numpy as np
import pandas
import scipy.stats
    
# load the iris dataset split by feature and named
def get_data_split_panda():
    iris = datasets.load_iris()
    iris_data = pandas.DataFrame(iris.data)
    iris_data["Species"] = pandas.Categorical.from_codes(iris.target, iris.target_names)
    iris_data["SpeciesId"] = iris.target
    iris_data.columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", 'Species', 'Speciesd']
    return iris_data

# just load and return unlabeled dataset
def get_data():
    return datasets.load_iris()

# assuming a normally distributed 1-D array, remove outliers by 3-sigma method and return new mean
def trimmed_mean(arr):
    cutoff = np.std(arr)*3
    filter = abs(arr - np.mean(arr)) < cutoff
    return np.mean(arr[filter])

# make numbers suitable for printing
def sanitize(matrix, skip_first=True):
    num = 1 if skip_first else 0
    for i in range(len(matrix)):
        for j in range(num,len(matrix[i])):
            matrix[i][j] = str(round(matrix[i][j], 3))

# given a data frame, compute the summary statistics and return in an array
def get_statistics(frame, name):
    headers = [name, "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    matrix = [["Minimum"], ["Maximum"], ["Mean"], ["Trimmed Mean"], ["Standard Deviation"], ["Skewness"], ["Kurtosis"]]
    matrix[0] = matrix[0] + [np.amin(frame.loc[:, headers[i]]) for i in range(1,5)]
    matrix[1] = matrix[1] + [np.amax(frame.loc[:, headers[i]]) for i in range(1,5)]
    matrix[2] = matrix[2] + [np.mean(frame.loc[:, headers[i]]) for i in range(1,5)]
    matrix[3] = matrix[3] + [trimmed_mean(frame.loc[:, headers[i]]) for i in range(1,5)]
    matrix[4] = matrix[4] + [np.std(frame.loc[:, headers[i]]) for i in range(1,5)]
    matrix[5] = matrix[5] + [scipy.stats.skew(frame.loc[:, headers[i]]) for i in range(1,5)]
    matrix[6] = matrix[6] + [scipy.stats.kurtosis(frame.loc[:, headers[i]]) for i in range(1,5)]
    return (matrix, headers)

# given a data frame, compute covariance matrix
def get_covar_mat(frame):
    # print(frame.cov().values.tolist())
    return pandas.DataFrame.cov(frame).values.tolist()







