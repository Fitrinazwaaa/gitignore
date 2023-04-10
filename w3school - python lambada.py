#PYTHON LAMBADA
'''Fungsi lambda adalah fungsi anonim kecil.
Fungsi lambda dapat mengambil sejumlah argumen, tetapi hanya dapat memiliki satu ekspresi.'''

#Tambahkan 10 ke argument a, dan kembalikan hasilnya:
x = lambda a : a + 10
print(x(5))                                 # === 15

#Kalikan argumen adengan argumen bdan kembalikan hasilnya:
x = lambda a, b : a * b
print(x(5, 6))                              # === 30

#Ringkas argumen a, b, c dan kembalikan hasilnya
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))                           # === 13

#try
b = lambda a,  b, c, d : a * b / c + d
print(b(6, 8, 3, 10))                       # === 26.0

#Gunakan definisi fungsi itu untuk membuat fungsi yang selalu menggandakan angka yang Anda kirim:
def keep(n) :
    return lambda a : a * n
result = keep(2)
print(result(11))                           # === 22













