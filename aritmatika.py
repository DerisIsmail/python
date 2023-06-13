""" OPERASI ARITMATIKA """
a = 10
b = 3

# operasi tambah (+)
hasil = a + b
print(f"{a} + {b} = {hasil}")

# operasi pengurangan (-)
hasil = a - b
print(f"{a} - {b} = {hasil}")

# operasi perkalian (*)
hasil = a * b
print(f"{a} x {b} = {hasil}")

# operasi pembagian (/)
hasil = a / b
print(f"{a} : {b} = {hasil}")

# operasi eksponen / pangkat (**)
hasil = a ** b
print(f"{a} ** {b} = {hasil}")

# operasi modulus / sisa bagi (%)
hasil = a % b
print(f"{a} % {b} = {hasil}")

# operasi floor division / counter dari modulus (//)
hasil = a // b
print(f"{a} // {b} = {hasil}")

""" 
PRIORITAS OPERASI PADA ARITMATIKA 
1. ()
2. Ekponen / Pangkat (**)
3. Perkalian / Pembagian / Modulus & Floor Division
4. Pertambahan or Pengurangan
"""

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(f"{x} ** {y} * ({z} + {x}) / {y} - {y} % {z} // {x} = {hasil}")
