import pandas as pd

def merge_targets_to_final(train_file, targets_file, output_file):
    """
    targets_file dosyasındaki 'TARGET' bilgilerini,
    train_file dosyasındaki 'ID' bilgisine göre ekler ve
    güncellenmiş veri setini output_file olarak kaydeder.

    Parameters:
    train_file (str): Eğitim veri seti dosyası (CSV).
    targets_file (str): Hedef veri seti dosyası (CSV).
    output_file (str): Güncellenmiş veri setini kaydedecek dosya adı.
    """
    # CSV dosyalarını okuyun
    targets_df = pd.read_csv(targets_file)
    final_train_df = pd.read_csv(train_file)

    # `ID` sütununa göre birleştirin
    merged_df = final_train_df.merge(targets_df[['ID', 'TARGET']], on='ID', how='left')

    # Sonuçları yeni bir CSV dosyasına yazın
    merged_df.to_csv(output_file, index=False)

    print(f"Birleştirme işlemi tamamlandı ve '{output_file}' dosyasına kaydedildi.")

# Kullanım
merge_targets_to_final('users_train.csv', 'targets_train.csv', 'users_train.csv')
