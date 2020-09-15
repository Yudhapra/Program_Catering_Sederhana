#Yudha Prasetyo_Project_UAS

#Judul Program
print("\n================================================")
print("##           Program Sistem Catering          ##")
print("================================================\n")

#Input Data Pelanggan
nama = input("Masukkan Nama Anda\t\t: ")
alamat = str(input("Masukkan Alamat Anda\t\t: "))
no = input("Masukkan Nomer Telp. Anda\t: ")
print("\nMasukkan Tanggal Pesan\nFormat (hari/bulan/tahun)")
tgl = input("Tanggal Pesan\t\t\t: ")
print("\nMasukkan Tanggal Ambil\nFormat (hari/bulan/tahun)")
tgl2 = input("Tanggal Ambil Pesanan\t\t: ")

#Menu
print("\n\t================================")
print("\t|  Pilih Menu Makanan :        |")
print("\t|  1. Rendang      5000/pcs    |")
print("\t|  2. Ayam Bakar   4000/pcs    |")
print("\t|  3. Sayur Asem   7000/pcs    |")
print("\t|  4. Nasi Kuning  8000/pcs    |")
print("\t|  5. Nasi Goreng  12000/pcs   |")
print("\t|  6. Nasi Kucing  6000/pcs    |")
print("\t================================")

#Input Pilihan
pilih = input("\nPilih Menu : ")
print("__________________________________________________\n")

if  str(pilih) == '1':
    r1 = "Rendang"
    R = int(input("Kuantitas yang diinginkan (pcs) : "))
    rh = R * 5000
    print("Rendang","=",rh,"Ribu\n")
    
elif str(pilih) == '2':
    a1 = "Ayam Bakar"
    A = int(input("Kuantitas yang diinginkan (pcs) : "))
    ah = A * 4000
    print("Ayam Bakar","=",ah,"Ribu\n")
    
elif str(pilih) == '3':
    s1 = "Sayur Asem"
    S = int(input("Kuantitas yang diinginkan (pcs) : "))
    sh = S * 7000
    print("Sayur Asem","=",sh,"Ribu\n")

elif str(pilih) == '4':
    k1 = "Nasi Kuning"
    K = int(input("Kuantitas yang diinginkan (pcs) : "))
    kh = K * 8000
    print("Nasi Kuning","=",kh,"Ribu\n")

elif str(pilih) == '5':
    g1 = "Nasi Goreng"
    G = int(input("Kuantitas yang diinginkan (pcs) : "))
    gh = G * 12000
    print("Nasi Goreng","=",gh,"Ribu\n")

elif str(pilih) == '6':
    c1 = "Nasi Kucing"
    C = int(input("Kuantitas yang diinginkan (pcs) : "))
    ch = C * 6000
    print("Nasi Kucing","=",ch,"Ribu\n")

else :
    print("Input Yang Anda Masukan Salah!\nHanya Dapat Memilih Nomer 1 Sampai 5 Saja!")

#Menampilkan Hasil
print("================================================\n")
print("Hasil : ")
print("Pesanan Anda, Atas nama : ", nama, "\nDengan Alamat\t\t: ", alamat, "\nNomer Telp. Anda\t: ", no)
print("Tanggal Pesan\t\t: ", tgl, "\nTanggal Ambil\t\t: ", tgl2)

if  str(pilih) == '1':
    print("Pilihan Anda adalah\t: ",r1, R, "pcs,", "dengan total harga", rh, "Ribu")

elif str(pilih) == '2':
    print("Pilihan Anda adalah\t: ",a1, A, "pcs,", "dengan total harga", ah, "Ribu")

elif str(pilih) == '3':
    print("Pilihan Anda adalah\t: ",s1, S, "pcs,", "dengan total harga", sh, "Ribu")

elif str(pilih) == '4':
    print("Pilihan Anda adalah\t: ",k1, K, "pcs,", "dengan total harga", kh, "Ribu")

elif str(pilih) == '5':
    print("Pilihan Anda adalah\t: ",g1, G, "pcs,", "dengan total harga", gh, "Ribu")

elif str(pilih) == '6':
    print("Pilihan Anda adalah\t: ",c1, C, "pcs,", "dengan total harga", ch, "Ribu")

else :
    print("ZONK!!")
