stack = []


def tambah_buku(stack, buku_baru):
    stack.append(buku_baru)
    print(f" {buku_baru} berhasil ditambahkan ke dalam stack.")


def hapus_buku_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat dihapus.")
    else:
        buku_terakhir = stack.pop()
        print(f" {buku_terakhir} berhasil dihapus dari stack.")


def tambah_pengarang(stack, pengarang_baru):
    stack.append(pengarang_baru)
    print(f" {pengarang_baru} berhasil ditambahkan ke dalam stack.")


def hapus_pengarang_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada pengarang yang dapat dihapus.")
    else:
        pengarang_terakhir = stack.pop()
        print(f" {pengarang_terakhir} berhasil dihapus dari stack.")


def tampilkan_barang_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang dapat ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {barang_teratas}.")


while True:
    print("\nToko buku saat ini:", stack)
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tambah Pengarang")
    print("4. Hapus Pengarang Terakhir")
    print("5. Tampilkan Barang Teratas")
    print("6. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4/5/6): ")

    if pilihan == "1":
        buku_baru = input("Masukkan nama buku yang akan ditambahkan: ")
        tambah_buku(stack, buku_baru)
    elif pilihan == "2":
        hapus_buku_terakhir(stack)
    elif pilihan == "3":
        pengarang_baru = input(
            "Masukkan nama pengarang yang akan ditambahkan: ")
        tambah_pengarang(stack, pengarang_baru)
    elif pilihan == "4":
        hapus_pengarang_terakhir(stack)
    elif pilihan == "5":
        tampilkan_barang_teratas(stack)
    elif pilihan == "6":
        print("Terima kasih sudah lihat lihat barang disini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
