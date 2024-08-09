# website-rekindle

## Deskripsi

Proyek ini adalah contoh implementasi chatbot yang diintegrasikan ke dalam website. Website dihosting menggunakan GitHub Pages, sementara backend chatbot dikelola menggunakan serverless functions di Vercel.

## Struktur Proyek

- `frontend/` - Berisi file HTML, CSS, dan JavaScript untuk antarmuka pengguna.
- `api/` - Folder yang berisi serverless functions yang dihosting di Vercel.

## Prerequisites

1. Akun GitHub
2. Akun Vercel

## Langkah-Langkah Implementasi

### 1. Menyiapkan Frontend di GitHub Pages

1. **Buat Repository GitHub:**
   - Masuk ke GitHub dan buat repository baru.
   - Beri nama repository sesuai dengan format `username.github.io` jika ingin menggunakan domain `username.github.io` atau nama lain jika tidak.

2. **Upload File Frontend:**
   - Upload file HTML, CSS, dan JavaScript dari folder `frontend/` ke repository GitHub.

3. **Aktifkan GitHub Pages:**
   - Pergi ke tab "Settings" pada repository.
   - Di bagian "Pages," pilih branch yang berisi file frontend (misalnya, `main` atau `master`).
   - Klik "Save." GitHub Pages akan menghasilkan URL yang dapat diakses.

### 2. Menyiapkan Backend di Vercel

1. **Buat Akun Vercel dan Proyek Baru:**
   - Daftar di [Vercel](https://vercel.com/) dan login.
   - Buat proyek baru dan hubungkan ke repository GitHub yang sama atau berbeda.

2. **Tambahkan Serverless Functions:**
   - Di dalam proyek Vercel, buat folder bernama `api/` di root.
   - Tambahkan file serverless function (misalnya, `chatbot.py`) di folder `api/`:
     ```python
     from flask import Flask, request, jsonify
     app = Flask(__name__)

     @app.route('/api/chatbot', methods=['POST'])
     def chatbot():
         user_message = request.json.get('message')
         # Logika chatbot di sini
         response_message = f"Bot response to '{user_message}'"
         return jsonify({'response': response_message})
     ```

3. **Deploy Proyek di Vercel:**
   - Commit dan push perubahan ke repository.
   - Vercel akan secara otomatis mendeteksi dan mendeply serverless functions.

### 3. Menghubungkan Frontend dengan Backend

1. **Update Kode JavaScript Frontend:**
   - Modifikasi file JavaScript di frontend untuk menghubungkan ke endpoint serverless function di Vercel:
     ```javascript
     async function sendMessageToChatbot(message) {
       const response = await fetch('/api/chatbot', {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify({ message })
       });
       const data = await response.json();
       return data.response;
     }

     document.getElementById('send-button').addEventListener('click', async () => {
       const message = document.getElementById('message-input').value;
       const response = await sendMessageToChatbot(message);
       document.getElementById('chat').innerText = response;
     });
     ```

2. **Tes dan Verifikasi:**
   - Buka URL GitHub Pages dan pastikan antarmuka pengguna bekerja dengan baik.
   - Kirimkan pesan ke chatbot dan verifikasi bahwa respons yang diterima sesuai.

## Kontak

Jika kamu memiliki pertanyaan atau butuh bantuan, silakan hubungi [Kavatsmara@gmail.com](mailto:kavatsmara@gmail.com) atau buka isu di repository ini.

## Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
