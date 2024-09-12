#from tensorflow.python.client import device_lib
#print(device_lib.list_local_devices())


import pandas as pd

# İki CSV dosyasını yükle
df1 = pd.read_csv('test_sample.csv')
df2 = pd.read_csv('train_sample.csv')

# Sütun adlarını set olarak al
columns_df1 = set(df1.columns)
columns_df2 = set(df2.columns)

# df1'de olup df2'de olmayan sütunlar
missing_in_df2 = columns_df1 - columns_df2
print("df1'de olup df2'de olmayan sütunlar:", missing_in_df2)

# df2'de olup df1'de olmayan sütunlar
missing_in_df1 = columns_df2 - columns_df1
print("df2'de olup df1'de olmayan sütunlar:", missing_in_df1)
