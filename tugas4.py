# 1. List – akses & manipulasi
print("\n -List akses & manipulasi-")

data_kucing =["Asep", 6, 3.5, "Abu-putih", 2020, "Domestik", "Male"]

# elemen pertama & terakhir
print("Elemen Pertama:", data_kucing[0])
print("Elemen Terakhir:", data_kucing[-1])

# slicing [ start:stop:step]
print("-SLICING-")
print("hasil slicing:", data_kucing[0:7:2])

# Append
print("-APPEND-")
print("data sebelum ditambahkan:", data_kucing)
data_kucing.append("Sukak Ikan")
print("data setelah ditambahkan:", data_kucing)

# Insert
print("-INSERT-")
print("Data sebelum di Insert:", data_kucing)
data_kucing.insert(7, "Ngeyel Banget")
print("Data setelah di Insert:", data_kucing)

# Extend
print("-EXTEND-")
print("data sebelum di extend:", data_kucing)
data_kucing.extend(["Ganteng", 2026])
print("data setelah di extend:", data_kucing)

# POP
print("-POP-")
print("data sebelum di pop:", data_kucing)
data_kucing.pop(2)
print("data setelah di pop:", data_kucing)

# REMOVE
print("-REMOVE-")
print("data sebelum di remove:", data_kucing)
data_kucing.remove(2020)
print("data setelah di remove:", data_kucing)

# 2. Tuple – immutability & unpacking
print("\n -TUPLE-")
nama_kucing =("Winter", "Spring", "Summer","Autumn", "Asep")
warna_kucing =("Abu-Putih", "Orange", "Krem muda", "Krem", "Orange-putih")

print("-Tampilkan panjang dan Akses indeks-")
print(len(nama_kucing))
print("indeks Ke-4:", nama_kucing[4])
print(nama_kucing[4] + " berwarna " + warna_kucing[0])

# Unpacking
nama_kucing1, nama_kucing2, nama_kucing3, *rest= nama_kucing
print("-UNPACKING-")
print("Nama Kucing 1:", nama_kucing1)
print("Nama Kucing 2:", nama_kucing2)
print("Nama Kucing 3:", nama_kucing3)
print("Sisa Nama Kucing:", rest)

# 3. Set – keunikan & operasi himpunan
print("\n -Set(keunikan & operasi himpunan)-")

set_kucing1 = {"Asep", "Autumn", "Summer", "Spring", "Winter"}
set_kucing2 = {"Winter", "Asep", "Cutie", "Milo", "Pusy"}

print("Set Kucing 1:", set_kucing1)
print("Set Kucing 2:", set_kucing2)

print("Hasil Union:", set_kucing1 | set_kucing2)
print("Hasil Intersection:", set_kucing1 & set_kucing2)
print("Hasil Difference:", set_kucing1 - set_kucing2)
print("Hasil Symmetric Difference:", set_kucing1 ^ set_kucing2)

#4. Dictionary – key/value dasar
print("\n -Dictionary(key/value dasar)-")
mahasiswa = {
    "Nama": "Khanara",
    "NIM": "2211021",
    "Kota": "Batam",
    "Angkatan":2022}

print("data awal:", mahasiswa)
## Tambah key baru
print("\nsebelum nambah key:", mahasiswa) 
mahasiswa["Jurusan"] = "Sistem Informasi"
print("\nsesudah nambah key:", mahasiswa)

# Ubah nilai key
print("\n sebelum ubah nilai:", mahasiswa)
mahasiswa["Kota"] = "London"
print("\nsesudah ubah nilai:", mahasiswa)

# Hapus key
print("\n sebelum dihapus:", mahasiswa)
del mahasiswa ["Angkatan"]
print("\nsesudah dihapus:", mahasiswa)

# Menampilkan keys, values, dan items
print("keys:", mahasiswa.keys())
print("values:", mahasiswa.values())
print("items:", mahasiswa.items())

# Iterasi key:value
print("\n data mahasiswa:")
for key, value in mahasiswa.items():
    print(key, ":", value)


# 5. Nested Structures
print("\n -Nested Structures-")

daftar_buku = [
    {"judul": "Filosofi Teras", "penulis": "Henry Manampiring", "tahun": 2018},
    {"judul": "Hujan", "penulis": "Tere Liye", "tahun": 2016},
    {"judul": "Laut Bercerita", "penulis": "Leila S. Chudori", "tahun": 2017},
    {"judul": "Tentang Kamu", "penulis": "Tere Liye", "tahun": 2016}
]

print("Semua Judul Buku:")
for buku in daftar_buku:
    print(buku["judul"])

buku_terbaru = [buku for buku in daftar_buku if buku["tahun"] >= 2017]

print("\nBuku Tahun 2017 ke Atas:")
for buku in buku_terbaru:
    print(buku["judul"])

# 6. Comprehension & utilitas
print("\n -Comprehension & utilitas")
# List comprehension
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x ** 2 for x in angka]

print("-List comprehension")
print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

# Dict comprehension
status_angka = {
    x: "genap" if x % 2 == 0 else "ganjil"
    for x in range(1, 11)
}
print("-Dict comprehension")
print("Status angka:", status_angka)

#Set comprehension
kalimat = "Belajar Python"
huruf_unik = {
    huruf.lower()
    for huruf in kalimat
    if huruf != " "
}
print("-Set comprehension-")
print("Huruf unik:", huruf_unik)

# 7. Keanggotaan & Pencarian Sederhana
print("\n -Keanggotaan & Pencarian Sederhana-")
nama_kucing = ["Asep", "Winter", "Spring", "Summer", "Autumn"]
set_kucing = {"Asep", "Winter", "Spring", "Summer"}

# Cek keanggotaan pada list
print("-Cek keanggotaan pada list")

if "Asep" in nama_kucing:
    print("Asep ada di dalam list")
else:
    print("Asep tidak ada di dalam list")

# Cek keanggotaan pada set
if "Cutie" in set_kucing:
    print("Cutie ada di dalam set")
else:
    print("Cutie tidak ada di dalam set")

# Cari posisi item pada list
if "Spring" in nama_kucing:
    print("Spring ada di index:", nama_kucing.index("Spring"))
else:
    print("Spring tidak ditemukan")