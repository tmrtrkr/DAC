import pandas as pd

def adjust_release_date(file_path_xlsx, output_file_csv):
    """
    This function reads an Excel file, converts the 'release_date' column to numeric (if possible),
    subtracts 2000 from the 'release_date' column, adds the result as a new column, and saves the
    modified DataFrame to a new CSV file.
    
    :param file_path_xlsx: Path to the input Excel (.xlsx) file
    :param output_file_csv: Path to the output CSV file where changes will be saved
    """
    # Load the Excel file
    df = pd.read_excel(file_path_xlsx)

    # Convert the 'release_date' column to numeric, coerce errors (invalid data becomes NaN)
    df['release_date'] = pd.to_numeric(df['release_date'], errors='coerce')

    # Subtract 2000 from the 'release_date' column (only if the value is numeric)
    df['adjusted_release_date'] = df['release_date'].apply(lambda x: x - 2000 if pd.notnull(x) else None)

    # Save the modified DataFrame to a CSV file
    df.to_csv(output_file_csv, index=False)

    print(f"New column added and file saved to {output_file_csv}.")


def filter_device_models_by_year(input_file):
    """
    Bu fonksiyon bir CSV dosyasını okur ve her marka için 2024 ile 2020 yılları arasında her yıl için 3 ayrı modeli döndürür.
    Sonuçları konsola yazdırır.

    :param input_file: Giriş CSV dosyası
    """
    # CSV dosyasını oku
    df = pd.read_csv(input_file)
    
    # 'release_date' sütununun sadece yıllarını alıyoruz (tarih formatındaysa)
    df['release_year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
    
    # 2020 ile 2024 yılları arasındaki verileri filtrele
    filtered_df = df[(df['release_year'] >= 2020) & (df['release_year'] <= 2024)]
    
    # Boş sonuçları kaldırmak için dropna uyguluyoruz
    filtered_df = filtered_df.dropna(subset=['release_year'])
    
    # Her marka için 2024'ten 2020'ye kadar her yıl 3 model seçme işlemi
    for brand in filtered_df['device_brand'].unique():
        brand_df = filtered_df[filtered_df['device_brand'] == brand]
        
        for year in range(2024, 2020 - 1, -1):
            year_df = brand_df[brand_df['release_year'] == year]
            
            # Eğer o yıl için 3 veya daha fazla model varsa, 3 tanesini seç
            if len(year_df) >= 3:
                selected_models = year_df.sample(3)
                print(f"\nBrand: {brand}, Year: {year}")
                print(selected_models[['device_model', 'release_date']])

# Örnek kullanım
filter_device_models_by_year('grouped_device_models.csv')



#adjust_release_date('grouped_device_models.xlsx', 'grouped_device_models.csv')
