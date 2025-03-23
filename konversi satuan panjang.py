# fungsi untuk konversi satuan panjang
def konversi_satuan_panjang():
    
    # daftar satuan panjang
    satuan = {
        'Kilometer':1000,
        'Hectometer':100,
        'Dekameter':10,
        'Meter':1,
        'Desimeter':0.1,
        'Centimeter':0.01,
        'Milimeter':0.001
    }
    
    # daftar pilihan satuan 
    pilihan_satuan = list(satuan.keys())
    
    # input nama user
    nama = input("Masukkan Nama Anda: ")
    print("|========================================|")
    print(f"|Halo, {nama}! Selamat Datang Di Program|")
    print("|        Koversi Satuan Panjang          |")
    print("|========================================|")
    
    # menampilkan pilihan satuan
    print("Pilih Satuan Awal: ")
    for i, satuan_awal in enumerate(pilihan_satuan):
        print(f"{i+1}. {satuan_awal}")
    
    # input indeks satuan awal
    indeks_awal = int(input("Masukkan Nomor Satuan Awal: ")) -1
    print()
    
    # menampilkan pilihan satuan untuk opsi satuan tujuan
    print("Pilih Satuan Tujuan: ")
    for i, satuan_tujuan in enumerate(pilihan_satuan):
        print(f"{i+1}. {satuan_tujuan}")
    
    # input indeks satuan tujuan
    indeks_tujuan = int(input("Masukkan Nomor Satuan Tujuan: ")) -1
    
    # input nilai yang akan dikonversi
    nilai = float(input("Masukkan Nilai Yang Ingin Dikonversi: "))
    
    # ambil satuan awal dan tujuan berdasarkan indeks
    satuan_awal = pilihan_satuan[indeks_awal]
    satuan_tujuan = pilihan_satuan[indeks_tujuan]
    
    # konversi nilai awal ke meter
    nilai_meter = nilai * satuan[satuan_awal]
    
    # konversi nilai meter ke satuan tujuan
    nilai_tujuan = nilai_meter / satuan[satuan_tujuan]
    
    # hasil konversi
    if nilai_tujuan % 1 == 0:
        # jika hasil konversi adalah bilangan bulat
        print(f"{nama}, {int(nilai)} {satuan_awal} Adalah {int(nilai_tujuan)} {satuan_tujuan}")
    else:
        # jika hasil konversi adalah bilangan desimal
        print(f"{nama}, {nilai} {satuan_awal} Adalah {nilai_tujuan:.2f} {satuan_tujuan}")
    
if __name__ == "__main__":
    konversi_satuan_panjang()