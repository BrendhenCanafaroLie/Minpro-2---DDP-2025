
import getpass
from prettytable import PrettyTable
import os


# Data ekskul pakai dictionary
ekskul = {
    1: {"nama": "Basket", "pembina": "Pak Andi", "jadwal": "Senin & Rabu 15.00"},
    2: {"nama": "Paduan Suara", "pembina": "Bu Sinta", "jadwal": "Selasa 16.00"},
    3: {"nama": "Pramuka", "pembina": "Pak Budi", "jadwal": "Jumat 14.00"}
}

#Fungsi Create (SIP)
def tambah_data(): 
    while True:
        try:
            nama = input("Masukkan nama ekskul: ")
            pembina = input("Masukkan nama pembina: ")
            jadwal = input("Masukkan jadwal: ")
            nomor = max(ekskul.keys(), default=0) + 1
            ekskul.update({ nomor: {"nama": nama, "pembina": pembina, "jadwal": jadwal} })
            print("Ekstrakurikuler berhasil ditambahkan!")
            break
        except KeyboardInterrupt:
            print("Terjadi gangguan Ctrl + C")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")
        except BaseException:
            print("Terjadi Error")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")

#Fungsi Read Cuman Karyawan
def tampilkan_data():
    if ekskul:
        tabel = PrettyTable(["No", "Nama Ekskul", "Pembina", "Jadwal"])
        for i, data in ekskul.items():
            tabel.add_row([i, data["nama"], data["pembina"], data["jadwal"]])
        print(tabel)
    else:
        print("Belum ada data ekskul.")


#Fungsi Update (SIP)
def ubah_data():
    while True:
        try:
            tampilkan_data()
            nomor = int(input("Masukkan nomor ekskul yang ingin diubah: "))
            nama = input("Masukkan nama ekskul baru: ")
            pembina = input("Masukkan nama pembina baru: ")
            jadwal = input("Masukkan jadwal baru: ")
            ekskul[nomor] = {"nama": nama, "pembina": pembina, "jadwal": jadwal}
            print(" Data berhasil diubah!")
            break
        except ValueError:
            print("Input harus berupa angka.")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")
        except KeyboardInterrupt:
            print("Terjadi gangguan Ctrl + C")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")
        except BaseException:
            print("Terjadi Error")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")

#Fungsi Delete(SIP)
def hapus_data():
    while True:
        try:
            tampilkan_data()
            nomor = int(input("Masukkan nomor ekskul yang ingin dihapus: "))
            del ekskul[nomor]
            print(" Data berhasil dihapus!")
            break
        except ValueError:
            print("Input harus berupa angka.")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")
        except KeyError:
            print("Nomor ekskul tidak ditemukan")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")
        except KeyboardInterrupt:
            print("Terjadi gangguan Ctrl + C")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")
        except BaseException:
            print("Terjadi Error")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")

#Penampilan menu dan login
def main():
    while True:
        print("=== Sistem Login ===")
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        # Verifikasi
        if username == "manager" and password == "123":
            role = "manager"
            print(" Login berhasil sebagai Manager\n")
            break
        elif username == "karyawan" and password == "456":
            role = "karyawan"
            print(" Login berhasil sebagai Karyawan\n")
            break
        else:
            print(" Username atau password salah")
            input("Silakan Coba lagi, Tekan enter")
            os.system("cls")

    # Menu utama
    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat Daftar Ekskul")
        if role == "manager":
            print("2. Tambah Ekskul")
            print("3. Ubah Ekskul")
            print("4. Hapus Ekskul")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                tampilkan_data()
            elif pilihan == 2 and role == "manager":
                tambah_data()
            elif pilihan == 3 and role == "manager":
                ubah_data()
            elif pilihan == 4 and role == "manager":
                hapus_data()
            elif pilihan == 5:
                print("Terima kasih, program selesai.")
                break
            else:
                print(" Menu pilihan tidak tersedia")
        except ValueError:
            print("Input harus berupa angka.")
        except KeyboardInterrupt:
            print("Terjadi gangguan Ctrl + C")

main()
