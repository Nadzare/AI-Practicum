#Library (random dan datetime)
import random
import datetime

#Struktur kontrol: Fungsi untuk menampilkan daftar film
def tampilkan_film():
    print("Daftar Film yang Tersedia:")
    for i, film in enumerate(films, 1):
        print(f"{i}. {film} - Harga: Rp{films[film]}")

#Struktur kontrol: Fungsi untuk memesan tiket
def pesan_tiket():
    tampilkan_film()
    pilihan = int(input("Pilih nomor film: "))
    if pilihan < 1 or pilihan > len(films):
        print("Pilihan tidak valid!")
        return
    
    film_terpilih = list(films.keys())[pilihan - 1]
    harga_tiket = films[film_terpilih]
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))
    
    kursi_terpilih = [] 
    for _ in range(jumlah_tiket):  
        kursi = random.randint(1, 50)  
        kursi_terpilih.append(kursi)
    
    total_harga = harga_tiket * jumlah_tiket
    waktu_pemesanan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
    print("\n--- Detail Pemesanan ---")
    print(f"Film        : {film_terpilih}")
    print(f"Jumlah Tiket: {jumlah_tiket}")
    print(f"Nomor Kursi : {kursi_terpilih}")
    print(f"Total Harga : Rp{total_harga}")
    print(f"Waktu Pesan : {waktu_pemesanan}")
    print("Tiket berhasil dipesan!\n")

#Struktur data: Dictionary untuk menyimpan daftar film dan harga tiket
films = {
    "KKN di Desa Penari": 45000,
    "Sewu Dino": 50000,
    "Pengabdi Setan 2: Communion": 48000,
    "Mencuri Raden Saleh": 47000
}

#Struktur kontrol: Perulangan utama program
while True:
    print("\nSistem Pemesanan Tiket Bioskop")
    print("1. Lihat daftar film")
    print("2. Pesan tiket")
    print("3. Keluar")
    
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        tampilkan_film()
    elif pilihan == "2":
        pesan_tiket()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan layanan kami!")
        break
    else:
        print("Pilihan tidak valid, coba lagi!")
