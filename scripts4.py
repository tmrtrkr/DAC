import pandas as pd

# CSV dosyasını oku
df = pd.read_csv('users_train.csv')

# 'mobile' kategorisindeki cihazların sayımını yap
mobile_df = df[df['device_category'] == 'mobile']
mobile_device_counts = mobile_df['device_model'].value_counts()

# 50'den az tekrar sayısına sahip cihaz modellerini filtrele
models_mobile_50_or_more = mobile_device_counts[mobile_device_counts >= 50].index

# 'mobile' kategorisindeki cihazlar arasında 50'den az tekrar sayısına sahip olanları çıkar
filtered_mobile_df = mobile_df[mobile_df['device_model'].isin(models_mobile_50_or_more)]

# 'tablet' kategorisindeki cihazların sayımını yap
tablet_df = df[df['device_category'] == 'tablet']
tablet_device_counts = tablet_df['device_model'].value_counts()

# 20'den az tekrar sayısına sahip cihaz modellerini filtrele
models_tablet_20_or_more = tablet_device_counts[tablet_device_counts >= 20].index

# 'tablet' kategorisindeki cihazlar arasında 20'den az tekrar sayısına sahip olanları çıkar
filtered_tablet_df = tablet_df[tablet_df['device_model'].isin(models_tablet_20_or_more)]

# Filtrelenmiş 'mobile' ve 'tablet' kategorilerindeki cihazları birleştir
filtered_df = pd.concat([filtered_mobile_df, filtered_tablet_df])

# Yeni CSV dosyasına kaydet
filtered_df.to_csv('filtered_devices.csv', index=False)

print("50'den az tekrar sayısına sahip 'mobile' kategorisindeki cihazlar ve 20'den az tekrar sayısına sahip 'tablet' kategorisindeki cihazlar çıkarıldı ve sonuçlar 'filtered_devices.csv' dosyasına kaydedildi.")
