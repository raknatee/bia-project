import numpy as np
from sklearn.linear_model import LinearRegression
from typing import List

dataset:List[int] = []

with open('./data.csv','r') as f:
    header = f.readline()
    while line := f.readline():

        strings = line.split(',')
        data = [float(strings[0]),float(strings[1])]
        dataset.append(data)

dataset = np.array(dataset)
X = dataset[:,0].reshape(-1,1)
y = dataset[:,1].reshape(-1,1)
print(dataset.shape)

linear = LinearRegression().fit(X,y)
print("score",linear.score(X,y))
print("coef",linear.coef_)
print("intercept",linear.intercept_)

