# buatlah projek program CLI yang ada
# 1. validasi input/error handling 
# 2. tampilan CLI komplit dan lengkap
# 3. menggunakan lebih dari 5 function
# 4. menggunakan dictionary/list yang baik
# 5. upload ke github, buat read me nya minta ke AI

from statistics import mean
hp_prices = [['iphone', 15000000], ['Samsung', 12000000], ['Vivo', 10000000], ['Nokia', 2000000], ['Asus', 4000000]]

def display_menu():
    print ("\nMenu:")
    print ("1. Lihat seluruh data")
    # print ("2. Tambah data")
    # print ("3. Hapus data")
    # print ("4. Ubah Harga")
    # print ("5. Hitung rata-rata")
    print ("2. Keluar")

def lihat_data():
    print("\nData Harga Hp:")

    if not hp_prices:
        print("Tidak ada data.")
        return
    
    for hp, harga in hp_prices:
        print(f"-{hp}: Rp{harga:,}")

def main():
    while True:
        display_menu()
        choice = input("Pilih menu (1-2): ")

        if choice == '1':
            lihat_data(1)
        elif choice == '2':
            print ("Terima kasih! Program selesai.")
        else:
            print ("Pilihan tidak valid. Silakan pilih menu yang benar.")


# jsa
main()