import pandas as pd
import numpy as np

# CSV dosyasını okuma
df = pd.read_csv('users_test.csv')

# iPhone model dağılımı
iphone_model_distribution = {
    'iPhone 11': 52448,
    'iPhone 13': 31742,
    'iPhone 12': 21075,
    'iPhone 14 Pro Max': 19121,
    'iPhone 14': 17677,
    'iPhone 13 Pro Max': 16293,
    'iPhone XR': 13769,
    'iPhone 14 Pro': 9218,
    'iPhone 8 Plus': 8150,
    'iPhone 13 Pro': 7986,
    'iPhone 14 Plus': 7364,
    'iPhone 11 Pro Max': 6674,
    'iPhone 12 Pro': 6402,
    'iPhone 8': 5377,
    'iPhone SE (2nd generation)': 5274,
    'iPhone X': 4761,
    'iPhone 11 Pro': 4689,
    'iPhone 7 Plus': 4535,
    'iPhone 7': 4288,
    'iPhone XS Max': 3372,
    'iPhone XS': 3154,
    'iPhone 12 mini': 3043,
    'iPhone 13 mini': 2098,
    'iPhone 6s': 1905,
    'iPhone SE (3rd generation)': 1650,
    'iPhone 6s Plus': 976,
    'iPhone SE': 257,
    'iPhone 6': 148,
    'iPhone 6 Plus': 36,
    'iPhone 5s': 25
}

# Toplam iPhone cihaz sayısını buluyoruz (iPhone hariç)
total_ios_devices = sum(iphone_model_distribution.values())

# Her bir modelin yüzdesini hesaplıyoruz
iphone_model_percentages = {model: count / total_ios_devices for model, count in iphone_model_distribution.items()}

# "iPhone" olarak belirtilen 39,210 kaydı bu yüzdelere göre orantılı olarak dağıtacağız
iphone_to_distribute = 39210

# iPhone modellerine göre rastgele dağılım yapıyoruz
models = list(iphone_model_percentages.keys())
probabilities = list(iphone_model_percentages.values())

# "iPhone" yazan satırları buluyoruz
iphone_indices = df[df['device_model'] == 'iPhone'].index

# Tahmini modelleri orantılı olarak dağıtıyoruz
predicted_models = np.random.choice(models, size=len(iphone_indices), p=probabilities)

# Yeni sütunu oluşturup tahmin edilen modelleri atıyoruz
df.loc[iphone_indices, 'predicted_device_model'] = predicted_models

# Diğer satırların (iPhone olmayanlar) model bilgilerini olduğu gibi yeni sütuna kopyalıyoruz
df.loc[df['device_model'] != 'iPhone', 'predicted_device_model'] = df['device_model']

# Veriyi mevcut CSV dosyasının üzerine kaydetme
df.to_csv('users_test.csv', index=False)

print("Tahmini modeller ve mevcut modeller sütun olarak eklendi ve dosya kaydedildi.")
