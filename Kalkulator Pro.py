#Sambutan
print("Selamat Datang di Kalkulator Pro! silahkan")


#Input
number1 = int(input('masukkan angka pertama : '))
number2 = int(input('masukkan angka kedua : '))


#Fungsi 1 Kalkulator
print("Perhitungan")

#Penjumlahan
add = number1 + number2
print(f'{number1} + {number2} = {add}')


#Pengurangan
sub = number1 - number2
print(f'{number1} - {number2} = {sub}')


#Perkalian
mul = number1 * number2
print(f'{number1} X {number2} = {mul}')


#Pembagian
div = number1 / number2
print(f'{number1} / {number2} = {div}')


#Sisa pembagian
mod = number1 % number2
print(f'{number1} % {number2} = {mod}')


#Pangkat
expo = number1 ** number2
print(f'{number1} ^ {number2} = {expo}')


#Pembagian dengan hasil dibulatkan ke bawah
floor_div = number1 // number2
print(f'{number1} // {number2} = {floor_div}')


#fungsi 2 Perbandingan
print("Perbandingan")

#Persamaan
print(f'Apakah {number1} Sama dengan {number2}?')
print(number1 == number2)

#Pertidaksamaan
print(f'Apakah {number1} Tidak sama dengan {number2}?')
print(number1 != number2)


#Lebih besar dari
print(f'Apakah {number1} Lebih besar dari {number2}?')
print(number1 > number2)


#Lebih kecil dari
print(f'Apakah {number1} Lebih kecil dari {number2}?')
print(number1 < number2)


#Lebih besar sama dengan
print(f'Apakah {number1} Lebih besar sama dengan {number2}?')
print(number1 >= number2)


#Lebih kecil sama dengan
print(f'Apakah {number1} Lebih kecil sama dengan {number2}?')
print(number1 <= number2)