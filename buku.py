class Buku:
    def __init__(self, kode_buku, judul, penulis, penerbit, tahun_terbit, jumlah_buku):
        self.kode_buku = kode_buku.strip()
        self.judul = judul.strip()
        self.penulis = penulis.strip()
        self.penerbit = penerbit.strip()
        self.tahun_terbit = int(tahun_terbit)
        self.jumlah_buku = int(jumlah_buku)

    def validasi_atribut(self, nama_atribut, nilai):
        if nama_atribut in ["kode_buku", "judul", "penulis", "penerbit"]:
            return isinstance(nilai, str) and nilai.strip() != ""
        if nama_atribut == "tahun_terbit":
            return isinstance(nilai, int) and nilai > 0
        if nama_atribut == "jumlah_buku":
            return isinstance(nilai, int) and nilai >= 0
        return False

    def perbarui_atribut(self, data_baru):
        if not isinstance(data_baru, dict):
            return False

        if "judul" in data_baru and self.validasi_atribut("judul", str(data_baru["judul"])):
            self.judul = str(data_baru["judul"]).strip()
        if "penulis" in data_baru and self.validasi_atribut("penulis", str(data_baru["penulis"])):
            self.judul = str(data_baru["penulis"]).strip()
        if "penerbit" in data_baru and self.validasi_atribut("penerbit", str(data_baru["penerbit"])):
            self.judul = str(data_baru["penerbit"]).strip()
        if "tahun_terbit" in data_baru and self.validasi_atribut("tahun_terbit", str(data_baru["tahun_terbit"])):
            self.judul = str(data_baru["tahun_terbit"]).strip()
        if "jumlah_buku" in data_baru and self.validasi_atribut("jumlah_buku", str(data_baru["jumlah_buku"])):
            self.judul = str(data_baru["jumlah_buku"]).strip()

        return True

    def to_dict(self):
        return{
            "kode_buku": self.kode_buku,
            "judul": self.judul,
            "penulis": self.penulis,
            "penerbit": self.penerbit,
            "tahun_terbit": self.tahun_terbit,
            "jumlah_buku": self.jumlah_buku
        }
