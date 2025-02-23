
class PancongData:
    def __init__(self):
        self.sales = []  

    def add_sale(self, name, quantity, price):
        self.sales.append({"name": name, "quantity": quantity, "price": price})  

    def get_sales(self):
        return self.sales  

    def remove_sale(self, index):
        if 0 <= index < len(self.sales):
            del self.sales[index]  
            return True
        return False



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

    def delete_sale(self):
        sales = self.data.get_sales()
        if not sales:
            self.view.show_message("Belum ada data penjualan untuk dihapus.")
            return

        self.view.display_table(sales)
        while True:
            try:
                index = int(self.view.input_data("Masukkan nomor data yang ingin dihapus: ")) - 1
                if self.data.remove_sale(index):
                    self.view.show_message("Data berhasil dihapus.")
                    break
                else:
                    raise ValueError("Nomor data tidak valid.")
            except ValueError as e:
                self.view.show_message(f"Input tidak valid: {e}")



if __name__ == "__main__":
    data = PancongData()  
    view = PancongView()  
    process = PancongProcess(data, view)  

    while True:
        view.show_message("\n=== Program Penjualan Pancong ===")
        view.show_message("1. Tambah Data Penjualan")
        view.show_message("2. Tampilkan Data Penjualan")
        view.show_message("3. Hapus Data Penjualan")
        view.show_message("4. Keluar")
        choice = view.input_data("Pilih menu: ")

        if choice == "1":
            process.add_sale()  
        elif choice == "2":
            process.display_sales()  
        elif choice == "3":
            process.delete_sale()  
        elif choice == "4":
            view.show_message("Terima kasih telah menggunakan program ini.")
            break  
        else:
            view.show_message("Pilihan tidak valid, silakan coba lagi.") 
