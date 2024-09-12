import pandas as pd

# CSV dosyalarını yükle
df1 = pd.read_csv('targets_train.csv')  # ID ve TARGET içeren dosya
df2 = pd.read_csv('users_test.csv')  # Sadece ID içeren dosya

# 'ID' sütununa göre birleştirme (merge)
merged_df = pd.merge(df2, df1[['ID', 'TARGET']], on='ID', how='left')

# Sonucu kaydetmek istersen
merged_df.to_csv('merged_output.csv', index=False)

# Birleştirilen veriyi incelemek için
print(merged_df.head())
