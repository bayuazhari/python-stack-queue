class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

book_stack = Stack()

def menu():
    print("Pilihan Menu:\n1. Tambah Buku\n2. Hapus Buku Terakhir\n3. Tampilkan Buku Teratas\n4. Keluar")

def tambah_buku():
    judul_buku = input("Masukkan judul buku: ")
    pengarang = input("Masukkan nama pengarang: ")
    book_stack.push((judul_buku, pengarang))
    print("Buku berhasil ditambahkan ke dalam tumpukan.")

def hapus_buku():
    if book_stack.is_empty():
        print("Tumpukan buku kosong.")
    else:
        book_stack.pop()
        print("Buku terakhir berhasil dihapus dari tumpukan.")

def tampilkan_buku():
    if book_stack.is_empty():
        print("Tumpukan buku kosong.")
    else:
        print("Buku teratas di tumpukan: ", book_stack.peek())

while True:
    menu()
    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 1:
        tambah_buku()
    elif pilihan == 2:
        hapus_buku()
    elif pilihan == 3:
        tampilkan_buku()
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")
