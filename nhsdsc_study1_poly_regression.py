import pandas
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# dtst_dir = "datasets/diabetes_012_health_indicators_BRFSS2015.csv"
dtst_dir = "datasets/diabetes_012_test_1.csv"

dtst = pandas.read_csv(dtst_dir).dropna()

# Function that takes in a pandas dataframe and outputs a new dataframe with n rows. These rows are selected randomly from the original dataset.
# IMPORTANT: Function is incomplete. If someone could finish it, that would be much appreciated!
def createRandomSmallDataset(dtst, n):

    newDataframe = pandas.DataFrame(columns=list(dtst.columns.values))

    for i in range(0, n):
        row = dtst.iloc[[random.randint(0, len(dtst))]]
        newDataframe.loc[i] = row

    return newDataframe

x = dtst[["Diabetes_012", "HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke", "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education", "Income"]].values
y = dtst["MentHlth"].values

'''
plt.plot(dtst["GenHlth"], dtst["MentHlth"])
plt.show()
'''

polyModel = PolynomialFeatures(degree = 4, include_bias=False) # Changing degree into 1 results in linear regression model.
polyX = polyModel.fit_transform(x)

# Split the dataset into to train/test sections.

xTrain, xValidation, yTrain, yValidation = train_test_split(polyX, y, test_size=0.3, random_state=42)

polyModel.fit(xTrain, yTrain)

linearModel = LinearRegression()
linearModel.fit(xTrain, yTrain)

predictions = linearModel.predict(xValidation)

print(predictions)
print(mean_squared_error(yValidation, predictions, squared=False))

degrees = [1, 2, 3, 4, 5, 6, 7]
mean_squared_error_list = [6.658825469443437, 6.553170836282355, 6.5089789129822035]

'''
degrees = [1, 2, 3, 4, 5, 6, 7]
averageSquaredError = []

for degree in degrees:

    polyModel = PolynomialFeatures(degree=degree)
    polyX = polyModel.fit_transform(x)
    polyModel.fit(polyX, y)

    linearModel = LinearRegression()
    linearModel.fit(polyX, y)
    predictions = linearModel.predict(polyX)

    averageSquaredError.append(mean_squared_error(y, predictions, squared=False))

plt.scatter(degrees, averageSquaredError, color="green")
plt.plot(degrees, averageSquaredError, color="red")
'''


# https://stackoverflow.com/questions/57507832/unable-to-allocate-array-with-shape-and-data-type
# https://enjoymachinelearning.com/blog/multivariate-polynomial-regression-python/
