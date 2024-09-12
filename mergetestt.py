import pandas as pd

# CSV dosyalarını yükleyin
train_df = pd.read_csv('trainOrigin copy.csv')
grouped_df = pd.read_csv('grouped_device_models.csv')

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
merged_df.to_csv('trainOrigin_with_release_dates.csv', index=False)
