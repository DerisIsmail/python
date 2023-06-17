# Latihan date and time
import datetime as dt

print('Silahkan masukan tanggal bulan dan tahun lahir anda : \n')
tanggal = int(input('Tanggal \t: '))
bulan = int(input('Bulan \t\t: '))
tahun = int(input('Tahun \t\t: '))

hariIni = dt.date.today()
tanggalLahir = dt.date(tahun, bulan, tanggal)

umurHari = hariIni - tanggalLahir
umurTahun = umurHari.days // 365
print(f"Umur anda adalah : {umurTahun} Tahun")
