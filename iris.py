import pandas as pd
import numpy as np
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

knn = KNeighborsClassifier(n_neighbors=10)

knn.fit(X_train, y_train)

X_new = np.array([[7,2.1,6.9,0.3]])

prediction = knn.predict(X_new)

print("The name of the predicted target : {}".format(iris_dataset['target_names'][prediction]))

y_prediction = knn.predict(X_test)

for i in range(0, len(y_prediction)):
    y_pred = y_prediction[i]
    print("{} : {}".format(X_test[i], iris_dataset['target_names'][y_pred]))

print("accuracy_score : ",knn.score(X_test, y_test))

joblib.dump(knn, './knn_model.pkl')