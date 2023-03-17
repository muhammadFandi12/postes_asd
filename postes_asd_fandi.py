#nama : muhammad fandi perdana

from prettytable import PrettyTable


class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.next = None


class MahasiswaLinkedList:
    def __init__(self):
        self.head = None

    def tambah_mahasiswa(self, nim, nama, jurusan):
        new_mahasiswa = Mahasiswa(nim, nama, jurusan)

        if not self.head:
            self.head = new_mahasiswa
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_mahasiswa


    def tampilkan_mahasiswa(self):
        if not self.head:
            print("Tidak ada mahasiswa yang terdaftar.")
        else:
            current = self.head
            table = PrettyTable(["NIM", "Nama", "Jurusan"])
            while current:
                table.add_row([current.nim, current.nama, current.jurusan])
                current = current.next
            print(table)

    def cari_mahasiswa(self, nim):
        current = self.head
        while current is not None:
            if current.nim == nim:
                return current
            current = current.next
        return None



    def update_mahasiswa(self, nim, nama, jurusan):
        mahasiswa = my_list.cari_mahasiswa(nim)
        if mahasiswa:
            mahasiswa.nim = nim
            mahasiswa.nama = nama
            mahasiswa.jurusan = jurusan
            print("Data mahasiswa berhasil diupdate!")
        else:
            print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

    def hapus_mahasiswa(self, nim):
        current = self.head
        if current and current.nim == nim:
            self.head = current.next
            current = None
            print("Mahasiswa berhasil dihapus")
            return
        prev = None
        while current and current.nim != nim:
            prev = current
            current = current.next
        if current is None:
            print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
            return
        prev.next = current.next
        current = None
        print("Mahasiswa berhasil dihapus!")



def tampilan_menu():
    print("""
    |========================================|
    |------------DATA MAHASISWA--------------|
    |========================================|
    |1. Tambah Data Mahasiswa                |
    |2. Tampilkan Data Mahasiswa             |
    |3. Cari Data Mahasiswa                  |
    |4. Update Data Mahasiswa                |
    |5. Hapus Data Mahasiswa                 |
    |6. Keluar                               |
    |========================================|""")


tampilan_menu()
my_list = MahasiswaLinkedList()

while True:
    pilih = input("Masukan pilihan anda: ")

    if pilih == "1":
        nim = input("Masukan NIM          : ")
        nama = input("Masukan Nama         : ")
        jurusan = input("Masukan Nama Jurusan : ")
        my_list.tambah_mahasiswa(nim, nama, jurusan)
        print("Data mahasiswa berhasil ditambahkan!")
    
    elif pilih == "2":
        my_list.tampilkan_mahasiswa()

    elif pilih == "3":
        nim = input("Masukan NIM yang ingin dicari: ")
        mahasiswa = my_list.cari_mahasiswa(nim)
        if mahasiswa:
            print(f"mahasiswa dengan NIM {nim} ditemukan")
            print(f"NIM : {mahasiswa.nim}")
            print(f"Nama : {mahasiswa.nama}")
            print(f"Jurusan : {mahasiswa.jurusan}")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    elif pilih == "4":
        my_list.tampilkan_mahasiswa()
        nim = input("Masukan NIM mahasiswa yang ingin diupdate: ")
        mahasiswa = my_list.cari_mahasiswa(nim)
        if mahasiswa:
            nim_baru = input("Masukan NIM baru: ")
            nama_baru = input("Masukan Nama baru: ")
            jurusan_baru = input("Masukan Jurusan baru: ")
            mahasiswa.nim = nim_baru
            mahasiswa.nama = nama_baru
            mahasiswa.jurusan = jurusan_baru
            my_list.update_mahasiswa(nim_baru, nama_baru, jurusan_baru)
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")



    elif pilih == "5":
        my_list.tampilkan_mahasiswa()
        nim = input("Masukan NIM mahasiswa yang ingin dihapus: ")
        mahasiswa = my_list.cari_mahasiswa(nim)
        if mahasiswa:
            my_list.hapus_mahasiswa(nim)
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    elif pilih == "6":
        exit()




