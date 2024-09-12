import pandas as pd

def total_retention(df, retention_prefix='RetentionD'):
    retention_columns = [col for col in df.columns if col.startswith(retention_prefix)]
    df['total_retention'] = df[retention_columns].sum(axis=1)
    return df[['ID', 'total_retention']]

def total_level_advanced(df, level_advanced_prefix='LevelAdvancedCountD'):
    level_advanced_columns = [col for col in df.columns if col.startswith(level_advanced_prefix)]
    df['total_level_advanced'] = df[level_advanced_columns].sum(axis=1)
    return df[['ID', 'total_level_advanced']]

def total_level_duration(df, level_duration_prefix='Level_'):
    level_duration_columns = [col for col in df.columns if col.startswith(level_duration_prefix)]
    df['total_level_duration'] = df[level_duration_columns].sum(axis=1)
    return df[['ID', 'total_level_duration']]

def total_ad_revenue(df, ad_revenue_prefix='AdRevenueD'):
    ad_revenue_columns = [col for col in df.columns if col.startswith(ad_revenue_prefix)]
    df['total_ad_revenue'] = df[ad_revenue_columns].sum(axis=1)
    df['total_ad_revenue'] = df['total_ad_revenue'].round(2)  # Yuvarlama işlemi
    return df[['ID', 'total_ad_revenue']]

def total_iap_revenue(df, iap_revenue_prefix='IAPRevenueD'):
    iap_revenue_columns = [col for col in df.columns if col.startswith(iap_revenue_prefix)]
    df['total_iap_revenue'] = df[iap_revenue_columns].sum(axis=1)
    df['total_iap_revenue'] = df['total_iap_revenue'].round(2)  # Yuvarlama işlemi
    return df[['ID', 'total_iap_revenue']]

def add_first_prediction(df):
    return df[['ID', 'first_prediction']]

def process_data(file_path, output_path):
    df = pd.read_csv(file_path)
    
    df_total_retention = total_retention(df)
    df_total_level_advanced = total_level_advanced(df)
    df_total_level_duration = total_level_duration(df)
    df_total_ad_revenue = total_ad_revenue(df)
    df_total_iap_revenue = total_iap_revenue(df)
    df_first_prediction = add_first_prediction(df)
    
    # Birleştirme işlemi
    df_combined = df_total_retention.merge(df_total_level_advanced, on='ID')
    df_combined = df_combined.merge(df_total_level_duration, on='ID')
    df_combined = df_combined.merge(df_total_ad_revenue, on='ID')
    df_combined = df_combined.merge(df_total_iap_revenue, on='ID')
    df_combined = df_combined.merge(df_first_prediction, on='ID')
    
    # Sonuçları CSV dosyasına kaydet
    df_combined.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

# Dosya yollarını belirtin
input_file_path = 'user_features_train.csv'
output_file_path = 'processed_data_train.csv'
process_data(input_file_path, output_file_path)

input_file_path = 'user_features_test.csv'
output_file_path = 'processed_data_test.csv'
process_data(input_file_path, output_file_path)
