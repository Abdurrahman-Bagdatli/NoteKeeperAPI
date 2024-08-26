﻿# NoteKeeperAPI
NotesAPI is an API used for adding, retrieving, updating, and deleting notes. It is developed using Flask and uses a MySQL database.
## Kullanılabilir Uç Noktalar

- **POST /addItems**: Yeni bir not ekler.
- **GET /getItems**: Tüm notları alır.
- **PATCH /patchItems**: Var olan bir notu günceller.
- **DELETE /deleteItems**: Bir notu siler.

## Teknolojiler

- **Flask**: API'nin oluşturulmasında kullanılan framework.
- **MySQL**: Not verilerinin saklandığı veritabanı.
- **PyMySQL**: MySQL veritabanına bağlanmak için kullanılan Python kütüphanesi.
- **Flask-CORS**: The modules (origin) of incoming applications and which HTTP methods (PUT, DELETE, GET, etc.) can be used are checked..
