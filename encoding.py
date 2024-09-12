import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def preprocess_and_save(file_path):
    # Veriyi oku
    df = pd.read_csv(file_path)
    
    # One-hot encoding için fonksiyon
    def preprocess_ad_network_one_hot(df, column_name='platform'):
        encoder = OneHotEncoder(sparse_output=False, drop='first')  # sparse yerine sparse_output kullanıyoruz
        encoded_columns = encoder.fit_transform(df[[column_name]])
        
        # Yeni sütun adlarını oluştur
        column_names = encoder.get_feature_names_out([column_name])
        
        # DataFrame'ye ekleyin
        encoded_df = pd.DataFrame(encoded_columns, columns=column_names)
        df = pd.concat([df, encoded_df], axis=1).drop(columns=[column_name])
        
        return df
    
    # `ad_network` sütununu işle
    df = preprocess_ad_network_one_hot(df)
    
    # İşlenmiş veriyi dosyaya kaydet
    df.to_csv(file_path, index=False)




# Fonksiyonu çağır
file_path = 'final_train.csv'
preprocess_and_save(file_path)

file_path = 'final_test.csv'
preprocess_and_save(file_path)