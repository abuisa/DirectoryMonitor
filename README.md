# TOOL UNTUK DIRECTORY MONITOR 
Directory atau Folder Monitor adalah tool yang bagus untuk melakukan pengawasan atau memonitor perubahan yang terjadi pada file dan direktori dan support sub-direktori

## The License
This Script license is full freeee.. :).

## TEST
* linux/dir-monitor-all-even.py : Suksess di test di sistem operasi Linux Lubuntu base on ubuntu 16.04
* windows/watchdog.py : Suksess di test di sistem operasi Windows 10 64 bit

## Penelitian Malware 
Latar belakang tool ini adalah, pada awalnya saya butuh tool untuk melakukan penelitian malware, saya membutuhkan sebuah tool yang dapat 
merekam apa yang terjadi terhadap file ataupun direktori dan menampilkannya dalam bentuk baris record yang bisa saya format sendiri outputnya,
setelah kesa-kesini mencari akhirnya dapat juga dan jadilah tool ini.

## windows 
Untuk yang --> `/windows/watchdog.py` untuk melakukan monitor action terhadap file di sistem operasi windows,
telah dilakukan ujicoba pada windows 10
### kekurangannya watchdog.py
kekurangan watchdog.py adalah tidak bisa menghandel action atau kejadian ketika file diakses atau file di buka,
hanya menghandel action atau kejadian ketika file diubah, dihapus, direname, dan perubahan size. 
### How To : 
1. Download Script diatas, pilih sesuai base os anda, setelah download extract dan ingat nama foldernya
2. Pastikan anda telah meng-install python 3.x pada windows anda 
3. Buka CMD.exe atau CommandPrompt dan arahkan ke folder script yang anda download
4. Install module `win32file`, dengan perintah di cmd.exe (sebagai administrator) : `pip install pywin32`, kalo sudah lanjut..
5. dan ketik perintah : `python watchdog.py` setelah itu isi drive atau folder yang akan di monitor contoh, `Path to Watch : C:\`
* kalo ada pesan Eroor module mising, tinggal gunakan perintah `pip install <modulname>`, exp: `pip install mondulname` or google it !.

## linux
Untuk yang --> `/linux/dir-monitor-all-even.py` untuk melakukan monitor action terhadap file di sistem operasi Linux,
telah dilakukan ujicoba pada Linux Lubuntu base on ubuntu 16.04.
### kekurangan dir-monitor-all-even.py
kekurangan dir-monitor-all-even.py adalah action yang diberikan terlalu "rame" atau terlalu banyak sehingga ketika satu file 
diakses maka akan menampilkan even action close_write, access, dan open sehingga terasa sangat "rame" di raportnya.
### How To : 
1. Download Script diatas, pilih sesuai base os anda, setelah download extract dan ingat nama foldernya
2. Buka bash terminal dan arahkan ke folder script yang anda download
3. dan ketik perintah : `python dir-monitor-all-even.py` setelah itu isi folder yang akan di monitor contoh, `Folder to Watch : /var/log`
* kalo ada pesan Eroor module mising, tinggal gunakan perintah `pip install <modulname>`, exp: `pip install mondulname` or google it !.