print('Selamat Datang Di Faktorial Calculator!')

number1 = int(input('Masukkan Angka Disini : '))

def faktorial(number):
    if number == 1:
        return 1
    else:
        result = number*faktorial(number-1)
        return result
    
output = faktorial(number1)
print(number1,'Faktorial')
print('=',output)