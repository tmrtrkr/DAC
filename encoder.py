import pandas as pd

csv1 = 'users_train.csv'
csv2 = 'users_test.csv'

def convert_device_category(filepath, output_filepath):
    """
    'device_category' sütunundaki 'mobil' değerlerini 0 ve 'tablet' değerlerini 1 ile değiştirir.
    Sonuçları output_filepath ile belirtilen dosyaya kaydeder.

    :param filepath: Girdi CSV dosyasının yolu
    :param output_filepath: Sonuçların kaydedileceği CSV dosyasının yolu
    """
    # CSV dosyasını yükleyin
    df = pd.read_csv(filepath)
    
    # 'device_category' sütununu dönüştürün
    df['device_category'] = df['device_category'].map({'mobile': 0, 'tablet': 1})

    # Sonuçları kontrol edin
    print(df.head())

    # Yeni CSV dosyası oluşturun
    df.to_csv(output_filepath, index=False)


def convert_platform(filepath, output_filepath):
    """
    'platform' sütunundaki 'android' değerlerini 0 ve 'ios' değerlerini 1 ile değiştirir.
    Sonuçları output_filepath ile belirtilen dosyaya kaydeder.

    :param filepath: Girdi CSV dosyasının yolu
    :param output_filepath: Sonuçların kaydedileceği CSV dosyasının yolu
    """
    # CSV dosyasını yükleyin
    df = pd.read_csv(filepath)
    
    # 'platform' sütununu dönüştürün
    df['platform'] = df['platform'].map({'android': 0, 'ios': 1})

    # Sonuçları kontrol edin
    print(df.head())

    # Yeni CSV dosyası oluşturun
    df.to_csv(output_filepath, index=False)


def one_hot_encode_device_brand(filepath, output_filepath):
    """
    'device_brand' sütununu one-hot encoding işlemi uygular.
    Sonuçları output_filepath ile belirtilen dosyaya kaydeder.

    :param filepath: Girdi CSV dosyasının yolu
    :param output_filepath: Sonuçların kaydedileceği CSV dosyasının yolu
    """
    # CSV dosyasını yükleyin
    df = pd.read_csv(filepath)
    
    # 'device_brand' sütununu one-hot encoding yapın
    df_encoded = pd.get_dummies(df, columns=['device_brand'])

    # Sonuçları kontrol edin
    print(df_encoded.head())

    # Yeni CSV dosyası oluşturun
    df_encoded.to_csv(output_filepath, index=False)



def one_hot_encode_ad_network(filepath, output_filepath):
    """
    'ad_network' sütununu one-hot encoding işlemi uygular.
    Sonuçları output_filepath ile belirtilen dosyaya kaydeder.

    :param filepath: Girdi CSV dosyasının yolu
    :param output_filepath: Sonuçların kaydedileceği CSV dosyasının yolu
    """
    # CSV dosyasını yükleyin
    df = pd.read_csv(filepath)
    
    # 'ad_network' sütununu one-hot encoding yapın
    df_encoded = pd.get_dummies(df, columns=['ad_network'])

    # Sonuçları kontrol edin
    print(df_encoded.head())

    # Yeni CSV dosyası oluşturun
    df_encoded.to_csv(output_filepath, index=False)


def merge_and_save(users_train_path, processed_data_path, output_path):
    # Veriyi oku
    df_users_train = pd.read_csv(users_train_path)
    df_processed_data = pd.read_csv(processed_data_path)
    
    # Birleştir
    df_merged = df_users_train.merge(df_processed_data, on='ID', how='left')
    
    # Sonuçları CSV dosyasına kaydet
    df_merged.to_csv(output_path, index=False)
    print(f"Updated data saved to {output_path}")


# Fonksiyonu çağırın
convert_platform(csv1, csv1)
convert_platform(csv2, csv2)

# Fonksiyonu çağırın
convert_device_category(csv1, csv1)
convert_device_category(csv2, csv2)

one_hot_encode_device_brand(csv1, csv1)
one_hot_encode_device_brand(csv2, csv2)

one_hot_encode_ad_network(csv1, csv1)
one_hot_encode_ad_network(csv2, csv2)

merge_and_save(csv1, 'processed_data_train.csv', csv1)
merge_and_save(csv2, 'processed_data_test.csv', csv2)