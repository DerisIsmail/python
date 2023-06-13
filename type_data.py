from ctypes import c_double

""" TIPE DATA PADA PYTHON """

# type data int
data_int = 1
print(type(data_int))

# type data float (desimal)
data_float = 1.5
print(type(data_float))

# type data bool
data_bool = True or False
print(type(data_bool))

# type data str
data_str = 'Deris Ganteng'
print(type(data_str))

""" TIPE DATA KHUSUS """

# bilangan complex
data_complex = complex(5, 6)
# print(data_complex)
print(type(data_complex))

# type data dari bahasa C dengan cara import ---> from from ctypes import c_double untuk contoh
data_c_double = c_double(10)
# print(data_c_double)
print(type(data_c_double))
