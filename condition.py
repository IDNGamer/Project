number1 = int(input('masukkan angka pertama : '))
number2 = int(input('masukkan angka kedua : '))

print(number1 > number2)
print(number1 < number2)

print(number2 > number1)
print(number2 < number1)

cuaca = input('Hari ini Cuacanya...(Hujan/Panas/Cerah)').lower()
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
elif cuaca == "panas" and payung == 'y' and topi == 'n':
    print("Cuacanya sangat panas, lebih baik pakai payung")
elif cuaca == "panas" and payung == 'n' and topi == 'y':
    print("Cuacanya panas mau pakai topi?")
elif cuaca == "panas" and payung == 'n' and topi == 'n':
    print("Cuacanya panas lho")
elif cuaca == "panas" and payung == 'y' and topi == 'y':
    print("Lebih baik kamu memilih salah satu saja")
elif cuaca == "cerah" and payung == 'n' and topi == 'n':
    print("Cuacanya cukup cerah untuk piknik")
else:
    print("Invalid Input")
