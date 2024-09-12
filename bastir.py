import pandas as pd



def print_device_brands_info(dataset_path):
    # Veri setini okuma
    df = pd.read_csv(dataset_path)

    # Device brand'e göre benzersiz marka ve model sayısı ile her bir markanın kaç kere geçtiğini bulma
    device_info = df.groupby('device_brand').agg(
        unique_models=('device_model', 'nunique'),  # Benzersiz model sayısı
        brand_count=('device_brand', 'count')       # Her bir brand kaç kere geçti
    ).reset_index()

    # Sonuçları bastırma
    for index, row in device_info.iterrows():
        print(f"Device Brand: {row['device_brand']}, Unique Models: {row['unique_models']}, Occurrences: {row['brand_count']}")

# Fonksiyonu kullanma örneği


def filter_device_brands(dataset_path, output_path):
    # Veri setini okuma
    df = pd.read_csv(dataset_path)

    # Device brand'e göre her bir markanın kaç kere geçtiğini bulma
    brand_counts = df['device_brand'].value_counts()

    # 100'den fazla geçen markaları seçme
    valid_brands = brand_counts[brand_counts >= 550].index

    # 100'den az geçenleri filtreleme
    filtered_df = df[df['device_brand'].isin(valid_brands)]

    # Sonuç veri setini kaydetme
    filtered_df.to_csv(output_path, index=False)
    print(f"Filtrelenmiş veri seti '{output_path}' olarak kaydedildi.")

# Fonksiyonu kullanma örneği

#print_device_brands_info('filtered_dataset.csv')



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

#add_gdpr_column('users_train.csv', 'GDP.csv', 'updated_users_train.csv')


def optimize_device_brands():
    # Verilen device brand bilgilerini veri çerçevesine ekleme
    data = {
        'Device Brand': ['Apple', 'Google', 'Honor', 'Huawei', 'Infinix', 'LG', 'Lenovo', 'Motorola', 'Nokia', 'OPPO', 'OnePlus', 'POCO', 
                         'Realme', 'Samsung', 'T-Mobile', 'TCL', 'Tecno', 'Vivo', 'Xiaomi', 'ZTE'],
        'Unique Models': [63, 28, 49, 110, 80, 68, 55, 160, 66, 149, 52, 5, 115, 288, 13, 73, 69, 188, 242, 85],
        'Occurrences': [363353, 3209, 12587, 13043, 7457, 3195, 3583, 76003, 1282, 22900, 5774, 941, 12155, 225742, 704, 2920, 8635, 14386, 82115, 4006]
    }
    
    df = pd.DataFrame(data)
    
    # Occurrence başına düşen model sayısını hesaplama
    df['Occ_per_Model'] = df['Occurrences'] / df['Unique Models']
    
    # Metrik değeri küçükten büyüğe doğru sıralama
    df_sorted = df.sort_values(by='Occ_per_Model', ascending=False)
    
    # En optimize edilebilecek markaları gösterme
    print(df_sorted[['Device Brand', 'Unique Models', 'Occurrences', 'Occ_per_Model']])

# Fonksiyonu çalıştırma
#optimize_device_brands()

def remove_brands(dataset_path, output_path, brands_to_remove):
    # Veri setini okuma
    df = pd.read_csv(dataset_path)

    # Belirtilen markaları çıkartma
    filtered_df = df[~df['device_brand'].isin(brands_to_remove)]

    # Sonuç veri setini kaydetme
    filtered_df.to_csv(output_path, index=False)
    print(f"Filtrelenmiş veri seti '{output_path}' olarak kaydedildi.")



def remove_nulls_from_column(csv_path, column_name, output_path):
    """
    Belirtilen sütundaki null değerleri içeren satırları siler ve sonucu bir CSV dosyasına kaydeder.

    Args:
        csv_path (str): Üzerinde işlem yapılacak CSV dosyasının yolu.
        column_name (str): Null değerlerin kontrol edileceği sütunun adı.
        output_path (str): Güncellenmiş CSV dosyasının kaydedileceği yol.
    """
    # CSV dosyasını oku
    df = pd.read_csv(csv_path)

    # Belirtilen sütundaki null değerleri içeren satırları sil
    if column_name in df.columns:
        df_cleaned = df.dropna(subset=[column_name])
    else:
        print(f"Uyarı: '{column_name}' adlı sütun veri setinde bulunamadı.")
        return

    # Sonuçları yeni bir CSV dosyasına kaydet
    df_cleaned.to_csv(output_path, index=False)
    print(f"Null değerler içeren satırlar silindi ve dosya '{output_path}' olarak kaydedildi.")

# Kullanmak için örnek:




def convert_permission_column(file_path, column_name='has_ios_att_permission'):
    """
    Converts True values to 1 and False values to 0 in the specified column of the CSV file.
    
    Parameters:
    file_path (str): The path to the CSV file.
    column_name (str): The name of the column to convert (default is 'has_ios_att_permission').
    
    Returns:
    None: The function saves the updated DataFrame to the same CSV file.
    """
    # Veriyi oku
    df = pd.read_csv(file_path)
    
    if column_name in df.columns:
        df[column_name] = df[column_name].astype(int)  # Converts True to 1 and False to 0
        # Güncellenmiş veriyi kaydet
        df.to_csv(file_path, index=False)
        print(f"Column '{column_name}' successfully converted and saved.")
    else:
        print(f"Column '{column_name}' does not exist in the DataFrame.")

# Fonksiyonu çağır
#file_path = 'final_train.csv'
#convert_permission_column(file_path)


#file_path = 'final_test.csv'
#convert_permission_column(file_path)

 #rint_device_brands_info('users_train_filtered_dataset.csv')
#filter_device_brands('users_train.csv', 'users_train.csv')
#remove_brands('users_train.csv', 'users_train_filtered_dataset_OPPO.csv', brands_to_remove)
#print_device_brands_info('users_train_filtered_dataset.csv')
#remove_nulls_from_column('user_features_test.csv', 'first_prediction', 'user_features_test.csv')
#remove_nulls_from_column('final_train.csv', 'total_retention', 'final_train.csv')

csv1 = 'users_train.csv'
csv2 = 'users_test.csv'

remove_nulls_from_column(csv1, 'total_ad_revenue', csv1)
remove_nulls_from_column(csv2, 'total_ad_revenue', csv2)

#convert_permission_column(csv1, column_name='has_ios_att_permission')
#convert_permission_column(csv2, column_name='has_ios_att_permission')