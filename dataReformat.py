import warnings

import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 10000)  # 最多显示数据的行数
warnings.filterwarnings("ignore")

path = r'C:\Users\Louie\PycharmProjects\Chevron-Datathon-Project'
df = pd.read_csv(path + '\%s.csv' % "added_testing_data", index_col=False)


df = df.pivot_table('Amount', ['StateCode', 'Year', 'State', 'CO2 Emissions (Mmt)',
                          'TotalNumberofInvestments', 'TotalAmountofAssistance'], 'MSN')
print(df.head())
df.to_csv(path+'\\added_testing_data2.csv', encoding='gbk')
exit()



rowNum = df.shape[0]
# print(df)
# exit()


states = set(df["StateCode"])
MSNs = set(df['MSN'])
test_set = set(df['CO2 Emissions (Mmt)'])
# print(len(states))
# print(len(test_set))
exit()


testMap = {}
test_col = "CO2 Emissions (Mmt)"

for i in range(rowNum):
    state = df['StateCode'].iloc[i]
    year = df['Year'].iloc[i]
    if (state, year) not in testMap.keys():
        testMap[(state, year)] = df.iloc[i][test_col]
    elif testMap[(state, year)] != df.iloc[i][test_col]:
        print(i)
        exit()
        
print(testMap)