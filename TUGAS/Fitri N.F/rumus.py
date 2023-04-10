# SEGITIGA
def rumus_luas_segitiga():
    print(" ")
    print("             Menghitung luas segitiga")
    print("===================================================")
    alas = int(input("Masukan alas : "))
    tinggi = int(input("Masukkan tinggi : "))
    print("====================================")
    luas = 0.5*(alas*tinggi)
    print(f"Luas segitiga dari alas {alas}cm tinggi {tinggi}cm adalah : {luas}")
    print('Terimakasih Telah Menggunakan Program Saya :)')
    print(" ")

def rumus_keliling_segitiga():
    print(" ")
    print("          Menghitung keliling segitiga")
    print("===================================================")
    a = int(input("Masukan sisi a : "))
    b = int(input("Masukkan sisi b : "))
    c = int(input("Masukkan sisi c : "))
    keliling = int(a + b + c)
    print("====================================")
    print(f"keliling segitiga dari sisi a {a}cm sisi b {b}cm sisi c {c} adalah : {keliling}")
    print('Terimakasih Telah Menggunakan Program Saya :)')
    print(" ")


# PERSEGI
def rumus_luas_persegi():
    print(" ")
    print("            Menghitung luas persegi")
    print("===================================================")
    sisi = int(input("Masukan sisi : "))
    luas = int(sisi*sisi)
    print("====================================")
    print(f"Luas persegi dari sisi {sisi}cm adalah : {luas}")
    print('Terimakasih Telah Menggunakan Program Saya :)')
    print(" ")

def rumus_keliling_persegi():
    print(" ")
    print("           Menghitung keliling persegi")
    print("===================================================")
    sisi = int(input("Masukan sisi : "))
    keliling = int(4 * sisi)
    print("====================================")
    print(f"Keliling persegi dari sisi {sisi}cm adalah : {keliling}")
    print('Terimakasih Telah Menggunakan Program Saya :)')
    print(" ")


# PERSEGI PANJANG
def rumus_luas_persegi_panjang():
    print(" ")
    print("         Menghitung luas persegi panjang")
    print("===================================================")
    panjang = int(input("Masukan panjang : "))
    lebar = int(input("Masukan lebar : "))
    print("====================================")
    luas = int(panjang * lebar)
    print(f"Luas persegi panjang dari panjang {panjang}cm lebar {lebar}cm adalah : {luas}")
    print('Terimakasih Telah Menggunakan Program Saya :)')
    print(" ")

def rumus_keliling_persegi_panjang():
    print(" ")
    print("       Menghitung keliling persegi panjang")
    print("===================================================")
    panjang = int(input("Masukan panjang : "))
    lebar = int(input("Masukan lebar : "))
    print("====================================")
    keliling = int((2 * panjang) + (2 * lebar))
    print(f"keliling persegi panjang dari panjang {panjang}cm lebar {lebar}cm adalah : {keliling}")
    print('Terimakasih Telah Menggunakan Program Saya :)')
    print(" ")
    print(" ")


# LINGKARAN
def rumus_luas_lingkaran():
    print(" ")
    print("     Menghitung luas lingkaran")
    print("===================================================")
    print("1. Diameter")
    print("2. Jari - jari")
    choice = input("Masukkan pilihan : ")
    if choice == '1':
        print("====================================")
        d = int(input("Masukkan nilai diameter : "))
        print("====================================")
        r = d * 0.5
        if (r % 7) == 0 :
            luas = int((r * r) * 22 / 7)
            print(f"Luas lingkaran dari diameter {d}cm adalah : {luas}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")
        else:
            luas = float((r * r) * 3.14)
            print(f"Luas lingkaran dari diameter {d}cm adalah : {luas}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")

    elif choice == '2':
        print("====================================")
        r = int(input("Masukkan nilai jari  - jari : "))
        print("====================================")
        if (r % 7) == 0 :
            luas = int((r * r) * 22 / 7)
            print(f"Luas lingkaran dari jari - jari {r}cm adalah : {luas}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")
        else:
            luas = float(3.14 * (r * r) )
            print(f"Luas lingkaran dari jari - jari {r}cm adalah : {luas}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")
    

def rumus_keliling_lingkaran():
    print(" ")
    print("        Menghitung keliling lingkaran")
    print("===================================================")
    print("1. Diameter")
    print("2. Jari - jari")
    choice = input("Masukkan pilihan : ")
    if choice == '1':
        print("====================================")
        d = int(input("Masukkan nilai diameter : "))
        print("====================================")
        if (d % 7) == 0 :
            keliling = int(d * 22 / 7)
            print(f"keliling lingkaran dari jari - jari {d}cm adalah : {keliling}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")
        else:
            keliling = float(d * 3.14)
            print(f"keliling lingkaran dari jari - jari {d}cm adalah : {keliling}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")

    elif choice == '2':
        print("====================================")
        r = int(input("Masukkan nilai jari  - jari : "))
        print("====================================")
        d = int(2 * r)
        if (d % 7) == 0 :
            keliling = int(d * 22 / 7)
            print(f"keliling lingkaran dari jari - jari {r}cm adalah : {keliling}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")
        else:
            keliling = float(d * 3.14)
            print(f"keliling lingkaran dari jari - jari {r}cm adalah : {keliling}")
            print('Terimakasih Telah Menggunakan Program Saya :)')
            print(" ")