print("=====================================")
print("Latihan 1\n")

n = int(input())

for i in range (n):
  for j in range (n):
    print("*", end = "")
  print()

print("=====================================")
print("Latihan 2\n")

for i in range (3):
  uname = input("Username anda : ")
  pw = input("Password anda : ")

  if uname == "informatika" and pw == "12345678":
    print("Berhasil login!")
    break
  else :
    print("Username atau password salah coba lagi")

else:
  print("Akun anda diblokir!")