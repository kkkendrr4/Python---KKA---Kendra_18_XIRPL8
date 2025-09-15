def main():
    print("=== Program Pembelajaran Dasar Python ===")
    
    # 1. Hello World
    print("Hello, World!")

    # 2. Variabel dan Tipe Data
    nama = "John"
    umur = 25
    tinggi = 5.9
    is_student = True

    print("\nTipe Data Dasar:")
    print("Nama:", nama)
    print("Umur:", umur)
    print("Tinggi:", tinggi)
    print("Apakah mahasiswa?", is_student)

    # 3. Input dari Pengguna
    nama_input = input("\nMasukkan nama Anda: ")
    umur_input = input("Masukkan umur Anda: ")
    print("Halo, " + nama_input + "! Anda berumur " + umur_input + " tahun.")

    # 4. Struktur Kontrol (If-Else)
    umur_input = int(umur_input)
    if umur_input >= 18:
        print("Anda adalah seorang dewasa.")
    else:
        print("Anda masih anak-anak.")

    # 5. Looping (For dan While)
    print("\nMenggunakan loop for:")
    for i in range(5):
        print("Ini adalah iterasi ke-", i)

    print("\nMenggunakan loop while:")
    count = 0
    while count < 5:
        print("Count adalah:", count)
        count += 1

    # 6. Fungsi
    def sapa(nama):
        print("Halo, " + nama + "!")

    sapa("Alice")
    sapa("Bob")

    # 7. List dan Operasi Dasar
    buah = ["apel", "jeruk", "pisang"]
    buah.append("mangga")
    buah.remove("jeruk")

    print("\nDaftar Buah:")
    for item in buah:
        print(item)

    # 8. Dictionary
    mahasiswa = {
        "nama": "Alice",
        "umur": 21,
        "jurusan": "Informatika"
    }

    print("\nInformasi Mahasiswa:")
    print("Nama:", mahasiswa["nama"])
    print("Umur:", mahasiswa["umur"])

    # 9. Penanganan Kesalahan (Exception Handling)
    try:
        angka = int(input("\nMasukkan angka untuk dibagi 10: "))
        hasil = 10 / angka
        print("Hasilnya adalah:", hasil)
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol!")

    # 10. Membaca dan Menulis File
    with open("contoh.html", "w") as file:
        file.write("")

    with open("contoh.txt", "r") as file:
        konten = file.read()
        print("\nIsi file:", konten)

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()