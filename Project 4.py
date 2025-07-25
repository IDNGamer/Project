number1 = int(input('masukkan angka pertama : '))
number2 = int(input('masukkan angka kedua : '))

print(number1 > number2)
print(number1 < number2)

print(number2 > number1)
print(number2 < number1)

cuaca = input('Hari ini Cuacanya...(hujan/panas/cerah)').lower()
payung = input('Bawa Payung? (Y/N)').lower()
topi = input('Mau Pakai Topi? (Y/N)').lower()

if cuaca == "cerah" and payung == "y" and topi == "n":
    print('Cuacanya cerah, mau jalan-jalan dengan payung?')
elif cuaca == "cerah" and payung == "n" and topi == "y":
    print("Cuacanya cerah, lebih baik memakai topi")
elif cuaca == "cerah" and payung == 'n' and topi == 'n':
    print("Cuacanya cukup cerah untuk piknik")
elif cuaca == "cerah" and payung == "y" and topi == "y":
    print("Cuacanya memang cerah, tapi kamu tetap harus memilih salah satu, payung atu topi?")

else:
    print("Invalid Input")
