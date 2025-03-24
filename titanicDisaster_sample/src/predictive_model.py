from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection
import pandas as pd
from pretreatment import pretreatment

def predictive(train_file, test_file, test_t_path, test_p_path):
  train_data = pd.read_csv(train_file)

  survived = train_data.loc[train_data["Survived"]==1]
  not_survived = train_data.loc[train_data["Survived"]==0].sample(len(survived), random_state=0)

  X = pd.concat([survived, not_survived], ignore_index=True)
  y = X["Survived"]
  del X["Survived"]
  X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=0)

  model = DecisionTreeClassifier(random_state=0, max_depth=5)
  model.fit(X_train, y_train)
  # print(model.score(X_test, y_test))
  # print(model.score(X_train, y_train))

  importance = pd.DataFrame({"feature_names": X.columns, "coefficient": model.feature_importances_})
  # print(importance)

  pretreatment(test_file, test_t_path)

  test_data = pd.read_csv(test_t_path)

  # print(model.predict(test_data))
  # print(model.predict_proba(test_data))

  test_data["Survived"] = model.predict(test_data)

  del test_data["Pclass"]
  del test_data["Age"]
  del test_data["SibSp"]
  del test_data["Parch"]
  del test_data["Sex_female"]

  test_data.to_csv(test_p_path, index=False)

predictive("titanicDisaster_sample/output/pretreatment.csv", "titanicDisaster_sample/input/test.csv", "titanicDisaster_sample/output/pretreatment_test.csv", "titanicDisaster_sample/output/prediction_test.csv")