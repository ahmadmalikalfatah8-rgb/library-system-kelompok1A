from Perpustakaan import Perpustakaan
from buku import Buku
from penyimpanan import PenyimpananData

class Aplikasi:
    def __init__(self):
        penyimpanan = PenyimpananData("data_buku.txt")
        self.perpustakaan = Perpustakaan(penyimpanan)
        penyimpanan.periksa_file()
        self.perpustakaan.muat_data()

    def jalankan(self):
        while True:
            self.tampilkan_menu()
            pilihan = input("Pilih menu (1-5): ").strip()

            if pilihan == "1":
                self.menu_tambah_buku()
            elif pilihan == "2":
                self.menu_cari_buku()
            elif pilihan == "3":
                self.menu_hapus_buku()
            elif pilihan == "4":
                self.menu_update_buku()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan aplikasi ini.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def tampilkan_menu(self):
        print("\n=== Aplikasi Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Hapus Buku")
        print("4. Update Buku")
        print("5. Keluar")

    def menu_tambah_buku(self):
        print("\n=== Tambah Buku ===")
        kode_buku = input("Masukkan kode buku: ").strip()
        judul = input("Masukkan judul buku: ").strip()
        penulis = input("Masukkan penulis buku: ").strip()
        penerbit = input("Masukkan penerbit buku: ").strip()
        tahun_terbit = input("Masukkan tahun terbit buku: ").strip()
        jumlah_buku = input("Masukkan jumlah buku: ").strip()

        buku = Buku(kode_buku, judul, penulis, penerbit, tahun_terbit, jumlah_buku)
        if self.perpustakaan.tambah_buku(buku):
            print("Buku berhasil ditambahkan.")

    def menu_cari_buku(self):
        print("\n=== Cari Buku ===")
        kode_buku = input("Masukkan kode buku: ").strip()
        buku = self.perpustakaan.cari_buku(kode_buku)
        if buku:
            print(f"Kode Buku: {buku.kode_buku}")
            print(f"Judul: {buku.judul}")
            print(f"Penulis: {buku.penulis}")
            print(f"Penerbit: {buku.penerbit}")
            print(f"Tahun Terbit: {buku.tahun_terbit}")
            print(f"Jumlah Buku: {buku.jumlah_buku}")
        else:
            print("Buku tidak ditemukan.")

    def menu_hapus_buku(self):
        print("\n=== Hapus Buku ===")
        kode_buku = input("Masukkan kode buku: ").strip()

        if self.perpustakaan.hapus_buku(kode_buku):
            print("Buku berhasil dihapus.")
        else:
            print("Buku tidak ditemukan, gagal dihapus.")

    def menu_update_buku(self):
        print("\n=== Update Buku ===")
        kode_buku = input("Masukkan kode buku: ").strip()
        buku = self.perpustakaan.cari_buku(kode_buku)
        if buku:
            print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
            judul = input(f"Judul ({buku.judul}): ").strip()
            penulis = input(f"Penulis ({buku.penulis}): ").strip()
            penerbit = input(f"Penerbit ({buku.penerbit}): ").strip()
            tahun_terbit = input(f"Tahun Terbit ({buku.tahun_terbit}): ").strip()
            jumlah_buku = input(f"Jumlah Buku ({buku.jumlah_buku}): ").strip()

            data_baru = {}
            if judul:
                data_baru["judul"] = judul
            if penulis:
                data_baru["penulis"] = penulis
            if penerbit:
                data_baru["penerbit"] = penerbit
            if tahun_terbit:
                data_baru["tahun_terbit"] = int(tahun_terbit)
            if jumlah_buku:
                data_baru["jumlah_buku"] = int(jumlah_buku)

            self.perpustakaan.update_buku(kode_buku, data_baru)
            print("Buku berhasil diupdate.")
        else:
            print("Buku tidak ditemukan.")