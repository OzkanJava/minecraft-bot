import os
import glob

# Hedef klasörün yolunu belirtin
folder_path = 'C://Users//ozkan//Desktop//pxa//pxa2'

# Klasördeki tüm dosya adlarını al
files = glob.glob(os.path.join(folder_path, '*'))

for file_path in files:
    # Dosya adını al
    file_name = os.path.basename(file_path)
    # Dosya uzantısını kontrol et
    if not file_name.lower().endswith('.png'):
        try:
            os.remove(file_path)
            print(f'Silindi: {file_path}')
        except Exception as e:
            print(f'Hata oluştu: {file_path}, Hata: {e}')
