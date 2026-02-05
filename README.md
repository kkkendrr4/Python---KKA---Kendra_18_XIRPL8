Analisis Latihan 1: Dasar Class & Objek
Tugas: Apa yang terjadi jika kamu mengubah hero1.hp = 500 setelah objek dibuat? 
Analisis: Secara teknis, Python akan mengizinkan perubahan tersebut dan nilai hp pada objek hero1 akan berubah menjadi 500. Hal ini membuktikan bahwa secara default, atribut dalam Python bersifat Public, artinya siapa saja bisa mengubah data tersebut dari luar class tanpa melalui aturan tertentu.

Analisis Latihan 2: Interaksi Antar Objek
Tugas: Mengapa parameter lawan pada method serang harus menerima objek utuh, bukan hanya string nama? 
Analisis: Ini sangat penting karena dengan menerima objek utuh, kita bisa mengakses semua atribut dan method milik objek tersebut, seperti memanggil lawan.diserang() untuk mengurangi HP-nya. Jika hanya mengirim string nama, kita tidak bisa memanipulasi data internal (seperti nyawa) milik karakter lawan tersebut.

Analisis Latihan 3: Eksperimen super()
Tugas: Apa yang terjadi jika baris super().__init__(...) dihapus atau dijadikan komentar? 
Analisis: Error yang muncul: Akan muncul AttributeError: 'Mage' object has no attribute 'name' saat mencoba memanggil eudora.info().
Penyebab: Tanpa super(), constructor milik Parent Class (Hero) tidak pernah dijalankan, sehingga atribut name, hp, dan attack_power tidak pernah dibuat untuk objek Mage.
Peran super(): Berfungsi sebagai "penghubung" yang memastikan atribut dasar dari class induk tetap terisi meskipun kita membuat class anak yang baru.

Analisis Latihan 4: Enkapsulasi & Keamanan Data
Tugas 1 (Hacking): Apakah hero1._Hero__hp bisa diakses? 
Analisis: Ya, nilai HP tetap muncul. Ini disebut Name Mangling. Python tidak benar-benar mengunci data secara total, namun mengubah namanya agar sulit diakses secara tidak sengaja. Dalam standar profesional, kita tetap dilarang mengaksesnya secara langsung demi menjaga integritas data.
Tugas 2 (Uji Validasi): Apa gunanya method Setter? 
Analisis: Jika logika validasi dihapus, data HP bisa diisi angka negatif (misal -100) yang tidak masuk akal dalam game. Setter berfungsi sebagai "satpam" yang memastikan data yang masuk selalu valid dan aman sebelum benar-benar disimpan ke memori.

Analisis Latihan 5: Abstraction & Interface
Tugas 1 (Melanggar Kontrak): Apa arti error Can't instantiate abstract class Hero? 
Analisis: Error ini muncul karena Hero berjanji mengikuti kontrak GameUnit namun tidak membuat method serang. Konsekuensinya, class tersebut tidak akan pernah bisa digunakan untuk membuat objek nyata sampai semua "janji" (abstract method) dipenuhi.
Tugas 2 (Mencetak Cetakan): Mengapa GameUnit dilarang menjadi objek? 
Analisis: Karena GameUnit adalah blueprint murni yang hanya berisi konsep abstrak. Gunanya adalah sebagai standar atau "cetakan induk" agar semua karakter (Hero/Monster) memiliki struktur yang seragam dan konsisten.

Analisis Latihan 6: Polimorfisme & Fleksibilitas
Tugas 1 (Skalabilitas): Apa keuntungan Polimorfisme saat menambah karakter baru seperti Healer? 
Analisis: Keuntungannya adalah kita tidak perlu mengubah kode di program utama (seperti bagian perulangan for). Selama class baru memiliki method bernama serang, sistem akan otomatis mengenalinya. Ini membuat kode sangat fleksibel dan mudah diperbarui di masa depan.
Tugas 2 (Konsistensi): Mengapa nama method harus persis sama? 
Analisis: Jika namanya berbeda (misal tembak_panah), loop polimorfisme akan gagal dan menyebabkan error karena ia mencari method bernama serang. Polimorfisme bergantung pada kesamaan antarmuka untuk menjalankan perintah yang berbeda-beda.
