
from buku import Buku
from penyimpanan import PenyimpananData

class Perpustakaan:

    def __init__(self, penyimpanan: PenyimpananData):
        self.koleksi_buku: dict[str, Buku] = {}
        self.penyimpanan = penyimpanan

    def muat_data(self) -> None:
        data_buku = self.penyimpanan.baca_data()

        koleksi_baru = {}

        for data in data_buku:
            buku = Buku(
                data["kode_buku"],
                data["judul"],
                data["penulis"],
                data["penerbit"],
                data["tahun_terbit"],
                data["jumlah_buku"]
            )

            kode = buku.kode_buku

            if kode in koleksi_baru:
                raise ValueError(
                    f"Kode buku duplikat ditemukan: {kode}"
                )

            koleksi_baru[kode] = buku

        # Mengganti koleksi setelah seluruh data berhasil dimuat
        self.koleksi_buku = koleksi_baru

    def tambah_buku(self, buku: Buku) -> bool:

        if not isinstance(buku, Buku):
            return False

        kode = buku.kode_buku

        # Memeriksa kode buku duplikat
        if kode in self.koleksi_buku:
            return False

        # Menambahkan buku ke dictionary
        self.koleksi_buku[kode] = buku

        try:
            self._simpan_koleksi()
            return True

        except OSError:
            # Membatalkan penambahan jika penyimpanan gagal
            del self.koleksi_buku[kode]
            return False

    def cari_buku(self, kode_buku: str) -> Buku | None:

        if not isinstance(kode_buku, str):
            return None

        kode_buku = kode_buku.strip()

        return self.koleksi_buku.get(kode_buku)

    def hapus_buku(self, kode_buku: str) -> bool:

        buku = self.cari_buku(kode_buku)

        if buku is None:
            return False

        # Menghapus buku dari dictionary
        del self.koleksi_buku[kode_buku.strip()]

        try:
            self._simpan_koleksi()
            return True

        except OSError:
            # Mengembalikan buku jika penyimpanan gagal
            self.koleksi_buku[buku.kode_buku] = buku
            return False

    def update_buku(
        self,
        kode_buku: str,
        data_baru: dict
    ) -> bool:

        buku = self.cari_buku(kode_buku)

        if buku is None:
            return False

        # Menyimpan kondisi buku sebelum diperbarui
        data_lama = buku.to_dict()

        # Memperbarui atribut buku
        berhasil = buku.perbarui_atribut(data_baru)

        if not berhasil:
            return False

        try:
            self._simpan_koleksi()
            return True

        except OSError:
            # Mengembalikan objek ke kondisi sebelumnya
            self.koleksi_buku[buku.kode_buku] = Buku(
                **data_lama
            )
            return False

    def _simpan_koleksi(self) -> None:

        data_buku = [
            buku.to_dict()
            for buku in self.koleksi_buku.values()
        ]

        self.penyimpanan.simpan_data(data_buku)
