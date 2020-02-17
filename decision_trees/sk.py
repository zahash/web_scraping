from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from dfcleaner import cleaner
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
df = cleaner.sanitize_column_names(df)

conversion_dict = cleaner.suggest_convertion_dict(df)

df = cleaner.change_dtypes(df, conversion_dict)

feat = df.drop(columns="result")
label = df["result"]

feat = pd.get_dummies(feat, drop_first=True)
# print(feat.info())


X_train, X_test, y_train, y_test = train_test_split(feat, label, test_size=0.3)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# tree.plot_tree(clf) 
# plt.show()

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)