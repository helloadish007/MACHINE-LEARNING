from sklearn import datasets
import pandas as pd
diabetes = datasets.load_diabetes()
df = pd.DataFrame(diabetes.data)
df['target'] = diabetes.target

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(x, y)

feat_labels=diabetes.feature_names

imp_features=[]
for feature in zip(feat_labels, model.feature_importances_):
    imp_features.append(feature)
for i in range(0,3):
    print(imp_features[i])
