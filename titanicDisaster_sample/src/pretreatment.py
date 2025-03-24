import pandas as pd

def pretreatment(RelativeP, out_path):
  # inputファイル読み込み
  train_data = pd.read_csv(RelativeP)

  # 不要列の削除
  del train_data["Name"]
  del train_data["Cabin"]
  del train_data["Embarked"]
  del train_data["Ticket"]
  del train_data["Fare"]

  # Ageの調整
  train_data.dropna(subset=["Age"], axis=0, inplace=True)
  train_data["Age"] = train_data["Age"].round()

  # Sexのカテゴリカル変数化
  train_data = pd.get_dummies(train_data, dtype=int)
  del train_data["Sex_male"]

  # 前処理の情報を出力
  train_data.to_csv(out_path, index=False)

pretreatment("titanicDisaster_sample/input/train.csv", "titanicDisaster_sample/output/pretreatment.csv")