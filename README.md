------------------------------------------------------------------------------------------------------------------------------------------
                                                             TUGAS 2
------------------------------------------------------------------------------------------------------------------------------------------

1. Tautan menuju aplikasi PWS yang sudah di-deploy
    Link PWS: https://pbp.cs.ui.ac.id/web/project/raysha.reifika/tinychefmart

2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat sebuah proyek Django baru.
        - Membuat folder baru bernama TinyChefMart yang merupakan nama project dan menghubungkannya dengan git.
        - Membuat akun pws dan project baru
        - Membuat dan mengaktifkan virtual environment  
        - Menyiapkan dependencies dengan nama requirements.txt yang nantinya akan di-install. 
        - Membuat sebuah proyek Django baru dengan nama tiny_chef_mart
        - Menambahkan allowed host didalam settings berupa local host, ip, dan url pws
        - Membuat file bernama .gitignore. .gitignore diperlukan untuk menentukan file dan direktori yang harus diabaikan oleh git
        - Melakukan add, commit, push setiap diperlukan perubahan ke git

    - Membuat aplikasi dengan nama main pada proyek tersebut.
        - Membuat aplikasi baru bernama main
        - Menambahkan main ke dalam installed_apps di settings.py
        - Membuat direktori baru bernama templates di dalam direktori main
        - Di dalam templates buat file main.html yang akan berfungsi sebagai templates langsung denagn struktur kode django yang sesuai untuk menampilkan data
    
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        - Buka urls.py pada tiny_chef_mart
        - Tambahkan rute path('', include('main.urls'))
        - '' akan mengarahkan ke file urls.py pada main

    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
        - Membuat class product sebagai model yang akan didefinisikan
        - Di dalam class product, ditambahkan atribut app_name, price, desc, dan quantity dengan tipe data yang sesuai.
        - Model nantinya akan berisi data-data
        - Melakukan migrasi setiap melakukan perubahan pada model agar perubahan model database dapat dilacak

    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        - Mengubah dictionary context pada file views.py di main dengan data yang akan dirender ke html
        
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        - Membuat file urls.py di dalam folder main untuk mengatur rute url

    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        - Melakukan add, commit, push setiap diperlukan perubahan ke git sebelum melakukan deployment
        - Melakukan perintah di project command untuk project baru
        - Melakukan push ke pws master setiap ada perubahan tanpa melakukan perintah di project command

3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    [Client/Browser] 
        |
        | (Request: Mengirim/Mengetik URL)
        v
    [Internet] ------------------> [Web Server] ------------------------------------------> [urls.py]
                                                            (URL Routing)                       |
                                                                                                |
                                                                                                | (Melakukan request)
                                                                                                v
                                                    [Templates Folder]  <--------------------[views.py]
                                                            |                                    ^
                                                (Rendered)  |                                    | (Query Data)
                                                            v                                    v
                                                    [Client/Browser]                       [models.py] <----> [Database]
                                                                                                        
                            
                
    Client melalui browser mengetik sebuah url, dimana url akan mengirimkan request ke web server. Server akan memproses request dan melakukan url routing. dari url akan diekstrak argumen dari request tersebut. Dengan menggunakan database di models dan html template,  client akan menerima informasi kembali sebagai sebuah response

    urls.py:
    - Urls akan mengirim request ke views
    - Django memetakan argumen request atau url ke view
    - Url yang dikirim akan menentukan akan aplikasi yang dijalankan 

    views.py: 
    - Setelah urls dipetakan, views akan mengambil data  dari models dan mengolah data. Kemudian, data akan dikirimkan ke template html untuk dirender

    models.py:
    - Models akan mendefinisikan data dan mengelola interaksi dengan database.

    template html:
    - views akan merender template html dengan data dari models. Kemudian, akan mengirim response kepada client berupa web berdasarkan url yang diakses.

Referensi:
https://scele.cs.ui.ac.id/pluginfile.php/237029/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf

4. Jelaskan fungsi git dalam pengembangan perangkat lunak!
    Git adalah alat software development yang berfungsi sebagai sistem kontrol versi untuk menyimpan, mengatur, dan dokumentasi hasil kerja dalam hal ini adalah kode. Kemudian, git juga dapat men-track perubahan kode yang dilakukan sehingga jika terdapat kesalahan pada kode dapat dilihat dan dibandingkan dengan versi sebelumnya. Git juga dapat membantu dalam kerja tim dengan adanya branching dan merging. Meskipun bekerja sendiri, suatu tim dapat menggambungkan pekerjaannya (merging) dan memastikan setiap bagian tidak ada yang bentrok (branching).

