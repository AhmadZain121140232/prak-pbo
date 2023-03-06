class Mhs:
  def __init__(self, nama, NIM, kelasPBO, SKS):
    self.nama = nama
    self.NIM = NIM
    self.kelasPBO = kelasPBO
    self.SKS = SKS

  
  def info(self):
    print("Nama : " + self.nama )
    print("NIM : " + self.NIM )
    print("Kelas PBO Siakad : " + self.kelasPBO )
    print("SKS : " + self.SKS )

nama = input("Masukkan nama : ") 
NIM = input("Masukkan NIM : ") 
kelasPBO = input("Masukkan Kelas PBO Siakad : ") 
SKS = input("Masukkan jumlah SKS : ") 

print("=================")
Objek = Mhs(nama, NIM, kelasPBO, SKS)

Objek.info()