import pandas as pd

def update_device_category(file_path, output_path, device_models_to_update):
    # CSV dosyasını oku
    df = pd.read_csv(file_path)

    # 'device_category' 'mobile', 'device_model' belirtilen cihaz modelleri olan ve 'platform' 'iOS' olan satırları filtrele
    mask = (df['device_category'] == 'mobile') & \
           (df['device_model'].isin(device_models_to_update)) & \
           (df['platform'] == 'iOS')

    # Bu satırların 'device_category' değerini 'tablet' olarak güncelle
    df.loc[mask, 'device_category'] = 'tablet'

    # Güncellenmiş DataFrame'i kaydet
    df.to_csv(output_path, index=False)

    # Güncellenmiş DataFrame'i döndür
    return df

# TRAIN
device_models_to_update1 = [
    'iPod touch (7th generation)',
    'iPad (9th gen)',
    'iPad Air (4th gen)',
    'iPad Air (5th gen)',
    'iPad Pro (11-inch) (4th generation)',
    'iPad Pro (12.9-inch) (6th generation)',
    'iPad mini (5th generation)',
    'iPod touch 6th gen',
    'iPad (7th gen)',
    'iPad Pro (11-inch) (2nd generation)',
    'iPad mini (6th generation)',
    'iPad (8th gen)',
    'iPad Pro (12.9-inch) (3rd generation)',
    'iPad Air (3rd gen)'
]


device_models_to_update2 = [
    'iPad Air (4th gen)',
    'iPod touch (7th generation)',
    'iPhone 6 Plus',
    'iPhone 5s',
    'iPad (9th gen)',
    'iPad Pro (11-inch) (4th generation)',
    'iPhone 15',
    'iPad Pro (12.9-inch) (6th generation)',
    'iPod touch 6th gen',
    'iPad Air (5th gen)',
    'iPhone 15 Pro Max',
    'iPad mini (6th generation)',
    'iPad',
    'iPad Pro (11-inch) (3rd generation)',
    'iPad (7th gen)'
]

# Fonksiyonu çağırarak güncellemeleri yap



csv1 = 'users_train.csv'
csv2 = 'users_test.csv'


update_device_category(csv1, csv1, device_models_to_update1)
update_device_category(csv2, csv2, device_models_to_update2)

