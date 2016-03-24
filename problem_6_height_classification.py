"""Classify height class - Orenj assignment."""
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier


# Load data
data = pd.read_csv('./orenj_data.csv')

# Convert Gender to number. 'F' = 0, 'M' = 1
# Gender does not play a big role in helping classifying for this task
data['Gender'] = data.Gender.map({'F': 0, 'M': 1})
data['Gender'] = data['Gender'].astype(int)

# Drop 'Name' column
data = data.drop('Name', axis=1)

# Prepare train and rest data for RandomForest
train_data = data.values
test_data = np.array([1., 1.95])
test_data = test_data.reshape(1, -1)

# Training
forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(train_data[:, :2], train_data[:, 2])

# Predict
output = forest.predict(test_data)

print "Test data: {'Name': 'Obama', 'Gender': 'M', 'Height': 1.95}"
print "Class: ", output[0]
