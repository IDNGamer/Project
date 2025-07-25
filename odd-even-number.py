print('Selamat Datang Di Penentu Ganjil-Genap')

n = int(input('masukkan range angka disini : '))
choice = input('genap atau ganjil ? ketik disini : ').lower()

if choice == 'genap':
    for i in range(n):
        if i % 2 == 0:
            print(i)
        
elif choice == 'ganjil':
    for i in range(n):
        if i % 2 != 0:
            print(i)

else:
    print('Input salah atau tidak valid')