Referensi:
https://dcloud.co.id/blog/apa-itu-git.html#:~:text=Git%20adalah%20alat%20software%20development,code)%20secara%20efisien%20dan%20kolaboratif.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Django terorganisir dengan baik dan mudah untuk  diinstal. Desainer Django membuat kerangka kerja untuk  menerapkan arsitektur web dalam kode.
    - Django bekerja dengan baik dengan data karena memiliki model ORM. 
    - Django memisahkan antar kode dengan konsep MVT atau  Model-View-Template.  Oleh karena konsep tersebut, dapat mempermudah pengelolaan dan pengembangan serta memisahkan logika aplikasi dari tampilan.
    - Hemat biaya karena django adalah proyek Python gratis, tetapi menyediakan banyak komponen bawaan, seperti autentikasi, admin panel, dan ORM. Dengan komponen bawaan ini, pemula dapat lebih mudah memahami.
    - Django merupakan platform yang populer sehingga memiliki banyak dokumentasi.

    Dengan beberapa poin diatas, alasan dari seringnya framework django dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah django mudah dipelajari bagi pemula. 

Referensi:
https://aws.amazon.com/id/what-is/django/
https://cheesecakelabs.com/blog/django-framework-app-development/

6. Mengapa model pada Django disebut sebagai ORM?
    Model dalam konsep MVT django merupakan cara dari suatu data disimpan, diatur, dan dikelola. Model menghubungkan aplikasi dengan database dan membuat interaksi. ORM adalah Object Relational Mapping. Model pada django disebut sebagai ORM karena kerangka kerja django menggunakan lapisan pemetaan objek relasional yang dapat digunakan untuk berinteraksi dengan data. Oleh karena itu, dengan ORM pada django, developer dapat berinteraksi dengan database, seperti memodifikasi database,  menggunakan objek python tanpa menuliskan SQL nya secara manual.

Referensi:
https://www.scaler.com/topics/django/relationships-in-django-models/
https://pbp-fasilkom-ui.github.io/ganjil-2025/docs/tutorial-1


------------------------------------------------------------------------------------------------------------------------------------------
                                                             TUGAS 3
------------------------------------------------------------------------------------------------------------------------------------------

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    - Dengan data delivery, memungkinkan komunikasi yang efisien dan efektif antara client dan server melalui request HTTP.
    - Data delivery memungkinkan client mendapatkan informasi secara real time.
    - Data delivery memastikan layanan yang saling berinteraksi dan berbagi data mendapatkan data yang diperlukan untuk berfungsi dengan baik.
    - Data delivery memastikan sinkronisassi data antar sistem
    - Data delivery mendukung penggunakan API yang memungkinkan integrasi antar sistem

    In conclusion, Data delivery sangat penting untuk pengimplementasian  sebuah platform karena data delivery memastikan platform dapat mengirmkan dan menerima data dengan baik, cepat, dan efisien sehingga memastikan pengalaman client yang optimal.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, JSON lebih baik daripada XML karena JSON memiliki sintaks yang identik dengan kode untuk membuat javascript objects 
    sehingga mudah untuk meng-convert JSON data kedalam native Javascript objects. Kemudian, kode untuk membaca dan menghasilkan JSON data dapat ditulis dalam bahasa pemograman apapun. Selain itu, untuk AJAX Applications, JSON lebih cepat dan lebih mudah dari pada XML. 

    Alasan JSON lebih populer:
    - Sintaksnya JSON yang sederhana dan memiliki struktur yang mirip dengan Javascript. Sedangkan XML menggunakan tag yang lebih kompleks. Oleh karena itu, sintaks JSON lebih efisien dalam penulisan dan pembacaan data serta memudahkan dalam parsing. 
    - Dalam AJAX Applications, pengiriman data lebih cepat saat menggunakan JSON karena tidak diperlukan tag penutup yang berlebihan sehingga ukuran data yang dikirimkan lebih kecil.
    - Struktur data JSON juga lebih sederhana daripada XML karena JSON menggunakan kurung kurawal untuk objek dan kurung siku untuk array 
    sehingga lebih mudah saat bekerja dengan struktur data yang kompleks. Sedangkan, XML menggunakan tag yang lebih rumit untuk dibaca dan diolah.

    In conclusion, JSON lebih populer daripada XML karena lebih sederhana, performanya lebih cepat, lebih mudah untuk digunakan dan diproses.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() memiliki fungsi untuk memeriksa apakah data yang diinput pengguna valid sesuai dengan aturan. Jika sudah valid, data akan disimpan ke dalam database. Namun, jika tidak valid, tidak akan disimpan dalam database dan akan terdapat pesan error.
    Method is_valid() juga dapat membersihkan data input dan menyimpannya ke dalam atribut cleaned_data dengan melakukan seperti ini 
    name = form.cleaned_data['name']

    Mengapa method is_valid() dibutuhkan:
    - Method is_valid() memastikan bahwa hanya data yang sesuai aturan (valid) saja yang diproses/disimpan. Dengan hal ini dapat mencegah data yang salah atau berbahaya masuk ke dalam sistem yang dapat menyebabkan data corrupt dan kesalahan fatal lainnya. Kemudian, method is_valid() dapat memberikan respon ketika terdapat pengguna yang memberikan input yang salah sehingga pengguna dapat mengetahui apa yang harus diperbaiki. 
    
