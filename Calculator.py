# Simple Calculator Program.
# Programmed by Shafiul Kayem.

def Welcome():
    print('''
Welcome to Calculator!
''')
Welcome()
def Calculator():
    try:
        operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')


        num1 = int(input('Please enter the first number: '))
        num2 = int(input('Please enter the second number: '))    
        if operation == '+':
            print('{} + {} = {}'.format(num1, num2, num1 + num2))

        elif operation == '-':
            print('{} - {} = {}'.format(num1, num2, num1 - num2))

        elif operation == '*':
            print('{} * {} = {}'.format(num1, num2, num1 * num2))
    
        elif operation == '/':
            print('{} / {} = {}'.format(num1, num2, num1 / num2))
        else:
            print('You have not typed a valid operator, please run the Program Again.')
    
    except ZeroDivisionError:
        
        print('\nNot Possible to Divide by Zero!')
        
    Again()

def Again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        Calculate()
    elif calc_again.upper() == 'N':
        print('Thanks for using this Calculator!\nThis Calculator Made By Shafiul Kayem! \nSee you later.')
    else:
        Again()

Calculator()
