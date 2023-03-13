class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append(self)

    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print(f"Halo {self.__nama_pelanggan}, ingin melakukan apa?")
        print("1. Lihat saldo\n2. Tarik tunai\n3. Transfer saldo\n4. Keluar")

        pilih = int(input("Masukan nomor input: "))
        if pilih == 1:
            self.lihat_saldo()
        elif pilih == 2:
            self.tarik_tunai()
        elif pilih == 3:
            self.transfer()
        print()

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")
    
    def tarik_tunai(self):
        saldo = int(input("Masukan jumlah nominal yang ingin ditarik: "))
        if saldo <= self.__jumlah_saldo:
            print("Saldo berhasil ditarik!")
            self.__jumlah_saldo -= saldo
        else:
            print("Nominal saldo yang Anda punya tidak cukup!")

    def transfer(self):
        saldo = int(input("Masukan nominal yang ingin ditransfer: "))
        if saldo <= self.__jumlah_saldo:
            input_rek = int(input("Masukan no rekening tujuan: "))

            rek_penerima = None
            for rekening in AkunBank.list_pelanggan:
                if input_rek == rekening.__no_pelanggan:
                    rek_penerima = rekening
                    break
            
            if rek_penerima == None:
                print("No rekening tujuan tidak dikenal! Kembali ke menu utama...\n")
                self.lihat_menu()
            else:
                self.__jumlah_saldo -= saldo
                rek_penerima.__jumlah_saldo += saldo
                print(f"Transfer Rp {saldo} ke {rek_penerima.__nama_pelanggan} sukses!")


Akun1 = AkunBank(1234, "Ahmad Zain Mahmud", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon musk", 9999999999)

Akun1.lihat_menu()