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
            f"Transaksi '{transaction.customer_name} - {transaction.transaction_type}' akan ditambahkan ke dalam antrean.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean transaksi kosong.")
        else:
            removed_transaction = self.queue.pop(0)
            print(
                f"Transaksi '{removed_transaction.customer_name} - {removed_transaction.transaction_type}' sudah dilayani.")

    def peek(self):
        if self.is_empty():
            print("Antrean transaksi kosong.")
        else:
            next_transaction = self.queue[0]
            print(
                f"Transaksi selanjutnya yang akan dilayani: '{next_transaction.customer_name} - {next_transaction.transaction_type}'.")

    def is_empty(self):
        return len(self.queue) == 0


transaction_queue = TransactionQueue()

while True:
    print("\nPilih operasi:")
    print("1. Tambahkan transaksi ke antrean")
    print("2. Hapus transaksi yang sudah dilayani")
    print("3. Tampilkan transaksi berikutnya yang akan dilayani")
    print("4. Keluar")
    choice = input("Masukkan pilihan (1-4): ")

    if choice == '1':
        customer_name = input("Masukkan nama pelanggan: ")
        transaction_type = input("Masukkan jenis transaksi: ")
        transaction = Transaction(customer_name, transaction_type)
        transaction_queue.enqueue(transaction)
    elif choice == '2':
        transaction_queue.dequeue()
    elif choice == '3':
        transaction_queue.peek()
    elif choice == '4':
        print("Already done all the transaction queue.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-4.")
