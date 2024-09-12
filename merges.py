import pandas as pd

import pandas as pd

def add_release_dates(train_csv, grouped_csv, output_csv):
    """
    `train_csv` dosyasına `grouped_csv` dosyasındaki `release_date` bilgisini ekler ve sonucu `output_csv` dosyasına kaydeder.

    :param train_csv: trainOrigin copy.csv dosyasının yolu
    :param grouped_csv: grouped_device_models.csv dosyasının yolu
    :param output_csv: Sonuçların kaydedileceği CSV dosyasının yolu
    """
    # CSV dosyalarını yükleyin
    train_df = pd.read_csv(train_csv)
    grouped_df = pd.read_csv(grouped_csv)

    # Boşlukları temizle (eğer varsa)
    train_df.columns = train_df.columns.str.strip()
    grouped_df.columns = grouped_df.columns.str.strip()

    # grouped_device_models'de device_model başına tek bir release_date olduğundan emin olun
    # İlk release_date'i seçin (varsa birden fazla varsa)
    model_release_dates = grouped_df.groupby('device_model', as_index=False).agg({'release_date': 'first'})

    # train_df ile model_release_dates veri çerçevelerini birleştirin
    merged_df = pd.merge(train_df, model_release_dates, on='device_model', how='left')

    # Sonuçları kontrol edin
    print(merged_df.head())

    # Yeni CSV dosyası oluşturun
    merged_df.to_csv(output_csv, index=False)




def convert_column_to_lowercase(csv_path, column_name):
    """
    Belirtilen sütundaki tüm değerleri küçük harfe çevirir ve sonucu bir CSV dosyasına kaydeder.

    Args:
        csv_path (str): Üzerinde işlem yapılacak CSV dosyasının yolu.
        column_name (str): Küçük harfe çevrilecek sütunun adı.
        output_path (str): Güncellenmiş CSV dosyasının kaydedileceği yol.
    """
    # CSV dosyasını oku
    df = pd.read_csv(csv_path)

    # Belirtilen sütundaki tüm değerleri küçük harfe çevir
    if column_name in df.columns:
        df[column_name] = df[column_name].astype(str).str.lower()
    else:
        print(f"Uyarı: '{column_name}' adlı sütun veri setinde bulunamadı.")

    # Sonuçları yeni bir CSV dosyasına kaydet
    df.to_csv(csv_path, index=False)
    print(f"Sütundaki tüm değerler küçük harfe çevrildi ve dosya '{csv_path}' olarak kaydedildi.")


# Fonksiyon kullanım örneği
#csv_path = 'users_test.csv'


def merge_and_save(users_train_path, processed_data_path, output_path):
    # Veriyi oku
    df_users_train = pd.read_csv(users_train_path)
    df_processed_data = pd.read_csv(processed_data_path)
    
    # Birleştir
    df_merged = df_users_train.merge(df_processed_data, on='ID', how='left')
    
    # Sonuçları CSV dosyasına kaydet
    df_merged.to_csv(output_path, index=False)
    print(f"Updated data saved to {output_path}")

# Dosya yollarını belirtin
#users_train_path = 'users_train.csv'
#processed_data_path = 'processed_data_train.csv'
#output_path = 'final_train.csv'
#merge_and_save(users_train_path, processed_data_path, output_path)

# Dosya yollarını belirtin
#users_train_path = 'users_test.csv'
#processed_data_path = 'processed_data_test.csv'
#output_path = 'final_test.csv'
#merge_and_save(users_train_path, processed_data_path, output_path)


#merge_device_models_to_users(csv_path, 'grouped_device_models.csv', csv_path)

#convert_column_to_lowercase('trainOrigin.csv', 'country')
#merge_device_models_to_users('trainOrigin copy 2.csv', 'grouped_device_models.csv', 'trainOrigin copy 2.csv')
 
csv1 = 'users_train.csv'
csv2 = 'users_test.csv'

#convert_column_to_lowercase(csv1, 'country')
#convert_column_to_lowercase(csv1, 'platform')
#convert_column_to_lowercase(csv1, 'device_brand')
#convert_column_to_lowercase(csv1, 'device_model')

#convert_column_to_lowercase(csv2, 'country')
#convert_column_to_lowercase(csv2, 'platform')
#convert_column_to_lowercase(csv2, 'device_brand')
#convert_column_to_lowercase(csv2, 'device_model')
#add_release_dates(csv1, 'grouped_device_models.csv', csv1)
add_release_dates(csv2, 'grouped_device_models.csv', csv2)