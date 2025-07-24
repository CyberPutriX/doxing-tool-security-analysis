# 1. Gambaran Umum Analisis

## Peringatan

⚠️ **Perhatian Penting:**  
Repositori ini bertujuan untuk edukasi keamanan siber. Informasi di dalamnya membedah sebuah tools yang beredar di internet untuk menunjukkan risiko nyata dari menjalankan perangkat lunak dari sumber yang tidak terpercaya. Jangan pernah menjalankan tools asli yang dianalisis di sini.

## Latar Belakang

Analisis ini dilakukan terhadap sebuah repository bernama **DOXING-TOOLS** oleh pengguna dengan nama alias **Rolandino**. Tools ini diklaim sebagai alat multi-fitur untuk melakukan **doxing**, yaitu proses mengumpulkan informasi pribadi seseorang melalui berbagai sumber data publik atau API. 

Awalnya, tools ini dicurigai sebagai hoax karena klaimnya yang terlalu bombastis. Namun, setelah penyelidikan lebih lanjut, tools ini ternyata fungsional. Meskipun demikian, tools ini menyimpan **risiko keamanan tersembunyi** yang signifikan bagi penggunanya.

### Tujuan Analisis

Tujuan utama dari analisis ini adalah untuk:

1. **Memverifikasi Cara Kerja Tools:**  
   Meneliti bagaimana tools ini beroperasi, termasuk fungsi-fungsi utamanya dan bagaimana ia berinteraksi dengan API eksternal.

2. **Mengidentifikasi Risiko Keamanan:**  
   Menganalisis potensi bahaya yang terkandung dalam kode sumber, seperti fungsi spyware atau malware yang dapat membahayakan privasi pengguna.

3. **Memberikan Pembelajaran bagi Komunitas:**  
   Memberikan wawasan kepada komunitas tentang pentingnya memeriksa kode sumber sebelum menjalankan perangkat lunak dari sumber yang tidak dikenal.

## Gambaran Umum Tools

Tools ini disebut sebagai **multi-feature doxing tool** yang dikembangkan oleh Rolandino. Berdasarkan analisis awal, tools ini memiliki fitur-fitur berikut:

1. **Pencarian Data Target:**  
   Tools ini mengklaim mampu mencari informasi pribadi target melalui berbagai sumber, seperti API publik, database leak, dan layanan OSINT (Open Source Intelligence).

2. **API Integration:**  
   Tools ini terhubung dengan puluhan API, termasuk API untuk validasi nomor telepon, pencarian alamat IP, dan analisis metadata.

3. **Fungsi Terenkripsi:**  
   Kode sumber utama tools ini dienkripsi menggunakan teknik base64 berlapis, yang membuatnya sulit dibaca dan dianalisis secara langsung.

### Fungsi Utama Tools

Tools ini memiliki beberapa fungsi utama, antara lain:

- **Validasi Nomor Telepon:**  
  Menggunakan library `phonenumbers` untuk mendapatkan lokasi dan provider dari nomor telepon target.

- **Pencarian Lokasi Berdasarkan Alamat IP:**  
  Menggunakan layanan seperti `ipinfo.io` untuk mendapatkan informasi geografis pengguna.

- **Integrasi dengan API Publik:**  
  Tools ini terhubung dengan berbagai API publik, seperti `numverify`, `leakcheck`, dan `ip-api`.

### Red Flags Awal

Selama analisis awal, beberapa tanda bahaya (red flags) terdeteksi:

1. **Kode Terenkripsi:**  
   Kode sumber utama tools ini dienkripsi menggunakan base64 berlapis. Ini adalah praktik yang tidak umum dalam pengembangan perangkat lunak open-source dan sering digunakan untuk menyembunyikan fungsi berbahaya.

2. **Fungsi Spyware Tersembunyi:**  
   Setelah berhasil mendekripsi kode sumber, ditemukan sebuah fungsi yang secara otomatis mengumpulkan data pengguna (seperti alamat IP, lokasi, dan provider internet) dan mengirimkannya ke penulis tools melalui API Telegram.

3. **Limitasi Penggunaan Harian:**  
   Tools ini memiliki mekanisme limitasi penggunaan harian yang mencatat aktivitas pengguna dalam file JSON (`user_limit.json`). Hal ini menunjukkan bahwa penulis tools ingin memantau siapa saja yang menggunakan tools ini.

## Kesimpulan Sementara

Berdasarkan analisis awal, tools ini bukan hanya alat untuk melakukan doxing, tetapi juga berfungsi sebagai **spyware** yang diam-diam mencuri data pengguna. Tindakan mengenkripsi kode sumber dan menyembunyikan fungsi berbahaya adalah indikator kuat bahwa tools ini dirancang dengan niat buruk.

Untuk detail lebih lanjut tentang temuan utama, silakan baca file [**2_decryption_process.md**](analysis/2_decryption_process.md).