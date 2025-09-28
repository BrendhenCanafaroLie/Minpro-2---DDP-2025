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
<img width="1550" height="1866" alt="Minpro2 drawio" src="https://github.com/user-attachments/assets/641ca3ac-f9c7-43a9-84ce-4e4bfdb5ecb2" />

# Penjelasan Flowchart
## Mulai Program
Program dimulai, lalu langsung menuju ke fungsi main() dimana proses Login dimulai.

## Login
Pengguna harus memasukkan username dan password. Terdapat 2 percabangan, yaitu sebagai berikut :
1) Jika username & password salah, program kembali ke login dan menyuruh pengguna untuk melakukan ulang proses login.
3) Jika benar, program akan menentukan role kita dan pengaksesan untuk menjalankan menu operasi diberikan.

## Penampilan Menu
Program akan menampilkan menunya berdasarkan role pengguna, yaitu sebagai berikut :
1. Manager :\
   a. Lihat Daftar Ekskul\
   b. Tambah Ekskul\
   c. Ubah Ekskul\
   d. Hapus Ekskul\
   e. Keluar
3. Karyawan\
   a. Lihat Daftar Ekskul\
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
## Import Fungsi
<img width="358" height="78" alt="image" src="https://github.com/user-attachments/assets/b1c4e3ce-d777-4efc-bf91-cd90b6b8fa9a" />

## Dictionary
<img width="788" height="154" alt="image" src="https://github.com/user-attachments/assets/d9df80d9-d60d-4810-8d08-07cd9284c008" />

## Fungsi Menambah Ekskul
<img width="861" height="457" alt="image" src="https://github.com/user-attachments/assets/aa86f144-1467-4b5f-a210-fcf810947f72" />

## Fungsi Melihat Daftar Ekskul
<img width="759" height="229" alt="image" src="https://github.com/user-attachments/assets/5e8fa80d-9fa3-4e48-b144-87ab903a8c3c" />

## Fungsi Mengubah Ekskul
<img width="792" height="557" alt="image" src="https://github.com/user-attachments/assets/f83efe0a-400a-4a5e-bf8d-fa0bca9d1bed" />

## Fungsi Menghapus Ekskul
<img width="774" height="592" alt="image" src="https://github.com/user-attachments/assets/0a51700c-c8db-4c17-93f7-1b18d2c8dd54" />

## Fungsi Keluar
<img width="439" height="81" alt="image" src="https://github.com/user-attachments/assets/9435e25a-c33e-45ac-a935-bc10e94b660c" />

## Fungsi Login
<img width="613" height="469" alt="image" src="https://github.com/user-attachments/assets/642b0adf-3aa8-4d63-80ac-eca043b96dc1" />

## Fungsi Menu
<img width="517" height="450" alt="image" src="https://github.com/user-attachments/assets/5d7ef232-4d85-4f68-8e84-f4128b1ac21b" />

## Fungsi pilihan
<img width="491" height="456" alt="image" src="https://github.com/user-attachments/assets/527a95e4-e0d8-4bcf-a5f1-6cdadba71e7f" />


# Output dan Penggunaan
## Menu Program (Manager)
<img width="462" height="290" alt="image" src="https://github.com/user-attachments/assets/b2facbbd-26ff-4109-b6a1-fef8737503c7" />

## Menu Program (Karyawan)
<img width="433" height="234" alt="image" src="https://github.com/user-attachments/assets/381a7926-bdbf-48ae-b74f-9145f41eece7" />

## Tambah Ekskul
<img width="417" height="244" alt="image" src="https://github.com/user-attachments/assets/524ee3dd-4051-42f1-9953-4f43a8e57502" />

## Menampilkan Daftar Ekskul
<img width="541" height="327" alt="image" src="https://github.com/user-attachments/assets/3882af94-19a9-4404-9aa4-17c51821030e" />

## Mengubah Ekskul
<img width="508" height="417" alt="image" src="https://github.com/user-attachments/assets/b21b057e-bbb0-4ae4-8347-45376d9c72db" />

## Menghapus Ekskul
<img width="535" height="356" alt="image" src="https://github.com/user-attachments/assets/b1bfa571-719e-4385-81a6-15dbb75cc8dd" />

## Mengakhiri Program
<img width="313" height="195" alt="image" src="https://github.com/user-attachments/assets/549e6c8d-700e-41df-9c03-6d1295cfb6d5" />

## Beberapa Error Handling
<img width="356" height="118" alt="image" src="https://github.com/user-attachments/assets/4a945586-5481-4eed-90be-bb24c8ea74ae" />
<img width="527" height="376" alt="image" src="https://github.com/user-attachments/assets/3539f8ba-006c-45c2-9257-05b1d1d83ee6" />
<img width="627" height="324" alt="image" src="https://github.com/user-attachments/assets/0bf948b8-f236-4423-b2ce-1259582886b2" />




