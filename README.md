# Manage.it
> Manage.it is a web application for shops to manage their sellings, records every transaction, look up shop's statistics and many more. This app is built with django

> You can access the app on [https://manage-it.adaptable.app/main/](https://manage-it.adaptable.app/main/)
***
# This is how I make it 👇

## Membuat proyek Django baru
### Step 1: Buat direktori baru dan aktifkan _Virtual environment_
1. Buat direktori baru dengan nama `inventory_management`.
2. Buka direktori pada _command prompt_ kemudian jalankan perintah berikut.
```
python -m venv env
```
3. Aktifkan *Virtual Environment* dengan perintah berikut.
```
env\Scripts\activate.bat
```

### Step 2: _Install_ semua dependencies yang dibutuhkan dan buat proyek Django baru
1. Buat sebuah file bernama `requirements.txt` yang berisi:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
2. _Install_ semua dependencies di dalam _virtual environment_ dengan menjalankan perintah `pip install -r requirements.txt`. 
3. Setelah itu, buat proyek Django baru menggunakan perintah `django-admin startproject inventory-management .`

## Membuat aplikasi dengan nama main.
1. *Di dalam _virtual environment_*, jalankan perintah
`python manage.py startapp main`. Setelah itu, sebuah direktori aplikasi baru bernama `main` akan terbuat di dalam direktori utama.
2. Buka file `settings.py` pada direktori proyek, kemudian tambahkan `main` ke dalam variabel `INSTALLED_APPS` seperti berikut:
```python
INSTALLED_APPS = [
    ...
    'main',
    ...
]
```
3. Setelah itu, aplikasi main sudah berhasil terbuat dan terdaftar ke dalam proyek `inventory_management`.

## Melakukan _routing_ pada proyek.
1. Buka file `urls.py` pada direktori proyek `inventory_management`.
2. Pada variable `urlpatterns`, tambahkan kode berikut.
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    ...,
    path('main/', include('main.urls')),
    ...
]
```

## Membuat model pada aplikasi `main` dengan nama `Item`
1. Buka file `models.py` kemudian buat objek model dengan mendefinisikan atribut-atribut yang ingin kita gunakan seperti sebagai berikut.
```python
from django.db import models

class Item(models.Model):
    name= models.CharField(max_length=256)
    category = models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
```

2. Buat dan aplikasikan migrasi pada model dengan menjalankan perintah berikut.
* Buat migrasi model
```
python manage.py makemigrations
```
> perintah ini berfungsi untuk membuat berkas migrasi yang berisi perubahan pada model yang telah kita buat.

* Aplikasikan migrasi ke basis data.
```
python manage.py migrate
```
> perintah ini berfungsi untuk mengaplikasikan perubahan pada berkas migrasi ke basis data.

Dengan menjalankan langkah-langkah ini, kita telah berhasil membuat model pada aplikasi `main` dengan nama `Item`.

##  Membuat dan menghubungkan fungsi pada `views.py` dengan template.
1. Buat fungsi `show_main` pada `views.py` untuk mengimplementasikan template yang ingin dirender, definisikan juga variabel-variabel yang dibutuhkan di dalam template di dalam variable `context` seperti kode berikut.
```python
from django.shortcuts import render

context = {
    'nama' : 'Fathan Naufal Adhitama',
    'kelas' : 'PBP E'
}

def show_main(request):
    return render(request, "main.html", context)
```

2. Di dalam direktori `main`, buat direktori baru bernama `templates` kemudian buat file `main.html` di dalamnya. Pada file `main.html`, modifikasi tampilan pada template dengan menggunakan variable-variable yang di-_passing_ dari `views`.
```html
<h1>Manage.it</h1>

<h5>Name: </h5>
<p>{{nama}}</p>
<h5>Class: </h5>
<p>{{kelas}}</p>
```

> Dengan melakukan langkah ini, views telah terhubung dengan template dan siap untuk dirender menggunakan fungsi `show_main`.

## Membuat _routing_ pada aplikasi `main`.
1. Buat file dengan nama `urls.py` di dalam direktori `main`.
2. Setelah itu, masukkan kode berikut untuk mengatur views yang diinginkan pada tiap _path_.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Dengan melakukan langkah ini, fungsi `show_main` yang telah dibuat pada `views.py` dapat dipetakan ke URL yang diinginkan.

## Deployment menggunakan Adaptable
Terakhir, dilakukan deployment pada Adaptable dengan langkah-langkah berikut.
1. _Sign in_ ke Adaptable menggunakan akun Github.
2. Buat *New App* kemudian pilih opsi *Connect an existing repository*. Pilih _repository_ `inventory_management`.
3. Pilih *Python App Template* sebagai Deploy Template, dan *PostgreSQL* sebagai Database Type.
4. Ubah `Python Version` sesuai dengan versi Python yang telah terinstall pada _device_.
5. Isi `Start Command` dengan perintah berikut.
```
python manage.py migrate && gunicorn inventory_management.wsgi
```
6. Masukkan nama aplikasi, kemudian centang opsi `HTTP Listener on PORT` dan klik `Deploy App`.

===
## Bagan
![alt text](src/bagan.jpg "Bagan")

===

## Mengapa menggunakan virtual environment?
- **_Virtual environment_** (lingkungan virtual) berfungsi untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya.
- Dengan memisahkan tiap proyek Django di `virtualenv`-nya masing-masing, **package** dan **dependencies** tiap proyek akan terisolasi dan tidak akan terganggu karena mengalami konflik dengan **package** dan **dependencies** dari proyek Django lain.
- Karena sifat terisolasinya tadi, `virtual environment` dapat digunakan untuk membuat environment sendiri untuk tujuan **_testing_** dan **_development_** sehingga perubahan pada satu proyek tidak akan berpengaruh pada proyek lain.
- Selain itu, `virtual environment` juga berguna untuk kepentingan dalam aspek **_Security_**, **_Version Control_**, dan **_Deployment_**.

===

## MVC, MVT, MVVM
**MVC, MVT, dan MVVM** adalah pola arsitektur yang biasa digunakan dalam pengembangan aplikasi berbasis pemrograman untuk menyusun proyek yang terorganisasi dengan baik sehingga mempermudah proses _development_ maupun _maintenance_. Secara garis besar, mereka dapat didefinisikan sebagai berikut:
1. **MVC (Model-View-Controller)**:
- Model: menghubungkan aplikasi dengan basis data dan mengatur interaksi dengan data tersebut.
- View: mengontrol bagaimana data yang dikelola oleh model akan ditampilkan kepada pengguna.
- Controller: menangani dan memproses input user, dan mengkoordinasikan **Model** dan **View**
2. **MVT (Model-View-Template)**:
...MVT adalah salah satu turunan dari struktur MVC (Model-View-Controller), perbedaannya terletak pada:
- Template: memisahkan kode HTML dari logika aplikasi, merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view
3. **MVVM (Model-View-ViewModel)**:
... MVVM juga tidak berbeda jauh dengan pola arsitektur MVC dan MVT, perbedaannya terletak pada fungsinya yang memisahkan antara _business logic_ dan _data presentation logic_ (Views atau UI):
- ViewModel: mengelola presentasi data, logika tampilan, dan user input. Mengubah data dari **Model** menjadi format yang dapat ditampilkan oleh **View**

Sehingga, perbedaan utama dari ketiganya adalah MVC menggunakan Controller untuk _handle_ input user, MVT menggunakan Template untuk merancang kode HTML yang ingin ditampilkan, MVVM menggunakan ViewModel untuk memisahkan _business logic_ dan tampilan/User Interface.