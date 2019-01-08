import pandas as pd

data_train = pd.read_csv("../dataset/kaggle/tatanic/train.csv")

if __name__ == '__main__':
    data_train.info()