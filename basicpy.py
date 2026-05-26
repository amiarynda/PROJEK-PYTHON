# def salam() :
#     print('Hello selamat datang di Taruna Bhakti!')
#     print('Semoga hari anda menyenangkan!')

# salam()
# salam()
# # ini function tanpa return, kalau tidak ada return tidak bisa dipakai dimana-mana hanya dalam satu block (seperti def dan salam), kalau ada return bisa dipakai dimana-mana meskipun di dalam def lain.

# # f tanpa parameter
# def hai():
#     print ("halo")
# hai()

# f dengan parameter
# def salam(nama):
#     print("Halo", nama)
# salam("TB")

# f dengan banyak parameter
# def data(nama, umur):
#     print('Nama:', nama)
#     print('Umur:', umur)

# data('Nia', 17)

# f dengan return
# def tambah(a, b):
#     return a + b

# hasil = tambah(5, 3)
# print(hasil) # bisa dipanggil kembali walaupun saat sudah di convert/masukkan ke variabel, karena menggunakan return function.

# f dengan return 2

# def luas_persegi(s):
#     return s * s

# hasil = luas_persegi(4)
# print(hasil + 10)

# f dengan return 3

# def hitung_gaji(gaji_pokok, bonus):
#     return gaji_pokok + bonus

# gaji_nia = hitung_gaji(3000000, 500000)
# pajak = gaji_nia * 0.1

# print("Gaji Bersih:", gaji_nia - pajak)

# f dengan return 5

def rata_rata(nilai1, nilai2, nilai3):
    return (nilai1 + nilai2 + nilai3) / 3

hasil = rata_rata(80, 90, 100)

print("rata-rata", hasil)

def login(username, password):
    if username == "admin" and password == "123":
        return "Login Berhasil"
    else:
        return "Login Gagal"
    
print(login("admin", "123"))
print(login("admin", "456"))