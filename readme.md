## Deskripsi pipeline yang dibuat

Pipeline yang saya buat ini adalah sebuah pipeline yang ditujukan untuk build dan deploy dari branch tugas-1 kemarin. pipeline ini sudah secara otomatis akan pull dari repositori github OPREC-NCC pada branch tugas-1 untuk dibuild oleh jenkins. 

## Penjelasan integrasi Jenkins dengan SonarQube

Untuk integrasinya, saya menggunakan cara yang sama dengan cara yang diberikan dari github NCC. disini kita menggunakan sebuah plugin jenkins yaitu SonarQube scanner for jenkins, lalu kita setup tokennya sonarqube dan copy dan paste di jenkins agar jenkins bisa berkomunikasi dengan sonarqube kita. 

## Konfigurasi sonarqube

![config sonqube](image.png)


## code analysis dengan sonarqube

![code analysis](image-1.png)
![code analysis 2](image-2.png)

## kendala

- build docker dalam jenkins selalu gagal
- github tidak mau terhubung ke jenkins berkali-kali
- sonarqube scanner tidak bisa jalan
