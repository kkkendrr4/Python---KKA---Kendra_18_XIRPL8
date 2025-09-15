print("  <=============================================>")
print("<==========[ ʕ•ᴥ•ʔ CAFE DUO BEARS ʕ•ᴥ•ʔ ]==========>")
print("  <=============================================>")
print("  ")

menu1 = "Belum Ada"
hargamenu1 = 0

menu2 = "Belum Ada"
hargamenu2 = 0

menu3 = "Belum Ada"
hargamenu3 = 0

menu4 = "Belum Ada"
hargamenu4 = 0


while True:
    print("乂 [ ʕ•ᴥ•ʔ Welcome To Cafe Duo Bears ʕ•ᴥ•ʔ ] 乂")
    print("1. Menu Makanan & Minuman")
    print("2. Pembelian Menu Cafe")
    print("3. Keluar Dari Cafe")
    pilih = int(input("Masukkan Pilihan Anda (1/2/3): "))
    print("乂 <==================================> 乂")

    if pilih == 1:
        namaMenu = input("Masukkan Nama Menu Makanan/Minuman: ")
        harganya = int(input("Masukkan Harga Menu Makanan/Minuman: "))
        menu = namaMenu
        hargamenu = harganya
        print("乂 <==================================> 乂")
        print("List Menu Makanan: ")
        print("1. " + menu + " ..... Rp." + str(hargamenu))
        print("2. " + menu2 + " ..... Rp." + str(hargamenu2))
        print("List Menu Minuman: ")
        print("3. " + menu3 + " ..... Rp." + str(hargamenu3))
        print("4. " + menu4 + " ..... Rp." + str(hargamenu4))
        print("乂 <==================================> 乂")
        
        lanjuttidak = input("Ingin Melanjutkan Mengisi Menu/Tidak (Ya/Tidak): ")
        if lanjuttidak == "Ya" or lanjuttidak == "YA":
            namaMenu2 = input("Masukkan Nama Menu Makanan/Minuman: ")
            harganya2 = int(input("Masukkan Harga Menu Makanan/Minuman: "))
            menu2 = namaMenu2
            hargamenu2 = harganya2
            print("乂 <==================================> 乂")
            print("List Menu Makanan: ")
            print("1. " + menu + " ..... Rp." + str(hargamenu))
            print("2. " + menu2 + " ..... Rp." + str(hargamenu2))
            print("List Menu Minuman: ")
            print("3. " + menu3 + " ..... Rp." + str(hargamenu3))
            print("4. " + menu4 + " ..... Rp." + str(hargamenu4))
            print("乂 <==================================> 乂")
            tanya = input("Ingin Melanjutkan Mengisi Menu/Tidak (Ya/Tidak): ")
            if tanya == "Ya" or tanya == "YA":
                namaMenu3 = input("Masukkan Nama Menu Makanan/Minuman: ")
                harganya3 = int(input("Masukkan Harga Menu Makanan/Minuman: "))
                menu3 = namaMenu3
                hargamenu3 = harganya3
                print("乂 <==================================> 乂")
                print("List Menu Makanan: ")
                print("1. " + menu + " ..... Rp." + str(hargamenu))
                print("2. " + menu2 + " ..... Rp." + str(hargamenu2))
                print("List Menu Minuman: ")
                print("3. " + menu3 + " ..... Rp." + str(hargamenu3))
                print("4. " + menu4 + " ..... Rp." + str(hargamenu4))
                print("乂 <==================================> 乂")
                tanya = input("Ingin Melanjutkan Mengisi Menu/Tidak (Ya/Tidak): ")
                if tanya == "Ya" or tanya == "YA":
                    namaMenu4 = input("Masukkan Nama Menu Makanan/Minuman: ")
                    harganya4 = int(input("Masukkan Harga Menu Makanan/Minuman: "))
                    menu4 = namaMenu4
                    hargamenu4 = harganya4
                    print("乂 <==================================> 乂")
                    print("Selesai Menambahkan 6 Menu Makanan & Minuman")
                    print("\nList Menu Makanan: ")
                    print("1. " + menu + " ..... Rp." + str(hargamenu))
                    print("2. " + menu2 + " ..... Rp." + str(hargamenu2))
                    print("List Menu Minuman: ")
                    print("3. " + menu3 + " ..... Rp." + str(hargamenu3))
                    print("4. " + menu4 + " ..... Rp." + str(hargamenu4))
                    print("乂 <==================================> 乂")
                else:
                    print("Kembali Ke Awal")
                    print("乂 <==================================> 乂")
        else:
            print("Kembali Ke Awal")
            print("乂 <==================================> 乂")

    if pilih == 2:
        print("List Menu Makanan: ")
        print("1. " + menu + " ..... Rp." + str(hargamenu))
        print("2. " + menu2 + " ..... Rp." + str(hargamenu2))
        print("List Menu Minuman: ")
        print("3. " + menu3 + " ..... Rp." + str(hargamenu3))
        print("4. " + menu4 + " ..... Rp." + str(hargamenu4))
        print("乂 <==================================> 乂")
        pilihmana = int(input("Pilih Menu Makanan Dan Minuman: "))
        if pilihmana == 1: #Menu Makanan 1
            harga = hargamenu
            namamakan = menu
            jumlah = int(input("Jumlah " + namamakan + ": "))
            total = jumlah * harga
            pajak = total * 0.11
            hasil = total + pajak
            print("Nama Menu: " + namamakan + "\nHarga Menu: Rp." + str(harga) + "\nPajak: 11%\nHarga Pajak: Rp." + str(pajak) + "\nTotal Harga: Rp." + str(hasil))
            duitnya = int(input("Uang Pembayaran Anda: Rp."))
            if duitnya > hasil:
                print("Kembalian Uang Anda: Rp." + str(duitnya - hasil))
            elif duitnya == hasil:
                print("Uang Pembayaran Anda Cukup, Dan Tidak Ada Kembalian Uang!")
            else:
                print("Uang Pembayaran Anda Tidak Cukup, Silahkan Coba Lagi!")
            print("乂 <==================================> 乂")
        else:
            if pilihmana == 2: #Menu Makanan 2
                harga = hargamenu2
                namamakan = menu2
                jumlah = int(input("Jumlah " + namamakan + ": "))
                total = jumlah * harga
                pajak = total * 0.11
                hasil = total + pajak
                print("Nama Menu: " + namamakan + "\nHarga Menu: Rp." + str(harga) + "\nPajak: 11%\nHarga Pajak: Rp." + str(pajak) + "\nTotal Harga: Rp." + str(hasil))
                duitnya = int(input("Uang Pembayaran Anda: Rp."))
                if duitnya > hasil:
                    print("Kembalian Uang Anda: Rp." + str(duitnya - hasil))
                elif duitnya == hasil:
                    print("Uang Pembayaran Anda Cukup, Dan Tidak Ada Kembalian Uang!")
                else:
                    print("Uang Pembayaran Anda Tidak Cukup, Silahkan Coba Lagi!")
                print("乂 <==================================> 乂")
            else:
                if pilihmana == 3:  #Menu Minuman 3
                    harga = hargamenu3
                    namamakan = menu3
                    jumlah = int(input("Jumlah " + namamakan + ": "))
                    total = jumlah * harga
                    pajak = total * 0.11
                    hasil = total + pajak
                    print("Nama Menu: " + namamakan + "\nHarga Menu: Rp." + str(harga) + "\nPajak: 11%\nHarga Pajak: Rp." + str(pajak) + "\nTotal Harga: Rp." + str(hasil))
                    duitnya = int(input("Uang Pembayaran Anda: Rp."))
                    if duitnya > hasil:
                        print("Kembalian Uang Anda: Rp." + str(duitnya - hasil))
                    elif duitnya == hasil:
                        print("Uang Pembayaran Anda Cukup, Dan Tidak Ada Kembalian Uang!")
                    else:
                        print("Uang Pembayaran Anda Tidak Cukup, Silahkan Coba Lagi!")
                    print("乂 <==================================> 乂")
                else:
                    if pilihmana == 4:  #Menu Minuman 4
                        harga = hargamenu4
                        namamakan = menu4
                        jumlah = int(input("Jumlah " + namamakan + ": "))
                        total = jumlah * harga
                        pajak = total * 0.11
                        hasil = total + pajak
                        print("Nama Menu: " + namamakan + "\nHarga Menu: Rp." + str(harga) + "\nPajak: 11%\nHarga Pajak: Rp." + str(pajak) + "\nTotal Harga: Rp." + str(hasil))
                        duitnya = int(input("Uang Pembayaran Anda: Rp."))
                        if duitnya > hasil:
                            print("Kembalian Uang Anda: Rp." + str(duitnya - hasil))
                        elif duitnya == hasil:
                            print("Uang Pembayaran Anda Cukup, Dan Tidak Ada Kembalian Uang!")
                        else:
                            print("Uang Pembayaran Anda Tidak Cukup, Silahkan Coba Lagi!")
                        print("乂 <==================================> 乂")
                    else:
                        print("乂 <== Pilihan Menu Tidak Ada ==> 乂\n")
    else:
        if pilih == 3:
            print("Anda Keluar Dari Cafe Duo Bears, Terima Kasih Telah Berkunjung!")
            print("<===============[ ʕ•ᴥ•ʔ CAFE DUO BEARS ʕ•ᴥ•ʔ ]===============>")
            break
        else:
            if pilih > 3:
                print("乂 <= Pemilihan Tidak Ada, Silahkan Coba Lagi! => 乂")
       
                
