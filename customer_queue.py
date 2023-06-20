from queue import Queue

transaksi_queue = Queue()

def tambah_transaksi():
    nama = input("Masukkan nama pelanggan: ")
    transaksi = input("Masukkan jenis transaksi: ")
    transaksi_queue.put((nama, transaksi))
    print("Transaksi pelanggan", nama, "telah ditambahkan ke dalam antrian.")

def transaksi_selanjutnya():
    if transaksi_queue.empty():
        print("Tidak ada transaksi dalam antrian.")
    else:
        nama, transaksi = transaksi_queue.queue[0]
        print("Transaksi berikutnya yang akan dilayani:")
        print("Nama pelanggan:", nama)
        print("Jenis transaksi:", transaksi)

def transaksi_selesai():
    if transaksi_queue.empty():
        print("Tidak ada transaksi dalam antrian.")
    else:
        nama, transaksi = transaksi_queue.get()
        print("Transaksi pelanggan", nama, "telah selesai dilayani dan dihapus dari antrian.")

while True:
    print("\nMenu:")
    print("1. Tambahkan transaksi ke dalam antrian")
    print("2. Tampilkan transaksi berikutnya yang akan dilayani")
    print("3. Hapus transaksi yang telah dilayani")
    print("4. Keluar dari program")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    
    if pilihan == '1':
        tambah_transaksi()
    elif pilihan == '2':
        transaksi_selanjutnya()
    elif pilihan == '3':
        transaksi_selesai()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid.")
