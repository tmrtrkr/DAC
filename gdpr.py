import pandas as pd



def add_gdpr_column(users_train_path, gdpr_path, output_path):
    # Veri setlerini okuma
    users_train = pd.read_csv(users_train_path)
    gdpr = pd.read_csv(gdpr_path)

    # GDPR sütununu eklemek için GDPR.csv'deki '2024' sütununu 'GDPR' olarak yeniden adlandırma
    gdpr.rename(columns={'2024': 'gdp'}, inplace=True)

    # 'country' sütununa göre birleştirme yapma (left join)
    users_train = users_train.merge(gdpr[['country', 'gdp']], on='country', how='left')

    # Güncellenmiş veri setini kaydetme
    users_train.to_csv(output_path, index=False)
    print(f"Yeni dosya '{output_path}' olarak kaydedildi.")


def remove_null_gdpr(dataset_path, output_path):
    # Veri setini okuma
    df = pd.read_csv(dataset_path)

    # GDPR sütununda null olanları filtreleme
    filtered_df = df.dropna(subset=['gdp'])

    # Sonuç veri setini kaydetme
    filtered_df.to_csv(output_path, index=False)
    print(f"gdp'ı null olan veriler çıkarıldı ve filtrelenmiş veri seti '{output_path}' olarak kaydedildi.")

# Kullanmak için örnek
#remove_null_gdpr('updated_users_train.csv', 'updated_users_train.csv')

def remove_backslash_in_gdpr(dataset_path, output_path):
    # Veri setini okuma
    df = pd.read_csv(dataset_path)

    # GDPR sütununda '\' içeren satırları filtreleme
    filtered_df = df[~df['GDPR'].str.contains(r'\\', na=False)]

    # Sonuç veri setini kaydetme
    filtered_df.to_csv(output_path, index=False)
    print(f"GDPR sütununda 't' karakteri içeren veriler çıkarıldı ve filtrelenmiş veri seti '{output_path}' olarak kaydedildi.")

# Kullanmak için örnek
#remove_backslash_in_gdpr('updated_users_train.csv', 'updated_users_train.csv')
#remove_null_gdpr('users_test.csv', 'users_test.csv')
csv1 = 'users_train.csv'
csv2 = 'users_test.csv'

#add_gdpr_column(csv1, 'GDP.csv', csv1)
#add_gdpr_column(csv2, 'GDP.csv', csv2)

remove_null_gdpr(csv1, csv1)
remove_null_gdpr(csv2, csv2)