""" MERUBAH TIPE DATA PADA PYTHON """

""" Merubah dari type data Int ke Float, Str, Boolean """
print("===== INTEGER =====")
data_int = 1
print(f"Data = {data_int}, Type = {type(data_int)}")

# Eksekusi
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # Akan False jika nilai Int = 0 selain itu True
print(f"Data = {data_float}, Type = {type(data_float)}")
print(f"Data = {data_str}, Type = {type(data_str)}")
print(f"Data = {data_bool}, Type = {type(data_bool)}")


""" Merubah dari type data Float ke Int, Str, Boolean """
print("===== FLOAT =====")
data_float = 1.9
print(f"Data = {data_float}, Type = {type(data_float)}")

# Eksekusi
data_int = int(data_float)  # Akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)  # Akan False jika nilai Float = 0 selain itu True
print(f"Data = {data_int}, Type = {type(data_int)}")
print(f"Data = {data_str}, Type = {type(data_str)}")
print(f"Data = {data_bool}, Type = {type(data_bool)}")


""" Merubah dari type data Boolean ke Int, Float, Str """
print("===== BOOLEAN =====")
data_bool = True
print(f"Data = {data_bool}, Type = {type(data_bool)}")

# Eksekusi
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print(f"Data = {data_int}, Type = {type(data_int)}")
print(f"Data = {data_str}, Type = {type(data_str)}")
print(f"Data = {data_float}, Type = {type(data_float)}")


""" Merubah dari type data String ke Int, Float, Boolean """
print("===== STRING =====")
data_str = ""
print(f"Data = {data_str}, Type = {type(data_str)}")

# Eksekusi
# data_int = int(data_str) # -> value harus berupa angka
# data_float = float(data_str) # -> value harus berupa angka
data_bool = bool(data_str)  # Akan False jika string kosong selain itu True
# print(f"Data = {data_int}, Type = {type(data_int)}")
# print(f"Data = {data_float}, Type = {type(data_float)}")
print(f"Data = {data_bool}, Type = {type(data_bool)}")
