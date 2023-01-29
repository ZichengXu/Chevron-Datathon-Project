import warnings

import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 10000)  # 最多显示数据的行数
warnings.filterwarnings("ignore")

path = r'C:\Users\Louie\PycharmProjects\Chevron-Datathon-Project'
df = pd.read_csv(path + '\%s.csv' % "ProcessedInvestment_Data_Train", index_col=False)
print(df.shape)
df = df[df['Year'] == 2019]

print(df.shape)
df.to_csv(path+'\%test19.csv', encoding='gbk')
