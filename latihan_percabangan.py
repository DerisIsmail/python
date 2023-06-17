print(20*"-")
print("KALKULATOR SEDERHANA")
print(20*"-" + "\n")

angaka1 = float(input("Masukan angka 1 = "))
operator = input("operator (+, -, x, /) : ")
angaka2 = float(input("Masukan angka 2 = "))


# Percabangannya

if operator == "+":
    hasil = angaka1 + angaka2
    print(f"Hasilnya Adalah : {hasil}")
elif operator == "-":
    hasil = angaka1 - angaka2
    print(f"Hasilnya Adalah : {hasil}")
elif operator == "x":
    hasil = angaka1 * angaka2
    print(f"Hasilnya Adalah : {hasil}")
elif operator == "/":
    hasil = angaka1 / angaka2
    print(f"Hasilnya Adalah : {hasil}")
else:
    print("Pilahan operator yang anda masukan salah!")
