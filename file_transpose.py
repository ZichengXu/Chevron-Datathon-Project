import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 10000)  # 最多显示数据的行数
# warnings.filterwarnings("ignore")


def file_transpose(path, file, cols):
    df = pd.read_excel(path + file, sheet_name=1)
    df = df.iloc[:, 0:7]
    df = df.transpose()
    # print(df)
    df.to_csv(path + "energyConsumption.csv", encoding='gbk')


path = r"C:\Users\Louie\PycharmProjects\Chevron-Datathon-Project\\"
file= r'use_tot_realgdp.xlsx'
cols = ['State', '2015', '2016', '2017', '2018', '2019', '2020']
# file_transpose(path, file, cols=cols)
states = ['New Mexico', 'Indiana', 'Missouri', 'Wyoming', 'Illinois', 'Oklahoma', 'Colorado', 'Michigan', 'Tennessee', 'Kansas', 'California', 'Montana', 'Kentucky', 'Pennsylvania', 'Louisiana', 'Alabama', 'Delaware', 'Texas', 'Arizona', 'North Dakota', 'Ohio', 'Maryland', 'Washington', 'Massachusetts', 'North Carolina', 'Florida', 'South Dakota', 'New Jersey', 'Oregon', 'Hawaii', 'Nebraska', 'Alaska', 'Utah', 'Virginia', 'New Hampshire', 'Wisconsin', 'Connecticut', 'Rhode Island', 'Arkansas', 'Georgia', 'Vermont', 'Idaho', 'West Virginia', 'Maine', 'Iowa', 'South Carolina', 'Minnesota', 'New York', 'Nevada', 'Mississippi']
statesABBr = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'US']
years = [2020]
# years = [2015, 2016, 2017, 2018, 2019]


def fill_data(baseFile, dataFile):
    baseDf = pd.read_csv(baseFile, encoding='utf-8', index_col=False)
    dataDf = pd.read_csv(dataFile, encoding='utf-8', index_col=False)
    # dataDf = pd.read_excel(dataFile)
    
    newColName = 'totalExpenditure'
    baseDf[newColName] = None
    
    # print(dataDf)
    #
    # exit()
    
    # baseDf.loc[(baseDf['State'] == 'Indiana') & (baseDf['Year'] == 2019), newColName] = 123
    # print(baseDf[(baseDf['State'] == 'Indiana')])
    for state in statesABBr:
        for year in years:
            # val = dataDf.loc[dataDf['State'] == year][state]._values[0]
            val = dataDf.loc[dataDf['State'] == state][str(year)]._values[0]
            
            # print(baseDf.loc[(baseDf['Year'] == year) & (baseDf['State'] == state)])
            baseDf.loc[(baseDf['StateCode'] == state) & (baseDf['Year'] == year), newColName] = val
            
    
    
    # baseDf = baseDf[['StateCode', 'Year', 'State', newColName]]
    baseDf.to_csv(path + "added_testing_data2.csv", encoding='gbk')
    
    
    
    print(baseDf)





fill_data(path + "added_testing_data2.csv", path + "Total Expenditures.csv")
