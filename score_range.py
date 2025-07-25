print('Welcome to Score Judger!')
number1 = int(input('Enter Your Score Here: '))

if number1 >85:
    print('Grade A')
elif number1 <85 and number1 >70:
    print('Grade B')
elif number1 <70 and number1 >50:
    print('Grade C')
elif number1 <50:
    print('Grade D')