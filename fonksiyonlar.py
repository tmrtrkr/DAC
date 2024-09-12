import pandas as pd

def kategori_sayisi_ve_yazdir(csv_dosyasi, sutun_adi):

# Fonksiyonu kullanma örneği:
#csv_dosyasi = 'users_train.csv'  # CSV dosya yolu
#sutun_adi = 'device_model'  # Filtrelemek istediğin sütun adı

#kategori_sayisi_ve_yazdir(csv_dosyasi, sutun_adi)



    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)

    # Her kategoriyi bir kez al, sayısal olanları ve NaN değerleri stringe çevir
    kategoriler = df[sutun_adi].dropna().astype(str).unique()

    # Kategorileri alfabetik sıraya koy
    kategoriler = sorted(kategoriler)

    # Kategorileri alfabetik sırada yazdır
    for kategori in kategoriler:
        print(kategori)

    # Toplam kategori sayısını yazdır
    print(f"Toplam kategori sayısı: {len(kategoriler)}")


def kategori_sayisi_ve_farki_bul(csv_dosya1, csv_dosya2, sutun_adi):

#kategori_sayisi_ve_farki_bul('users_train.csv', 'users_test.csv', 'country')

    # İlk CSV dosyasını oku
    df1 = pd.read_csv(csv_dosya1)

    # İkinci CSV dosyasını oku
    df2 = pd.read_csv(csv_dosya2)

    # NaN değerlerini kaldır ve kategorileri string olarak al
    kategoriler1 = df1[sutun_adi].dropna().astype(str).unique()
    kategoriler2 = df2[sutun_adi].dropna().astype(str).unique()

    # Her iki dosyadaki kategori sayısını yazdır
    print(f"Birinci dosyadaki toplam kategori sayısı: {len(kategoriler1)}")
    print(f"İkinci dosyadaki toplam kategori sayısı: {len(kategoriler2)}")

    # Birinci dosyada olup ikinci dosyada olmayan kategoriler
    fark_kategoriler1 = set(kategoriler1) - set(kategoriler2)

    # İkinci dosyada olup birinci dosyada olmayan kategoriler
    fark_kategoriler2 = set(kategoriler2) - set(kategoriler1)

    # Farkları yazdır
    print(f"\nBirinci dosyada olup ikinci dosyada olmayan kategori sayısı: {len(fark_kategoriler1)}")
    if fark_kategoriler1:
        print("Birinci dosyada olup ikinci dosyada olmayan kategoriler:")
        for kategori in sorted(fark_kategoriler1):
            print(kategori)
    else:
        print("Birinci dosyadaki tüm kategoriler ikinci dosyada da mevcut.")

    print(f"\nİkinci dosyada olup birinci dosyada olmayan kategori sayısı: {len(fark_kategoriler2)}")
    if fark_kategoriler2:
        print("İkinci dosyada olup birinci dosyada olmayan kategoriler:")
        for kategori in sorted(fark_kategoriler2):
            print(kategori)
    else:
        print("İkinci dosyadaki tüm kategoriler birinci dosyada da mevcut.")


def satir_sil_ve_kaydet(csv_dosyasi, sutun_adi, silinecek_kategoriler):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)

    # Silinecek kategorileri içermeyen satırları filtrele
    df_filtered = df[~df[sutun_adi].isin(silinecek_kategoriler)]

    # Filtrelenmiş veriyi aynı dosya adıyla kaydet (orijinal dosyanın üzerine yazılır)
    df_filtered.to_csv(csv_dosyasi, index=False)

    print(f"- TRAIN-TEST ARASI EKSIK DEGERLER {sutun_adi} {csv_dosyasi} dosyasından silinen kategoriler: {silinecek_kategoriler}")



def kategori_farklarini_dondur(csv_dosya1, csv_dosya2, sutun_adi):
    # İlk CSV dosyasını oku
    df1 = pd.read_csv(csv_dosya1)

    # İkinci CSV dosyasını oku
    df2 = pd.read_csv(csv_dosya2)

    # NaN değerlerini kaldır ve kategorileri string olarak al
    kategoriler1 = df1[sutun_adi].dropna().astype(str).unique()
    kategoriler2 = df2[sutun_adi].dropna().astype(str).unique()

    # Birinci dosyada olup ikinci dosyada olmayan kategoriler
    fark_kategoriler1 = sorted(set(kategoriler1) - set(kategoriler2))

    # İkinci dosyada olup birinci dosyada olmayan kategoriler
    fark_kategoriler2 = sorted(set(kategoriler2) - set(kategoriler1))

    # İki farklı liste return ediliyor
    return fark_kategoriler1, fark_kategoriler2

def null_degerleri_sil_ve_overwrite(csv_dosyasi, sutun_adi):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # 'sutun_adi' sütununda NaN (null) olmayan satırları filtrele
    df_filtered = df[df[sutun_adi].notna()]
    
    # Filtrelenmiş veriyi aynı dosyaya kaydet (overwrite)
    df_filtered.to_csv(csv_dosyasi, index=False)
    
    print(f"- NULL CLEANING '{sutun_adi}' sütunundaki null değerler silindi ve dosya '{csv_dosyasi}' güncellendi.")

def replace_nulls(csv_dosyasi, column_name, replacement_value):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # Belirtilen sütundaki NaN (NULL) değerlerini verilen kelime ile değiştir
    df[column_name] = df[column_name].fillna(replacement_value)
    
    # Güncellenmiş DataFrame'i döndür
    df.to_csv(csv_dosyasi, index=False)


