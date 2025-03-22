import pandas as pd

train_data = pd.read_csv("titanicDisaster_sample/input/train.csv")
# print(train_data.head())
# print(train_data.columns)
print(train_data.isna().sum())
print(len(train_data))