import pandas as pd

def check_duplicate_ids(file):
    # CSV dosyasını okuyun
    df = pd.read_csv(file)

    # `ID` sütununu sayısal veri tipine dönüştürün
    df['ID'] = df['ID'].astype(int)

    # Yinelenen ID'leri kontrol edin
    duplicate_counts = df['ID'].value_counts()
    
    # Birden fazla kez tekrar eden ID'leri filtreleyin
    duplicates = duplicate_counts[duplicate_counts > 1]

    # Toplam yinelenen ID sayısını ve her birinin kaç kez tekrarlandığını bastırın
    print("Toplam yinelenen ID sayısı: {}".format(len(duplicates)))
    print("\nYinelenen ID'ler ve tekrar sayıları:")
    print(duplicates)

# Kullanım
check_duplicate_ids('users_train.csv')
