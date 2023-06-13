""" OPERASI KOMPARASI
    SETIAP HASIL DARI KOMPARASI BERNILAI BOOLEAN
    (>, <, >=, <=, ==, !=, IS, IS NOT)
"""

a = 4
b = 2

# Lebih besar dari >
print(20*"=", "Lebih besar dari (>)")
hasil = a > 3
print(f"{a} > 3 = {hasil}")
hasil = b > 3
print(f"{b} > 3 = {hasil}")
hasil = b > 2
print(f"{b} > 2 = {hasil} \n")


# Kurang dari dari <
print(20*"=", "Kurang dari (<)")
hasil = a < 3
print(f"{a} < 3 = {hasil}")
hasil = b < 3
print(f"{b} < 3 = {hasil}")
hasil = b < 2
print(f"{b} < 2 = {hasil} \n")

# Lebih dari sama dengan >=
print(20*"=", "Lebih dari sama dengan (>=)")
hasil = a >= 3
print(f"{a} >= 3 = {hasil}")
hasil = b >= 3
print(f"{b} >= 3 = {hasil}")
hasil = b >= 2
print(f"{b} >= 2 = {hasil} \n")

# Kurang dari sama dengan <=
print(20*"=", "Kurang dari sama dengan (<=)")
hasil = a <= 3
print(f"{a} <= 3 = {hasil}")
hasil = b <= 3
print(f"{b} <= 3 = {hasil}")
hasil = b <= 2
print(f"{b} <= 2 = {hasil} \n")

# Sama dengan ==
print(20*"=", "Sama dengan (==)")
hasil = a == 3
print(f"{a} == 3 = {hasil}")
hasil = b == 3
print(f"{b} == 3 = {hasil}")
hasil = b == 2
print(f"{b} == 2 = {hasil} \n")

# Tidak sama dengan !=
print(20*"=", "Tidak sama dengan (!=)")
hasil = a != 3
print(f"{a} != 3 = {hasil}")
hasil = b != 3
print(f"{b} != 3 = {hasil}")
hasil = b != 2
print(f"{b} != 2 = {hasil} \n")

print(20*"=", "object identity (is)")
# 'is' sebagai komparasi object identity
x = 5  # Ini adalah assignment membuat object
y = 6
print(f"Nilai x = {x}, Id = {hex(id(x))}")
print(f"Nilai x = {y}, Id = {hex(id(y))}")
hasil = x is y
print(f"hasil {x} is {y} = {hasil}")

print(20*"=", "object identity (is not)")
# 'is not' sebagai komparasi object identity
print(f"Nilai x = {x}, Id = {hex(id(x))}")
print(f"Nilai x = {y}, Id = {hex(id(y))}")
hasil = x is not y
print(f"hasil {x} is not {y} = {hasil}")
