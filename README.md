
# Öğrenci Veritabanı Yönetim Sistemi

Bu proje, Öğrenci Not Takip Sistemi'nin geliştirilmesi amacıyla hazırlanmıştır. Projede, Django framework'ü kullanılmış ve veritabanı yönetimi için SQLite tercih edilmiştir. Projenin temel amacı, öğrenci notlarının yüklenmesi, listelenmesi ve güncellenmesini sağlamaktır.

## Proje Gereksinimleri

- **Python 3.x**
- **Django 3.x veya özeri**
- **SQLite** (Django ile varsayılan olarak gelir)
- **pip** (Python paket yöneticisi)

## Proje Klonlama ve Kurulum

Projeyi GitHub'dan klonlamak ve gerekli ayarları yapmak için aşağıdaki adımları izleyin:

### 1. Projeyi Klonlama

```bash
git clone https://github.com/kullaniciadi/student_management.git
cd student_management
```

### 2. Sanal Ortam Oluşturma ve Bağlantı

Python sanal ortamı oluşturup etkinleştirin:

```bash
python -m venv venv
source venv/bin/activate # Windows için: venv\Scripts\activate
```

### 3. Gereksinimlerin Yüklenmesi

Projeye ait gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

### 4. Veritabanı Migrasyonlarını Uygulama

Veritabanı yapılandırmalarını uygulamak için:

```bash
python manage.py migrate
```

### 5. Verilerin Yüklenmesi

Öğrenci verilerini veritabanına yüklemek için:

```bash
python manage.py shell
>>> from load_students import load_students
>>> load_students()
```

## Projenin Çalıştırılması

Projenin geliştirme sunucusunu başlatmak için:

```bash
python manage.py runserver
```

Tarayıcınızda [http://127.0.0.1:8000/](http://127.0.0.1:8000/)admin adresine giderek projeyi görebilirsiniz.

## Proje Yapısı

- **student\_management**: Ana proje dizini.
  - **settings.py**: Proje ayarları.
  - **urls.py**: URL tanımlamaları.
  - **load\_students.py**: Veritabanına öğrenci veri yükleme scripti.
- **students**: Uygulama dizini.
  - **models.py**: Veritabanı modelleri.
  - **views.py**: Uygulama için görünüm fonksiyonları.
  - **templates/students/student\_list.html**: Öğrenci listesi için HTML şablonu.

## Proje Kullanımı

Projeyi başlattıktan sonra, ana sayfada yüklenen öğrencilerin listesini görebilirsiniz. Veritabanına yeni öğrenci ekleyebilir, mevcut öğrenci bilgilerini güncelleyebilirsiniz.



- **Django**: Django yapılandırmaları ve komutları için destek.
- **SQLite**: Veritabanı dosyasını incelemek ve sorguları çalıştırmak için kullanılabilir.



