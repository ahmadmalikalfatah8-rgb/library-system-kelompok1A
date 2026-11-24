from pathlib import Path

class PenyimpananData:
    def __init__(self, nama_file):
        self.nama_file = Path(nama_file)

    def periksa_file(self):
        if not self.nama_file.exists():
            self.nama_file.write_text("", encoding="utf-8")

    def baca_data(self):
        if not self.nama_file.exist():
            return[]

        teks = self.nama_file.read_text(encoding="utf-8")
        if teks.strip() == "":
            return[]

        hasil = []
        for blok in teks.split("---"):
            blok = blok.strip()
            if blok == "":
                continue

            data = {}
            for baris in blok.splitlines():
                if baris.strip() == "":
                    continue

                label, nilai = baris.split(" : ", 1)
                label = label.strip()
                nilai = nilai.strip()

                if label == "Kode Buku":
                    data["kode_buku"] = nilai
                elif label == "Judul":
                    data["judul"] = nilai
                elif label == "Penulis":
                    data["penulis"] = nilai
                elif label == "Penerbit":
                    data["penerbit"] = nilai
                elif label == "Tahun Terbit":
                    data["tahun_terbit"] = int(nilai)
                elif label == "Jumlah Buku":
                    data["jumlah_buku"] = int(nilai)

            hasil.append(data)
        
        return hasil

    def simpan_data(self, data_buku):
        teks = ""
        for data in data_buku:
            teks += "Kode Buku : " + data["kode_buku"] + "\n"
            teks += "Judul : " + data["judul"] + "\n"
            teks += "Penulis : " + data["penulis"] + "\n"
            teks += "Penerbit : " + data["penerbit"] + "\n"
            teks += "Tahun Terbit : " + str(data["tahun_terbit"]) + "\n"
            teks += "Jumlah Buku : " + str(data["jumlah_buku"]) + "\n"

        self.nama_file.write_text(teks, encoding="utf-8")