def yuvarla_ve_kaydet(csv_dosyasi, sutun_adi):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # Belirtilen sütundaki değerleri 2 ondalık basamağa yuvarla
    df[sutun_adi] = df[sutun_adi].round(2)
    
    # Dosyayı overwrite ederek kaydet
    df.to_csv(csv_dosyasi, index=False)
    
    print(f"{sutun_adi} sütunundaki değerler 2 ondalık basamağa yuvarlandı ve dosya '{csv_dosyasi}' güncellendi.")



def missing_degerleri_sifirla(csv_dosyasi):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # 'Level_x_Duration' ile başlayan tüm sütunları bul
    level_columns = [col for col in df.columns if col.startswith('Level_') and col.endswith('_Duration')]
    
    # Bu sütunlardaki NaN (missing) değerleri 0 ile değiştir
    df[level_columns] = df[level_columns].fillna(0)
    
    # Güncellenmiş veriyi aynı dosyaya kaydet
    df.to_csv(csv_dosyasi, index=False)
    
    print(f"'FILL NULL WITH 0 Level_x_Duration' sütunlarındaki missing (NaN) değerler 0 ile değiştirildi ve '{csv_dosyasi}' dosyasına kaydedildi.")


def revenue_sutunlarini_yuvarla_ve_kaydet(csv_dosyasi):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # 'AdRevenue' ve 'IAPRevenue' ile başlayan tüm sütunları bul
    revenue_columns = [col for col in df.columns if col.startswith('AdRevenue') or col.startswith('IAPRevenue')]
    
    # Bu sütunlardaki tüm değerleri 2 ondalık basamağa yuvarla
    df[revenue_columns] = df[revenue_columns].round(2)
    
    # Dosyayı güncellenmiş haliyle kaydet
    df.to_csv(csv_dosyasi, index=False, float_format="%.2f")
    
    print(f"- ROUND AND FORMAT'{csv_dosyasi}' dosyasındaki tüm AdRevenue ve IAPRevenue sütunlarındaki değerler 2 ondalık basamağa yuvarlandı ve kaydedildi.")


def retention_sutunlarini_cevir_ve_kaydet(csv_dosyasi):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # 'RetentionD' ile başlayan tüm sütunları bul
    retention_columns = [col for col in df.columns if col.startswith('RetentionD')]
    
    # Bu sütunlardaki boolean değerleri integer (1 ve 0) ile değiştir
    df[retention_columns] = df[retention_columns].astype(int)
    
    # Dosyayı güncellenmiş haliyle kaydet
    df.to_csv(csv_dosyasi, index=False)
    
    print(f"- BOOLEAN TO INT'{csv_dosyasi}' dosyasındaki RetentionD0'dan RetentionD15'e kadar olan boolean değerler integer (1 ve 0) olarak değiştirildi ve kaydedildi.")



def satir_ve_sutun_sayisini_bul(csv_dosyasi):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # Satır ve sütun sayısını bul
    satir_sayisi = df.shape[0]
    
    print(f"{csv_dosyasi} Satır sayısı: {satir_sayisi}")



def device_brandlari_sil_ve_kaydet(csv_dosyasi, sutun_adi, silinecek_brandlar, yeni_dosya_adi):
    # CSV dosyasını oku
    df = pd.read_csv(csv_dosyasi)
    
    # Silinecek markaları içermeyen satırları filtrele
    df_filtered = df[~df[sutun_adi].isin(silinecek_brandlar)]
    
    # Filtrelenmiş veriyi yeni bir CSV dosyasına kaydet
    df_filtered.to_csv(yeni_dosya_adi, index=False)
    
    print(f"{len(silinecek_brandlar)} model silindi ve güncellenmiş veri '{yeni_dosya_adi}' dosyasına kaydedildi.")



# Fonksiyonu kullanma örneği:
#device_brandlari_sil_ve_kaydet('users_test.csv', 'device_brand', silinecek_brandlar, 'users_test.csv')

csv_dosyasi1 = 'users_train.csv'
csv_dosyasi2 = 'users_test.csv'


#null_degerleri_sil_ve_overwrite(csv_dosyasi1, 'country')
#null_degerleri_sil_ve_overwrite(csv_dosyasi2, 'country')


#replace_nulls(csv_dosyasi1, 'ad_network', 'organic')
replace_nulls(csv_dosyasi2, 'ad_network', 'organic')

#null_degerleri_sil_ve_overwrite(csv_dosyasi1, 'device_brand')
#null_degerleri_sil_ve_overwrite(csv_dosyasi2, 'device_brand')


#null_degerleri_sil_ve_overwrite(csv_dosyasi1, 'device_model')
#null_degerleri_sil_ve_overwrite(csv_dosyasi2, 'device_model')


#bir, iki = kategori_farklarini_dondur(csv_dosyasi1, csv_dosyasi2, 'device_model')

#device_brandlari_sil_ve_kaydet(csv_dosyasi1, 'device_model', bir, csv_dosyasi1)
#device_brandlari_sil_ve_kaydet(csv_dosyasi2, 'device_model', iki, csv_dosyasi2)


#kategori_sayisi_ve_farki_bul(csv_dosyasi1, csv_dosyasi2, 'device_model')






