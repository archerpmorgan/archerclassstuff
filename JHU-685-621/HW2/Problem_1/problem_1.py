import markdown_table
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import common

def main():

    data = common.get_data_split_panda()
    features = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

    print("# Statstics Tables\n")
    print("## By Class\n")
    print("### Setosa\n")
    matrix, headers = common.get_statistics(data.loc[data['Species'] == 'setosa'].drop(columns=['Species', 'Speciesd']), "Setosa")
    common.sanitize(matrix)
    print(markdown_table.render(headers, matrix)+ "\n")

    matrix = common.get_covar_mat(data.loc[data['Species'] == 'setosa'].drop(columns=['Species', 'Speciesd']))
    common.sanitize(matrix, skip_first=False)
    for i in range(4):
        matrix[i] = [features[i]] + matrix[i] 
    print(markdown_table.render(["Covariance"] + features, matrix) + "\n")

    print("### Versicolor\n")
    matrix, headers = common.get_statistics(data.loc[data['Species'] == 'versicolor'].drop(columns=['Species', 'Speciesd']), "Versicolor")
    common.sanitize(matrix)
    print(markdown_table.render(headers, matrix)+ "\n")

    matrix = common.get_covar_mat(data.loc[data['Species'] == 'versicolor'].drop(columns=['Species', 'Speciesd']))
    common.sanitize(matrix, skip_first=False)
    for i in range(4):
        matrix[i] = [features[i]] + matrix[i] 
    print(markdown_table.render(["Covariance"] + features, matrix) + "\n")

    print("### Virginica\n")
    matrix, headers = common.get_statistics(data.loc[data['Species'] == 'virginica'].drop(columns=['Species', 'Speciesd']), "Virginica")
    common.sanitize(matrix)
    print(markdown_table.render(headers, matrix)+ "\n")

    matrix = common.get_covar_mat(data.loc[data['Species'] == 'virginica'].drop(columns=['Species', 'Speciesd']))
    common.sanitize(matrix, skip_first=False)
    for i in range(4):
        matrix[i] = [features[i]] + matrix[i] 
    print(markdown_table.render(["Covariance"] + features, matrix) + "\n")

if __name__ == "__main__":
    main()






