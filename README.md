# Minpro-2
# Profil
### Nama  : Brendhen Canafaro Lie
### NIM   : 250916033
### Kelas : Sistem Informasi A (2025)

# Deskripsi Singkat
Program yang saya buat ini merupakan mini project 2 pada mata kuliah **Praktikum Dasar-Dasar Pemrograman**. Program di koding menggunakan bahasa program Python yang menerapkan konsep CRUD (Create, Read, Update, Delete). Dengan menambahkan beberapa ketentuan fungsi yang telah dipelajari dalam mata kuliah. Hal yang di tambahkan adalah Dictionary, Perulangan For dan While, dan hal lainnya\
Tema yang dipilih adalah Ekstrakurikuler dengan tujuan untuk mengelola data kegiatan ekstrakurikuler di sekolah.
Terdapat 2 role yang tersedia dalam program ini yaitu
1) Manager (Password : 123)\
   Dapat mengakses 5 operasi menu yaitu CRUD (Create, Read, Update dan Delete)
3) Karyawan (Password : 456)\
   Hanya dapat mengakses penggunaan operasi melihat daftar ekstrakurikuler yang sudah ada

# Flowchart
[Gambar Flowchart]

# Penjelasan Flowchart
## Mulai Program
Program dimulai, lalu langsung menuju ke fungsi main() dimana proses Login dimulai.

## Login
Pengguna harus memasukkan username dan password. Terdapat 2 percabangan, yaitu sebagai berikut :
1) Jika username & password salah, program kembali ke login dan menyuruh pengguna untuk melakukan ulang proses login.
3) Jika benar, program akan menentukan role kita dan pengaksesan untuk menjalankan menu operasi diberikan.

## Penampilan Menu
Program akan menampilkan menunya berdasarkan role pengguna, yaitu sebagai berikut :
1. Manager :
   a. Lihat Daftar Ekskul
   b. Tambah Ekskul
   c. Ubah Ekskul
   d. Hapus Ekskul
   e. Keluar
3. Karyawan
   a. Lihat Daftar Ekskul
   b. Keluar

## Pilihan Menu
Proses Berdasarkan Pilihan Menu :

1) Pilihan 1 (Lihat Daftar Ekskul)
Menampilkan seluruh daftar ekstrakurikuler yang ada di dalam dictionary. Data ditampilkan dalam bentuk tabel (PrettyTable).

2) Pilihan 2 (Tambah Ekskul) (Manager saja)
Pengguna menginput nama ekskul, pembina, dan jadwal, setelah itu data baru otomatis disimpan ke dictionary.

3) Pilihan 3 (Ubah Ekskul) (Manager saja)
Pengguna memilih nomor ekskul yang ingin diubah, kemudian pengguna akan input data baru (nama, pembina, jadwal), dan program akan mengganti data lama.

4) Pilihan 4 (Hapus Ekskul) (Manager saja)
Pengguna memilih nomor ekskul dari daftar ekstrakurikuler, setelah itu program akan mengambil pilihan pengguna dan menghapus dari dictionary.

5) Pilihan 5 (Keluar)
Program menampilkan akan menuliskan "Terima kasih, program selesai". Setelah itu program akan berhenti

## Error Handling
Jika pengguna memasukkan input yang tidak sesuai:
1) except ValueError, Input harus berupa angka

2) except KeyError, Input Nomor ekskul tidak ada

2) except KeyboardInterrupt, Pengguna menekan Ctrl+C

3) except BaseException, Error lainnya yang tidak tercover

# Selesai Program
Dengan pengguna yang telah memilih menu operasi ke lima yaitu Keluar sebagai pengakhir program


# Kerangka Program
## Array
<img width="541" height="93" alt="image" src="https://github.com/user-attachments/assets/528d1122-2d27-423b-ab2b-37816470ebab" />\
Dibagian awal program, terlihat sebuah array yang sudah terisi, hal ini dikarenakan program tidak memakai **sistem perulangan**, mengharuskan array harus diisi terlebih dahulu sebelum dijalankan

## Print Menu
<img width="536" height="195" alt="image" src="https://github.com/user-attachments/assets/f13a140f-c4fc-4865-9620-337b32659fdd" />\
Di atas ini adalah bagian progam yang bekerja untuk menampilkan menu

## Pilihan 
<img width="437" height="24" alt="image" src="https://github.com/user-attachments/assets/42109bc6-3d61-4daf-a6b7-f32bb237048b" />\
Di sini program akan menginput pilihan nomor yang anda input dan akan dimasukkan kedalam **variabel data**

## Program Fungsi Pertama
<img width="493" height="192" alt="image" src="https://github.com/user-attachments/assets/17cec980-d88e-4faf-8eda-9efa4b0af3c3" />\
