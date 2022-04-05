# Import libraries:
# Model import Linear Regression
from sklearn.linear_model import LinearRegression
# Load the function that divides the file into training and test data
from sklearn.model_selection import train_test_split
# Import of the function responsible for calculating errors
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import csv

# Upload data:
df = pd.read_csv('cars.csv')
df.head()

# Y is the variable that will be tested and predicted
y = df.iloc[:, 0]
# X is the variable that contains the data that will be used for prediction
X = df.iloc[:, 1:]
# Division into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Model building
regressor = LinearRegression()
# Model training
regressor.fit(X_train, y_train)

# Prediction based on the model
y_pred = regressor.predict(X_test)

# Calculation of forecast accuracy measures:
# Average forecast's distance from the true value
print('MAE: ', mean_absolute_error(y_test, y_pred))


# New car prediction:
# Heading:
# cylinders, horsepower, weight, acceleration

while True:
    decision = input("Do you want to enter cars data? [Y/N]: ")
    if decision not in ["Y", "y", "yes"]:
        break
    try:
        cylinders = int(input("Enter the number of cylinders: "))
        horsepower = int(input("Enter the number of horsepower: "))
        weight = int(input("Enter the weight of the car:  "))
        acceleration = float(input("Enter the acceleration, e.g. 7.8: "))

        Xnew = [[cylinders, horsepower, weight, acceleration]]

        # Make a prediction
        ynew = regressor.predict(Xnew)
        # Show the inputs and predicted outputs
        y = round(ynew[0], 1)
        print("X=%s, Predicted=%s" % (Xnew[0], y))
        print("The estimated fuel consumption for this car is", y, "l/100km")

        add_decision = input("Do you want to add the results to the database? [Y/N]: ")
        if add_decision not in ["Y", "y", "yes"]:
            break
        try:
            Xnew[0].insert(0,y)
            with open(r'cars.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(Xnew[0])
        except:
            print("The entry could not be added to the database ")
    except:
        print("You only need to enter numeric values ")
        print("Incorrect result ")
input()
