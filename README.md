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
