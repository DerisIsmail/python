"""
    OPERASI LOGIKA ATAU BOOLEAN
    NOT, OR, AND, XOR
"""

# NOT
print(f"{10*'='} NOT {10*'='} \n")

a = False
c = not a
print(f"Data a = {a}")
print(f"{15*'-'} NOT")
print(f"Data c = {c} \n")

# OR (Akan True jika Salah Satu bernilai True)
print(f"{10*'='} OR {10*'='} ")

a = False
b = False
c = a or b
print(f"{a} OR {b} = {c}")
a = False
b = True
c = a or b
print(f"{a} OR {b}  = {c}")
a = True
b = False
c = a or b
print(f"{a}  OR {b} = {c}")
a = True
b = True
c = a or b
print(f"{a}  OR {b}  = {c} \n")


# AND (Akan True jika Semuanya bernilai True)
print(f"{10*'='} AND {10*'='} ")

a = False
b = False
c = a and b
print(f"{a} AND {b} = {c}")
a = False
b = True
c = a and b
print(f"{a} AND {b}  = {c}")
a = True
b = False
c = a and b
print(f"{a}  AND {b} = {c}")
a = True
b = True
c = a and b
print(f"{a}  AND {b}  = {c} \n")

# XOR (Akan True jika salah satu bernilai True, sisanya False) => OPERATOR BITWISE
print(f"{10*'='} XOR {10*'='} ")

a = False
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")
a = False
b = True
c = a ^ b
print(f"{a} XOR {b}  = {c}")
a = True
b = False
c = a ^ b
print(f"{a}  XOR {b} = {c}")
a = True
b = True
c = a ^ b
print(f"{a}  XOR {b}  = {c} \n")
