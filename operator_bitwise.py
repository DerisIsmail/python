"""
    OPERATOR BITWISE / OPERASI BINER / BINARY
"""

a = 9
b = 5


# Bitwise OR (|)
c = a | b
print(f"{15*'='} OR(|) {15*'='}")
print(f"nilai a : {a}, binary : {format(a,'08b')}")
print(f"nilai b : {b}, binary : {format(b,'08b')}")
print(f"{30*'-'} (|)")
print(f"nilai c :{c}, binary : {format(c,'08b')}\n")


# Bitwise AND (&)
c = a & b
print(f"{15*'='} AND(&) {15*'='}")
print(f"nilai a : {a}, binary : {format(a,'08b')}")
print(f"nilai b : {b}, binary : {format(b,'08b')}")
print(f"{30*'-'} (&)")
print(f"nilai c : {c}, binary : {format(c,'08b')}\n")


# Bitwise XOR (^)
c = a ^ b
print(f"{15*'='} XOR(^) {15*'='}")
print(f"nilai a : {a}, binary : {format(a,'08b')}")
print(f"nilai b : {b}, binary : {format(b,'08b')}")
print(f"{30*'-'} (^)")
print(f"nilai c : {c},binary : {format(c,'08b')}\n")


# Bitwise NOT (~)
c = ~a
d = 0b0000001001
e = 0b1111111111
print(f"{15*'='} NOT(~) {15*'='}")
print(f"nilai a   : {a},    binary : {format(a,'08b')}")
print(f"{40*'-'} (~)")
print(f"nilai c   : {c},  binary : {format(c,'08b')}")
print(f"{40*'-'} (^)")
print(f"nilai e^d : {e^d}, binary : {format(e^d,'08b')}\n")


# Shifting
# shifting right (>>)
c = a >> 2
print(f"{15*'='} (>>) {15*'='}")
print(f"nilai a : {a}, binary : {format(a,'08b')}")
print(f"{30*'-'} (>>)")
print(f"nilai c : {c}, binary : {format(c,'08b')}\n")


# shifting left (<<)
c = a << 2
print(f"{15*'='} (<<) {15*'='}")
print(f"nilai a : {a}, binary : {format(a,'08b')}")
print(f"{30*'-'} (<<)")
print(f"nilai c : {c}, binary: {format(c,'08b')}\n")
