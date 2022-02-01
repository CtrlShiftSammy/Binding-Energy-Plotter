from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import pandas
from scipy.stats import skew
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import math
import seaborn as sns

# Import DataSet
names = ['t1', 't2', 't3', 't4', 't5', 'experimentalBE', 'theoreticalBE']
dataSet = pandas.read_csv('data_cropped_with_formula.csv', names=names)

# Linear Regression
x = dataSet[['t1', 't2', 't3', 't4', 't5']]
y = dataSet.experimentalBE
z = dataSet.theoreticalBE

xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=1)

reg = LinearRegression().fit(xTrain, yTrain)
modPred = reg.predict(x)
print('R2(Model): ', r2_score(y,modPred)*100)
print('RMSE(Model): ', np.sqrt(mean_squared_error(y,modPred)))
print('RMSE(Theory): ', np.sqrt(mean_squared_error(y,z)))


# Graphing
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (16,9)

# Input vs Experiment Plot
# sns.pairplot(dataSet, x_vars=['a','z'], y_vars='experimentalBE', height=7, aspect=0.7);

plt.show()