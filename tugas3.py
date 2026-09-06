# Tugas Python Programming: Python Basics

#1. Deklarasi Variabel dan Tipe Data
nama_depan = "Khairunisa "
nama_belakang = "Nada"
umur = 21
tinggi_badan = 145.5
status_mahasiswa = True
hal_yang_disukai = ["Mendengarkan lagu", "Menonton film", "Jajan apapun", "Punya banyak uang", "Asep kucingku"]

print("-Deklarasi Variabel dan Tipe Data-")
print("nama lengkap:", nama_depan + " " + nama_belakang)
print("umur:", umur)
print("tinggi badan:", tinggi_badan)
print("status_mahasiswa:", status_mahasiswa)
print("hal_yang_disukai:", hal_yang_disukai)

#2. Manipulasi String
nama_depan = "Na"
nama_belakang = "Jaemin"
nama_lengkap = nama_depan + " " + nama_belakang
print ("-Manipulasi String-")
print(nama_lengkap)
print(len(nama_lengkap))
print(nama_lengkap.upper())
print(nama_lengkap.lower())

cat = "asep ganteng pake banget"
print (cat.split(" "))
print (cat.title())
print (cat.replace ("a", "i"))

#3. Operasi Matematika Sederhana
print("- Operasi Aritmatika-")
# - Penjumlahan
a = 20
b = 10
print("Penjumlahan")
print("20 + 10 =" + str(a + b))

# - Pengurangan
a = 15
b = 5
print("Pengurangan")
print("15 - 5 =" + str(a - b))

# - Perkalian
a = 11
b = 2
print("Perkalian")
print("11 * 2 =" + str(a * b))

# - Pembagian
a = 100
b = 10
print("Pembagian")
print("100 / 10 =" + str(a / b))

# - Pembagian Bulat
a = 15
b = 2
print("Pembagian Bulat")
print("15 // 2 =" + str(a // b))

# - Modulus (sisa bagi)
a = 15
b = 4
print("Modulus(sisa bagi)")
print("15 % 4 =" + str(a % b))

#4. List dan Akses Elemen
nama_kucing = ["Asep", "Winter", "Spring", "Summer", "Autumn"]
print("Tampilkan Elemen")
print("nama kucing:", nama_kucing)
print(nama_kucing[0])
print(nama_kucing[4])

# Append
print("append")
print("nama kucing sebelum ditambahkan:", nama_kucing)
nama_kucing.append("Cutie")
print("nama kucing setelah ditambahkan:", nama_kucing)

# Remove
print("remove")
print("nama kucing sebelum dihapus:", nama_kucing)
nama_kucing.remove("Winter")
print("nama kucing setelah dihapus:", nama_kucing)

# Pop
print("pop")
print("nama kucing sebelum di pop:", nama_kucing)
nama_kucing.pop(2)
print("nama kucing setelah di pop:", nama_kucing)

# 5. Penggunaan Input dari User
print("Perkenalan")
nama = input("Masukkan Nama Kamu: ")
umur = input("Masukkan Umur Kamu: ")
print(f"Halo semuanya, Perkenalkan nama saya {nama} dan umur saya {umur} tahun")









      