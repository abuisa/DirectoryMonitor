# TOOL UNTUK DIRECTORY MONITOR 


Directory atau Folder Monitor adalah tool yang bagus untuk melakukan pengawasan atau memonitor direktori

## Penelitian Malware 
Latar belakang tool ini adalah, pada awalnya saya butuk tool untuk melakukan penelitian malware, saya membutuhkan sebuah tool yang dapat 
merekam apa yang terjadi terhadap file ataupun direktori dan menampilkannya dalam bentuk baris record yang bisa saya format sendiri outputnya,
setelah kesa-kesini mencari akhirnya dapat juga dan jadilah tool ini.

## windows 
Untuk yang --> /windows/watchdog.py untuk melakukan monitor action terhadap file di sistem operasi windows,
telah dilakukan ujicoba pada windows 10
### kekurangannya 
kekurangan watchdog.py adalah tidak bisa menghandel action atau kejadian ketika file diakses atau file di buka,
hanya menghandel action atau kejadian ketika file diubah, dihapus, direname, dan perubahan size. 

## linux
Untuk yang --> /linux/dir-monitor-all-even.py untuk melakukan monitor action terhadap file di sistem operasi Linux,
telah dilakukan ujicoba pada Linux Lubuntu base on ubuntu 16.04.
### kekurangan
kekurangan dir-monitor-all-even.py adalah action yang diberikan terlalu "rame" atau terlalu banyak sehingga ketika satu file 
diakses maka akan menampilkan even action close_write, access, dan open sehingga terasa sangat "rame" di raportnya.