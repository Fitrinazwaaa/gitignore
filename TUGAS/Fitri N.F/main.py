from rumus import rumus_luas_segitiga, rumus_keliling_segitiga, rumus_luas_persegi, rumus_keliling_persegi,  rumus_luas_persegi_panjang, rumus_keliling_persegi_panjang, rumus_luas_lingkaran, rumus_keliling_lingkaran

def segitiga():
    choice = input('''Pilih Salah Satu !
        1. Luas Segitiga
        2. Keliling Segitiga
Masukkan pilihan : ''')
    if choice == '1':
        rumus_luas_segitiga()
    elif choice == '2':
        rumus_keliling_segitiga()
    else:
        main()

def persegi():
    choice = input('''Pilih Salah Satu !
        1. Luas Persegi
        2. Keliling Persegi
Masukkan pilihan : ''')
    if choice == '1':
        rumus_luas_persegi()
    elif choice == '2':
        rumus_keliling_persegi()
    else:
        main()

def persegi_panjang():
    choice = input('''Pilih Salah Satu !
        1. Luas Persegi Panjang
        2. Keliling Persegi Panjang
Masukkan pilihan : ''')
    if choice == '1':
        rumus_luas_persegi_panjang()
    elif choice == '2':
        rumus_keliling_persegi_panjang()
    else:
        main()

def lingkaran():
    choice = input('''Pilih Salah Satu !
        1. Luas Lingkaran
        2. Keliling Lingkaran
Masukkan pilihan : ''')
    if choice == '1':
        rumus_luas_lingkaran()
    elif choice == '2':
        rumus_keliling_lingkaran()
    else:
        main()
        

def main():
        print(" ")
        print("                          RUMUS BANGUN DATAR")
        choice = input("""=======================================================================
        1. Rumus Segitiga
        2. Rumus Persegi
        3. Rumus Persegi Panjang
        4. Rumus Lingkaran
        5. EXIT
Masukkan Pilihan : """)
        while True:
            if choice == '1':
                segitiga()
                break
            elif choice == '2':
                persegi()
                break
            elif choice == '3':
                persegi_panjang()
                break
            elif choice == '4':
                lingkaran()
                break
            elif choice == '5':
                print('\033c', end='')
                break
            else:
                choice = input("""Harap masukkan pilihan yang tepat!
Masukkan kembali pilihan : """)
main()