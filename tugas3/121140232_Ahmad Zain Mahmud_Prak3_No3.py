class Warga:
    #property kelas
    total_warga = 0
    
    def __init__(self, nama, no_hp, nik):
        # atribut instance
        self.nama = nama #public, bebas akses
        self._no_hp = no_hp #protected, hanya bisa diakses dalam class dan turunan
        self.__nik = nik  #private, hanya bisa diakses dalam class
        Warga.total_warga += 1
    
    def tampilkan_info(self):
        print(f"Nama  : {self.nama}")
        print(f"Nomor Handphone  : {self._no_hp}")
        print(f"NIK  : {self.__nik}")
        print()
      
    def ubah_nama(self, nama_baru):
        self.nama = nama_baru

    def ubah_no_hp(self, no_hp_baru):
      #perlakuannya sama seperti public, penanda kepada developer untuk tidak diubah, hanya untuk di akses
        self._no_hp = no_hp_baru
  
    def ubah_nik(self, nik_baru):
      #harus diakses melalui kelasnya
        self._Warga__nik = nik_baru

Warga1 = Warga("Zain", "0812", 12345)
Warga1.tampilkan_info()
Warga1.ubah_nama("Zia")
Warga1.ubah_no_hp("0813")
Warga1.ubah_nik(45678)
Warga1.tampilkan_info()
