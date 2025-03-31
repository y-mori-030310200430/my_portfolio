from pretreatment import pretreatment
from predictive_model import predictive

# pretreatment変数
RelativeP = "" # 元ファイル
out_path = "" # 成形後outputファイル

# predictive変数
train_file = "" # pretreatment後outputファイル
test_file  = "" # test用path
test_t_path = "" # test用ファイルのpretreatment後outputファイル
test_p_path = "" # 結果用ファイルパス

# 実行
pretreatment(RelativeP, out_path)
predictive(train_file, test_file, test_t_path, test_p_path)