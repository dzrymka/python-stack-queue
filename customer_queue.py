class Transaction:
    def __init__(self, customer_name, transaction_type):
        self.customer_name = customer_name
        self.transaction_type = transaction_type


class TransactionQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, transaction):
        self.queue.append(transaction)
        print(
            f"Transaksi '{transaction.customer_name} - {transaction.transaction_type}' ditambahkan ke dalam antrean.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean transaksi kosong.")
        else:
            removed_transaction = self.queue.pop(0)
            print(
                f"Transaksi '{removed_transaction.customer_name} - {removed_transaction.transaction_type}' telah dilayani.")

    def peek(self):
        if self.is_empty():
            print("Antrean transaksi kosong.")
        else:
            next_transaction = self.queue[0]
            print(
                f"Transaksi berikutnya yang akan dilayani: '{next_transaction.customer_name} - {next_transaction.transaction_type}'.")

    def is_empty(self):
        return len(self.queue) == 0


transaksi_antrean = TransactionQueue()

while True:
    print("\nPilih operasi:")
    print("1. Tambahkan transaksi ke antrean")
    print("2. Hapus transaksi yang telah dilayani")
    print("3. Tampilkan transaksi berikutnya yang akan dilayani")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == '1':
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        jenis_transaksi = input("Masukkan jenis transaksi: ")
        transaction = Transaction(nama_pelanggan, jenis_transaksi)
        transaksi_antrean.enqueue(transaction)
    elif pilihan == '2':
        transaksi_antrean.dequeue()
    elif pilihan == '3':
        transaksi_antrean.peek()
    elif pilihan == '4':
        print("Semua antrean sudah selesai menyelesaikan transaksi.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-4.")
