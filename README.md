## Biodata
Nama: Marsya Nabila Putri

Kelas: TI.24.A.4

NIM: 312410338

![Screenshot 2025-01-05 112905](https://github.com/user-attachments/assets/05ea6a1a-3fc2-42c8-b8b6-a036d978d77b)

Program ini adalah aplikasi sederhana untuk sistem penjualan pancong berbasis terminal. Program ini dibuat dengan pendekatan modular dan menggunakan prinsip OOP (Object-Oriented Programming). Program ini dijalankan untuk menambahkan data jumlah pancong yang terjual, menginput harga pancong, dan menghitung total harga setelah jumlah pancong yang dibeli dan harga pancong dengan input validasi.

```PYTHON
# Program Penjualan Pancong
# Menggunakan Konsep Modular dan OOP

# Modul Data
class PancongData:
    def __init__(self):
        self.sales = []

    def add_sale(self, name, quantity, price):
        self.sales.append({"name": name, "quantity": quantity, "price": price})

    def get_sales(self):
        return self.sales

# Modul View
class PancongView:
    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def input_data(prompt):
        return input(prompt)

    @staticmethod
    def display_table(sales):
        print("\n=== Data Penjualan Pancong ===")
        print(f"{'No':<5}{'Nama Pembeli':<20}{'Jumlah':<10}{'Harga':<10}{'Total':<10}")
        print("-" * 60)
        total_sales = 0
        for idx, sale in enumerate(sales, start=1):
            total = sale['quantity'] * sale['price']
            total_sales += total
            print(f"{idx:<5}{sale['name']:<20}{sale['quantity']:<10}{sale['price']:<10}{total:<10}")
        print("-" * 60)
        print(f"{'':<35}{'Total Penjualan':<15}{total_sales:<10}")

# Modul Proses
class PancongProcess:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def add_sale(self):
        name = self.view.input_data("Masukkan nama pembeli: ")
        while True:
            try:
                quantity = int(self.view.input_data("Masukkan jumlah pancong (harus angka positif): "))
                if quantity <= 0:
                    raise ValueError("Jumlah harus lebih dari 0.")
                break
            except ValueError as e:
                self.view.show_message(f"Input tidak valid: {e}")

        while True:
            try:
                price = int(self.view.input_data("Masukkan harga satuan pancong (harus angka positif): "))
                if price <= 0:
                    raise ValueError("Harga harus lebih dari 0.")
                break
            except ValueError as e:
                self.view.show_message(f"Input tidak valid: {e}")

        self.data.add_sale(name, quantity, price)
        self.view.show_message("Data penjualan berhasil ditambahkan!\n")

    def display_sales(self):
        sales = self.data.get_sales()
        if not sales:
            self.view.show_message("Belum ada data penjualan.")
        else:
            self.view.display_table(sales)

# Main Program
if __name__ == "__main__":
    data = PancongData()
    view = PancongView()
    process = PancongProcess(data, view)

    while True:
        view.show_message("\n=== Program Penjualan Pancong ===")
        view.show_message("1. Tambah Data Penjualan")
        view.show_message("2. Tampilkan Data Penjualan")
        view.show_message("3. Keluar")
        choice = view.input_data("Pilih menu: ")

        if choice == "1":
            process.add_sale()
        elif choice == "2":
            process.display_sales()
        elif choice == "3":
            view.show_message("Terima kasih telah menggunakan program ini.")
            break
        else:
            view.show_message("Pilihan tidak valid, silakan coba lagi.")
```

# Modul Data (PancongData)
Fungsi Utama:
Modul ini bertugas untuk menyimpan dan mengakses data penjualan.

Kode:

```PYTHON
class PancongData:
    def __init__(self):
        self.sales = []  # List untuk menyimpan data penjualan

    def add_sale(self, name, quantity, price):
        self.sales.append({"name": name, "quantity": quantity, "price": price})  # Menambah data penjualan

    def get_sales(self):
        return self.sales  # Mengembalikan data penjualan
````
Penjelasan:

- `self.sales`: Ini adalah list yang berfungsi untuk menyimpan data penjualan. Setiap item dalam list adalah dictionary yang berisi data penjualan, dengan kunci `name`, `quantity`, dan `price`.

- `add_sale`: Metode ini digunakan untuk menambahkan data penjualan ke dalam list sales. Data yang ditambahkan berupa nama pembeli, jumlah barang yang dibeli, dan harga barang per unit.

- `get_sales`: Metode ini digunakan untuk mengambil seluruh data penjualan yang sudah disimpan dalam `sales`.


# Modul View (PancongView)
Fungsi Utama:
Modul ini berfungsi untuk berinteraksi dengan pengguna, seperti menampilkan pesan, mengambil input, dan menampilkan tabel.

Kode:

```PYTHON
class PancongView:
    @staticmethod
    def show_message(message):
        print(message)  # Menampilkan pesan ke konsol

    @staticmethod
    def input_data(prompt):
        return input(prompt)  # Mengambil input dari pengguna

    @staticmethod
    def display_table(sales):
        print("\n=== Data Penjualan Pancong ===")
        print(f"{'No':<5}{'Nama Pembeli':<20}{'Jumlah':<10}{'Harga':<10}{'Total':<10}")
        print("-" * 60)

        total_sales = 0
        for idx, sale in enumerate(sales, start=1):
            total = sale['quantity'] * sale['price']  # Menghitung total harga
            total_sales += total
            print(f"{idx:<5}{sale['name']:<20}{sale['quantity']:<10}{sale['price']:<10}{total:<10}")

        print("-" * 60)
        print(f"{'':<35}{'Total Penjualan':<15}{total_sales:<10}")
````

Penjelasan:

- `show_message`: Metode ini digunakan untuk menampilkan pesan kepada pengguna melalui konsol. Pesan bisa berupa informasi, kesalahan, atau konfirmasi.

- `input_data`: Metode ini mengambil input dari pengguna dengan menampilkan prompt yang ditentukan. Input ini kemudian dikembalikan untuk diproses lebih lanjut.

- `display_table`: Metode ini digunakan untuk menampilkan data penjualan dalam bentuk tabel yang rapi. Setiap penjualan ditampilkan dengan informasi `No`, `Nama Pembeli`, `Jumlah`, `Harga`, dan `Total` (jumlah dikali harga). Di akhir tabel, total penjualan dihitung dan ditampilkan.


# Modul Proses (PancongProcess)
Fungsi Utama:
Modul ini mengatur logika aplikasi, seperti validasi input dan manipulasi data. Modul ini juga menghubungkan modul `PancongData` dan `PancongView`.

Kode:

```PYTHON
class PancongProcess:
    def __init__(self, data, view):
        self.data = data  # Objek dari PancongData
        self.view = view  # Objek dari PancongView

    def add_sale(self):
        name = self.view.input_data("Masukkan nama pembeli: ")  # Input nama pembeli
        while True:
            try:
                quantity = int(self.view.input_data("Masukkan jumlah pancong (harus angka positif): "))
                if quantity <= 0:
                    raise ValueError("Jumlah harus lebih dari 0.")
                break
            except ValueError as e:
                self.view.show_message(f"Input tidak valid: {e}")  # Menampilkan kesalahan

        while True:
            try:
                price = int(self.view.input_data("Masukkan harga satuan pancong (harus angka positif): "))
                if price <= 0:
                    raise ValueError("Harga harus lebih dari 0.")
                break
            except ValueError as e:
                self.view.show_message(f"Input tidak valid: {e}")  # Menampilkan kesalahan

        self.data.add_sale(name, quantity, price)  # Menyimpan data penjualan
        self.view.show_message("Data penjualan berhasil ditambahkan!\n")

    def display_sales(self):
        sales = self.data.get_sales()  # Mengambil data penjualan
        if not sales:
            self.view.show_message("Belum ada data penjualan.")  # Menampilkan pesan jika data kosong
        else:
            self.view.display_table(sales)  # Menampilkan tabel data penjualan
````

Penjelasan:

- `add_sale`:

   - Mengambil nama pembeli, jumlah, dan harga satuan dari input pengguna.
   - Melakukan validasi untuk memastikan bahwa jumlah dan harga yang dimasukkan adalah angka positif. Jika input tidak valid, pesan kesalahan akan ditampilkan, dan pengguna 
     diminta untuk mencoba lagi.
   - Data yang valid kemudian ditambahkan ke `PancongData` menggunakan metode `add_sale` yang ada di modul `PancongData`.

- `display_sales`:

   - Mengambil data penjualan dari `PancongData`.
   - Jika data penjualan kosong, pesan "Belum ada data penjualan" ditampilkan.
   - Jika ada data, data ditampilkan dalam bentuk tabel menggunakan metode `display_table` dari `PancongView`.


# Main Program
ungsi Utama:
Modul ini mengatur alur program dengan menampilkan menu dan menghubungkan modul `PancongData`, `PancongView`, dan `PancongProcess`.

Kode: 

```PYTHON
if __name__ == "__main__":
    data = PancongData()  # Membuat instance data
    view = PancongView()  # Membuat instance view
    process = PancongProcess(data, view)  # Membuat instance proses

    while True:
        view.show_message("\n=== Program Penjualan Pancong ===")
        view.show_message("1. Tambah Data Penjualan")
        view.show_message("2. Tampilkan Data Penjualan")
        view.show_message("3. Keluar")
        choice = view.input_data("Pilih menu: ")

        if choice == "1":
            process.add_sale()  # Menambah data penjualan
        elif choice == "2":
            process.display_sales()  # Menampilkan data penjualan
        elif choice == "3":
            view.show_message("Terima kasih telah menggunakan program ini.")
            break  # Mengakhiri program
        else:
            view.show_message("Pilihan tidak valid, silakan coba lagi.")  # Validasi input menu
````

Penjelasan:

- Program ini memulai dengan membuat instance dari `PancongData`, `PancongView`, dan `PancongProcess`, yang masing-masing bertanggung jawab untuk menyimpan data, berinteraksi dengan pengguna, dan menjalankan logika program.

- Program kemudian menampilkan menu utama yang memungkinkan pengguna untuk memilih:

   1.Menambah data penjualan dengan menggunakan `process.add_sale()`.
  
   2.Menampilkan data penjualan dengan menggunakan `process.display_sales()`.
  
   3.Keluar dari program.

- Jika pilihan tidak valid, pesan kesalahan akan ditampilkan, dan program meminta input lagi dari pengguna.


# Contoh Output Program
Berikut adalah contoh output setelah pengguna berhasil memasukkan data:

![Screenshot 2025-01-06 113616](https://github.com/user-attachments/assets/559ffa15-9f57-4667-a44e-949f807514ba)

![Screenshot 2025-01-06 113656](https://github.com/user-attachments/assets/25824c5a-50fe-40fd-b253-67b1ee4cd00f)





 




