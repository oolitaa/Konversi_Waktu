# Soal 1 - Konversi Waktu (30 Poin)

# Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").

# HH : Hours, 2 digits, range: 00 - 99

# MM : Minutes, 2 digits, range: 00 - 59

# SS : Seconds, 2 digits, range: 00 - 59

# Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

# def timeConverter(seconds):
#       .....
 

# Masukkan detik : 3600
# Konversi : 01:00:00

# Masukkan detik : 3665
# Konversi : 01:01:05
# Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string akan keluar notifikasi. Invalid Input

# Masukkan detik : ujian
# Invalid Input!

# Masukkan detik : 20.5
# Invalid Input!


def timeConverter(waktu):
    konversi = int(waktu)
    jam = round((konversi/60)/60)
    menit = round((konversi/60)%60)
    detik = str(konversi%60)

    if(len(str(jam)) < 2):
        jam = str(jam)
        jam = '0' + jam
    else:
        jam = jam

    if (len(str(menit)) < 2):
        menit = str(menit)
        menit = '0' + menit
    else :
        menit = menit
    
    if (len(str(detik)) < 2):
        detik = str(detik)
        detik = '0' + detik 
    else:
        detik = detik
    print(f'{jam}:{menit}:{detik}')

waktu = input('Masukkan detik :')
timeConverter(waktu)
