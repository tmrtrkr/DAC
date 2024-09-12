import pandas as pd

# Train ve test CSV dosyalarını oku
train_df = pd.read_csv('users_train.csv')
test_df = pd.read_csv('users_test.csv')

# Train'den 8000 satır, test'ten 5000 satır örnek al
train_sample = train_df.sample(n=800, random_state=42)
test_sample = test_df.sample(n=500, random_state=42)

# Örnekleri yeni CSV dosyalarına kaydet
train_sample.to_csv('train_sample.csv', index=False)
test_sample.to_csv('test_sample.csv', index=False)

print("Sampling complete. Train sample has 800 rows, test sample has 500 rows.")
