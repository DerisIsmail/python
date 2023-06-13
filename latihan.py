# Latihan Logika dan komparasi

# Membuat area rentang dari angka

# +++++++3---------10+++++++

inputUSer = int(input(
    f"Masukan angka yang bernilai \nKurang dari 3\natau\nLebih dari 10 : "))

# +++++++3------------------
# memeriksa angka kurang dari 3
isKurangDari = inputUSer < 3
print(f"Apakah {inputUSer} < 3 = {isKurangDari}")

# -----------------10+++++++
# memeriksa angka lebih dari 10
isLebihDari = inputUSer > 10
print(f"Apakah {inputUSer} > 10 = {isLebihDari}")

# +++++++3---------10+++++++
isCorrect = isKurangDari or isLebihDari
print(f"Angka yang anda masukan = {isCorrect}")
