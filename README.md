🚀 Analisis Logika OOP Python (Latihan 1-6)
Dokumentasi ini berisi ringkasan analisis dari implementasi 4 pilar utama Pemrograman Berorientasi Objek (OOP) pada Python.

🟢 1. Dasar Class & Object (Latihan 1 & 2)
Analisis: Class berfungsi sebagai blueprint (cetakan), sedangkan Object adalah hasil cetakannya.

Poin Penting: Penggunaan self sangat krusial agar objek dapat mengenali atributnya sendiri, dan parameter objek (seperti lawan) memungkinkan interaksi data antar-entitas yang berbeda.

🟡 2. Inheritance & Super() (Latihan 3)
Analisis: Memungkinkan Class anak (Child) mewarisi semua sifat Class induk (Parent).

Poin Penting: Fungsi super().__init__() wajib dipanggil agar atribut dari induk tetap terdefinisi tanpa harus menulis ulang kode (efisiensi).

🔴 3. Encapsulation (Latihan 4)
Analisis: Melindungi data sensitif menggunakan akses __ (private).

Poin Penting: Data tidak boleh diakses langsung dari luar. Kita menggunakan Getter untuk mengambil data dan Setter untuk mengubah data dengan validasi (keamanan data).

🔵 4. Abstraction (Latihan 5)
Analisis: Menggunakan modul abc untuk membuat "kontrak" kerja.

Poin Penting: Class abstrak tidak bisa diubah menjadi objek. Ia memaksa setiap class turunan untuk memiliki method tertentu agar struktur program tetap konsisten.

🟣 5. Polymorphism (Latihan 6)
Analisis: Kemampuan satu fungsi untuk memiliki banyak bentuk output.

Poin Penting: Kita bisa menjalankan perintah yang sama (misal: .aksi()) pada berbagai objek yang berbeda, dan hasilnya akan menyesuaikan dengan perilaku unik masing-masing objek tersebut.

🛠️ Kesimpulan Proyek
Implementasi ini membuktikan bahwa OOP membuat kode menjadi:

Modular: Mudah dipecah menjadi bagian kecil.

Scalable: Mudah menambah fitur baru tanpa merusak kode lama.

Secure: Data penting terlindungi dengan enkapsulasi.
