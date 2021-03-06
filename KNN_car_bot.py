# # = comment

# Here we import our plugins
import sklearn
from sklearn import preprocessing
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# here we enter data
data = pd.read_csv("cardata.csv")
print(data.head())

# from here create labels
le = preprocessing.LabelEncoder()
# start listing labels
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

# create variables
x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

# start writing variable testing code
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

#model
model = KNeighborsClassifier(n_neighbors=9)
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)

print(acc)

# predictions
predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]
for x in range(len(predicted)):
    print("predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    n = model.kneighbors([x_test[x]], 9, True)
    print("N: ", n)
