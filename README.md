# Soal Pemrograman Logika & Struktur Data - RSUD Sumenep

Pilih **salah satu** bahasa pemrograman (**Python** atau **PHP**) untuk mengimplementasikan solusi dari setiap soal.

Setiap soal memiliki folder masing-masing di [`python/`](python/) atau [`php/`](php/) sesuai bahasa yang kamu pilih. Kamu hanya perlu menulis kode solusi di file yang sudah disediakan.

> ⚠️ **Catatan:** Folder `test_php/` dan `test_python/` bersifat internal dan tidak perlu diubah. Unit test akan berjalan secara otomatis terhadap solusi yang kamu buat.

---

## Bobot Penilaian

| Soal | Topik | Bobot Nilai |
|:----:|-------|:-----------:|
| 1 | Maximum penjumlahan triplets | **25** |
| 2 | Penjumlahan dua bilangan terkecil | **15** |
| 3 | Ular Tangga Pattern | **40** |
| 4 | Maskify (String masking) | **20** |
| | **Total** | **100** |

Bobot nilai ditentukan berdasarkan tingkat kesulitan setiap soal:
- **Soal 3 (40)** — tersulit, membutuhkan logika perulangan bersarang dengan pola arah bolak-balik dari bawah ke atas.
- **Soal 1 (25)** — menengah, membutuhkan deduplikasi data dan seleksi tiga nilai terbesar.
- **Soal 4 (20)** — mudah, manipulasi string dasar.
- **Soal 2 (15)** — termudah, cukup sorting dan penjumlahan dua elemen pertama.

---

## Ketentuan Pengumpulan

1. **Dilarang menggunakan AI** (ChatGPT, GitHub Copilot, atau tools AI lainnya) dalam mengerjakan soal-soal ini. Keputusan ini diambil untuk mengukur kemampuan logika dan pemahaman struktur data secara mandiri.`
2. Setelah selesai mengerjakan, **compress folder project** ini (format `.zip`).
3. Upload file hasil compress ke link Google Form berikut:
   👉 [**Kumpulkan Jawaban di Sini**](https://form.jotform.com/261227395962061)

> ⚠️ Pastikan semua file solusi sudah terisi sebelum dikompres dan diupload.

---

## Deskripsi Soal

### Soal 1 - Maximum penjumlahan triplets
Tugas
Diberikan sebuah array/daftar bilangan bulat, temukan jumlah maksimum dari 3 elemen array yang BERBEDA.

Catatan:

Ukuran array minimal 3.

Elemen array bisa bernilai nol atau negatif.

Kemunculan angka yang sama dalam array bisa terjadi, jadi duplikasi tidak diikutsertakan saat menjumlahkan.

Input >> Output Contoh
```python
maxTriSum({3,2,6,8,2,3}) ==> return (17)
# Triplet terbaik = {6,8,3}, jumlahnya 17

maxTriSum({2,1,8,0,6,4,8,6,2,4}) ==> return (18)
# Triplet terbaik = {8,6,4}, jumlahnya 18

maxTriSum({-7,12,-7,29,-5,0,-7,0,0,29}) ==> return (41)
# Triplet terbaik = {12,29,0}, jumlahnya 41
```

### Soal 2 - Penjumlahan dua bilangan terkecil 
Buatlah sebuah fungsi yang mengembalikan **jumlah dari dua bilangan positif terkecil** dari sebuah array yang berisi minimal 4 bilangan bulat positif.
Tidak ada bilangan pecahan (float) atau bilangan non-positif yang akan diberikan sebagai input.

Contoh Soal

Jika array yang diberikan adalah `[19, 5, 42, 2, 77]`, maka keluarannya adalah `7` (karena dua bilangan terkecil adalah 2 dan 5, lalu dijumlahkan).

Jika array `[10, 343445353, 3453445, 3453545353453]`, maka keluarannya adalah `3453455` (karena 10 + 3453445 = 3453455).

Contoh lain: `[4, 1, 7, 3]` → `4` (1 + 3 = 4)

### Soal 3 - Ular Tangga Pattern
Buatlah sebuah program yang dapat membuat pola angka seperti ular tangga tetapi dimulai dari baris bawah
dengan ukuran yang ditentukan oleh input pengguna.

Jika input `n = 3`, program harus membuat kotak berukuran `n x n` dengan angka 1 sampai `n²`.

Pola dimulai dari **kiri bawah** (baris ke-n, kolom ke-1), lalu bergerak ke kanan untuk mengisi baris bawah,
kemudian naik satu baris ke atas dan bergerak ke kiri, dan seterusnya seperti ular tangga dari bawah ke atas.

**Contoh input = 3**
Output yang diharapkan:
```text
7 8 9
6 5 4
1 2 3
```
Penjelasan:

Baris 3 (bawah): 1 2 3 (ke kanan)

Baris 2: 6 5 4 (ke kiri, sambung dari 3 ke 4: naik lalu mundur)

Baris 1: 7 8 9 (ke kanan lagi)

### Soal 4 
Biasanya saat Anda membeli sesuatu, Anda ditanya apakah nomor kartu kredit, nomor telepon, atau jawaban pertanyaan rahasia Anda masih benar. Namun, karena seseorang bisa mengintip dari belakang, Anda tidak ingin informasi tersebut ditampilkan di layar. Sebagai gantinya, kita samarkan.

Tugas Anda adalah menulis fungsi `maskify`, yang mengubah semua karakter **kecuali empat karakter terakhir** menjadi tanda `'#'`.

Contoh (input → output):
```text
"4556364607935616" → "############5616"
     "64607935616" →      "#######5616"
               "1" →                "1"
                "" →                 ""
"Skippy" → "##ippy"
"Nananananananananananananananana Batman!" → "####################################man!"
```
---