4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    CSRF (Cross-Site Request Forgery) adalah sistem keamanan yang melindungi aplikasi web dari serangan yang dinamakan Cross-Site Request Forgery (CSRF). Saat membuat form django, csrf_token dibutuhkan untuk memastikan setiap dilakukan POST yang dikirim ke server berasal dari sumber resmi. 

    Jika kita tidak menambahkan csrf_token, aplikasi akan sangat rentan terhadap serangan CSRF karena aplikasi tidak dapat membedakan antara permintaan resmi dan permintaan yang dimanipulasi sehingga hacker dapat memanipulasi pengguna untuk melakukan tindakan tidak sah di aplikasi web tanpa sepengetahuan pengguna. Jika serangan tersebut berhasil, hacker dapat mengakses data sensitif, seperti akun bank, dan melakukan tindakan berbahaya lainnya.

    Hacker dapat memanfaatkan hal tersebut dengan membuat web berbahaya yang dapat memberikan request ke aplikasi django yang rentan. Kemudian, ketika pengguna sudah login ke web tersebut, akan terdapat request berbahaya yang dikirimkan ke server tanpa csrf_token. Tanpa csrf_token, server tidak bisa mendeteksi request tersebut resmi atau tidak sehingga server memproses request tersebut.
    
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat input form untuk menambahkan objek model pada app sebelumnya
        - Di dalam main membuat file forms.py untuk menerima input data
        - Membuat base.html didalam folder templates di direktori utama sebagai kerangka umum, lalu ubah settings pada bagian templates dengan menambahkan 'DIRS': [BASE_DIR / 'templates'],
        - Pada folder templates di direktori main, tambahkan block content
        - Pada views.py di main, tambahkan import redirect. Lalu, buat fungsi create_product_entry dengan parameter request untuk dilakukan method is_valid. Kemudian, tambahkan product_entries didalam show_main.
        - Tambahkan path url di urls.py
        - Buat file bernama create_product_entry.html pada direktori main/templates.
        - Didalam main.html, tambahkan kode untuk menampilkan product dan tombol add product entry untuk menerima input data.

    - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
        - Menambahkan id dan primary key didalam file models.py, lalu lakukan migrasi melalui cmd.
        - Pada views.py, tambahkan import HttpResponse dan serializers
        - Membuat fungsi dengan nama show_xml, show_json dengan parameter request.
        - Membuat fungsi dengan nama show_xml_by_id, show_json_by_id dengan parameter request dan id

    - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
        - Pada urls.py, tambahkan import show_xml, show_json dan tambahkan path urlnya sehingga linknya dapat dibuka dengan format xml atau json.
        - Pada urls.py, tambahkan import show_xml_by_id, show_json_by_id dan tambahkan path urlnya sehingga linknya dapat dibuka dengan format xml atau json berdasarkan idnya.

6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

![Screenshot 2024-09-16 191618](https://github.com/user-attachments/assets/0eb78173-1c67-4320-9ecd-d16651b071bf)
![Screenshot 2024-09-16 191640](https://github.com/user-attachments/assets/2a5af1f7-c395-48a4-8159-83528be39d82)
![Screenshot 2024-09-16 191655](https://github.com/user-attachments/assets/754cb741-b318-47aa-a446-a990c61f69ec)
![Screenshot 2024-09-16 191559](https://github.com/user-attachments/assets/b2dae56b-22b4-45d1-9f07-951efd1c566a)



Referensi:
https://scele.cs.ui.ac.id/pluginfile.php/238122/mod_resource/content/1/04%20-%20Data%20Delivery.pdf
https://www.thedevspace.io/community/django-forms
