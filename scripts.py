import pandas as pd

def print_csv_columns(file_path):
    # CSV dosyasını yükleyin
    df = pd.read_csv(file_path)
    
    # Sütun isimlerini bastırın
    print(df.columns.tolist())

# Kullanmak istediğiniz CSV dosyasının yolunu belirtin
file_path = 'users_train.csv'
print_csv_columns(file_path)
