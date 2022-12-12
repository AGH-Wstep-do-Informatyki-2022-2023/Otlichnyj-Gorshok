import os


path = os.getcwd()

url='https://drive.google.com/file/d/1_o-URMUHlT8tSLRFRibTsDAwmDRdYLwU/view'
#print(url)
file_id=url.split('/')[-2]
#print(file_id)

dwn_url='https://drive.google.com/uc?id=' + file_id
#print(dwn_url)
df = pd.read_csv(dwn_url)


#dodawanie do zbioru
df['+'] = df['sepallength'] + 4

print(df.head())


#mnożenie zbioru
df['*'] = df['sepallength'] * 5

#print(df.head())


#odejmowanie pomiedzy wierszami
df['petallength'] = df['sepallength'] - df['sepalwidth']

#print(df.head())


#dzielenie pomiedzy wierszami
df['petalwidth'] = df['sepallength'] / df['sepalwidth']



#print(df.head())




if sys.platform.startswith("win32"):
    df.to_csv(f"{path}\\file.csv")

elif sys.platform.startswith("darwin"):
    df.to_csv(f"{path}/file.csv")



