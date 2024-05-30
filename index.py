import requests
from tqdm import tqdm

# Meminta input dari pengguna untuk URL asli dan jumlah shortlink
original_url = input("Masukkan URL asli: ")
jumlah_short = int(input("Masukkan jumlah url short yang dihasilkan: "))
nama_file = input("Masukkan nama file output (tanpa ekstensi): ")

# URL API
url = 'https://urlshortener-self.vercel.app/shrink'

# Data yang akan dikirim dalam payload
data = {
    'original': original_url
}

# Membuat iterator tqdm untuk menampilkan bar progres
progress_bar = tqdm(total=jumlah_short, desc="Membuat Shortlinks", colour='green')

# List untuk menyimpan shortlinks
short_links = []

# Looping untuk membuat shortlink sejumlah jumlah_short
for i in range(jumlah_short):
    # Mengirim permintaan POST ke API
    response = requests.post(url, json=data)

    # Memeriksa respons
    if response.status_code == 200:
        # Mendapatkan shortlink dari respons JSON
        shortened_url = response.json()['url']
        short_links.append(shortened_url)
    else:
        print(f"Gagal membuat shortlink ke-{i + 1}. Kode status:", response.status_code)

    # Memperbarui bar progres
    progress_bar.update(1)

# Menyimpan shortlinks dalam file teks dalam format txt
filename = f"{nama_file}.txt"
with open(filename, "w") as file:
    for short_link in short_links:
        file.write(f"'{short_link}',\n")

print(f"\nShortlinks telah disimpan dalam file {filename} dengan format yang diinginkan.")
