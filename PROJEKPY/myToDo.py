tasks = []

def tampil_menu():
    print("\n=~=~=~📝 My TO DO LIST ^__^! =~=~=~")
    print("\n=~ 📎 Silakan pilih menu di bawah: ~=")
    print("\n1. Tambah task")
    print("2. Lihat semua task")
    print("3. Tandai sebagai selesai")
    print("4. Tandai sebagai prioritas")
    print("5. Hapus task")
    print("6. Keluar")
    print("\n====================================")

def tambah_task():
    task = input("Masukkan task baru... : ")
    deadline = input("Masukkan deadline task : ")

    tasks.append({
        "task": task, 
        "done": False, 
        "priority": False,
        "deadline": deadline
        })
    print("\n")
    print(f"Task '{task}' berhasil ditambahkan!")

def lihat_task():
    if not tasks:
        print("\n")
        print("Tidak ada task.")
        return
    print("\nDaftar Task:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i, task in enumerate(tasks, start=1):
        status = "Selesai ✅" if task["done"] else "Belum Selesai❌"

        priority = "⭐" if task["priority"] else ""

        print(f"{i}. {priority} {task['task']} ({status})")
        print(f"   Deadline: {task['deadline']}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def tandai_selesai():

    lihat_task()
    if not tasks:
        return
    try:
        index = int(input("Masukkan nomor task yang sudah selesai: ")) -1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("\n")
            print("\nTask berhasil ditandai sebagai selesai.")
        else:
            print("Nomor task tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def tandai_prioritas():
    lihat_task()

    if not tasks:
        return

    try:
        index = int(input("Masukkan nomor task prioritas: ")) - 1

        if 0 <= index < len(tasks):

            priority_task = tasks.pop(index)

            priority_task["priority"] = True

            tasks.insert(0, priority_task)

            print("Task berhasil dijadikan prioritas!")

        else:
            print("Nomor task tidak valid.")

    except ValueError:
        print("Input harus berupa angka.")

def hapus_task():
    lihat_task()
    if not tasks:
        return
    try:
        index = int(input("Masukkan nomor task yang ingin dihapus: ")) -1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print("\n")
            print(f"Task terhapus: {removed['task']}")
        else:
            print("Nomor task tidak valid.")
    except ValueError:
        print("Nomor task tidak valid.")

while True:
    tampil_menu() 
    choice = input("Pilih sebuah menu (1-6): ")
    
    if choice == '1' :
        tambah_task()
    elif choice == '2':
        lihat_task()
    elif choice == '3':
        tandai_selesai()
    elif choice == '4':
        tandai_prioritas()
    elif choice == '5':
        hapus_task()
    elif choice == '6':
        print("\nㅠㅠ")
        print("Selamat tinggal!")
        print("\n")
        break
    else:
        print("\n")
        print("Pilihan tidak valid. Coba lagi.")