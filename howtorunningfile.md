Cara Menjalankan Kalkulator GUI

1. Pastikan Python sudah terpasang di komputer Anda 
   Untuk mengecek apakah Python sudah terpasang, buka Command Prompt (Windows) atau terminal (MacBook/Linux), lalu ketikkan perintah berikut:
   ```bash
   python --version
   ```
   Jika Python sudah terpasang, versi Python akan ditampilkan. Jika belum, unduh dan pasang Python dari [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Windows: Setelah mengunduh dan memasang Python, pastikan untuk memilih opsi Add Python to PATH saat instalasi.
   - MacBook/Linux: Biasanya Python sudah terpasang secara default. Jika belum, Anda bisa menginstalnya dengan menggunakan Homebrew (MacBook) atau apt-get (Linux).

2. Pastikan Tkinter sudah terinstal.  
   Tkinter adalah library GUI yang sudah termasuk dalam instalasi Python. Untuk mengecek apakah Tkinter sudah terinstal, buka terminal atau command prompt dan jalankan perintah berikut:
   ```bash
   python -m tkinter
   ```
   - Windows: Tkinter sudah terpasang secara otomatis dengan Python, jadi Anda tidak perlu menginstalnya lagi.
   - MacBook: Tkinter biasanya sudah terinstal bersama Python yang terpasang. Jika terjadi masalah, Anda bisa menginstalnya menggunakan Homebrew dengan perintah `brew install python-tk`.
   - Linux: Jika Tkinter tidak terpasang, Anda bisa menginstalnya dengan perintah berikut di terminal:
     ```bash
     sudo apt-get install python3-tk  # untuk pengguna Linux berbasis Debian/Ubuntu
     ```
3. Simpan script kalkulator GUI ke dalam file  
   Salin seluruh kode program yang telah diberikan ke dalam sebuah file dengan nama `calculator_gui.py`.
4. Jalankan aplikasi kalkulator  
   Untuk menjalankan kalkulator, buka Command Prompt (Windows) atau terminal (MacBook/Linux), lalu arahkan ke folder tempat Anda menyimpan file `calculator_gui.py`. Kemudian ketikkan perintah berikut:
   ```bash
   python calculator_gui.py
   ```
5. Nikmati kalkulator GUI!  
   Aplikasi kalkulator akan muncul dengan tampilan antarmuka grafis (GUI). Anda bisa mulai menggunakannya untuk melakukan perhitungan matematis.

Catatan:  
- Jika Anda mengalami masalah saat menjalankan program, pastikan Python dan Tkinter telah terinstal dengan benar di sistem Anda.
- Untuk mode gelap (Dark Mode) atau terang (Light Mode), Anda bisa menggunakan tombol "Dark Mode" di bagian bawah aplikasi untuk mengganti tema antarmuka sesuai kebutuhan.
