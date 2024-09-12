import pandas as pd

def group_device_models_by_brand(input_path, output_path):
    # Veri setini okuma
    df = pd.read_csv(input_path)

    # Cihaz modellerini markalarına göre gruplama
    grouped_df = df[['device_brand', 'device_model']].drop_duplicates().sort_values(by=['device_brand', 'device_model'])

    # Excel dosyasına kaydetme
    grouped_df.to_excel(output_path, index=False)
    
    # Toplam benzersiz device modeli sayısını hesaplama
    total_models = grouped_df['device_model'].nunique()
    
    # Sonucu konsola bastırma
    print(f"Toplam benzersiz cihaz modeli sayısı: {total_models}")

    print(f"Cihaz modelleri markaya göre gruplandı ve '{output_path}' dosyasına kaydedildi.")

# Kullanım örneği
group_device_models_by_brand('users_train.csv', 'grouped_device_models.xlsx')
