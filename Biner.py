# Welcoming Massage
print('Welcome to Decimals to Biner and Biner to Decimals Converter!')

# Number input
number = int(input('Decimals Goes Here (Type 0 to ignore): '))
number1 = (input('Biner Goes Here (Type 0 to ignore ) : '))

# Convert To Biner
# Converter Showing Decimals
print('Decimals Input')
print(number)

# Converter Working (Decimals To Biner)...
numbertobiner = bin(number)

# Converter Showing Results
num = numbertobiner.replace("0b","")
print('Biner Output')
print(num)

# Convert To Decimals
# Converter Showing Biner
print('Biner Input')
print(number1)

#Converter Working (Biner To Decimals)...
binertonumber = int(number1, 2)

# Converter Showing Decimals
print('Decimals Output')
print(binertonumber)