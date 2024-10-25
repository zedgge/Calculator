import os

def addition():
    os.system('cls' if os.name == 'nt' else "clear")
    print('Addition')

    continue_calc = 'y'

    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 + num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('Enter more(y/n):'))
        while continue_calc.lower() not in ['y', 'n'] :
            print('please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n):'))

        if continue_calc.lower == 'n':
            break
        num = float(input('Enter another number: '))
        ans += num
        print(f'curent reault: {ans}')
        values_entered += 1
    return [ans, values_entered]

def subtraction() :
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')

    continue_calc = 'y'

    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number:'))
    ans = num_1 + num_2
    values_entered = 2
    print(f'current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('enter more (y/n): '))
        while continue_calc.lower() not in ['y', 'n']:
            print('please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n):'))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        ans -= num
        print(f'current result: {ans}')
        values_entered += 1
    return [ans, values_entered]

def multiplaction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(multiplaction)

    continue_calc = 'y'

    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number:'))
    ans = num_1 * num_2
    values_entered = 2
    print(f'Current result: {ans}')

    while continue_calc.lower() == 'y' :
        continue_calc - (input('Enter more (y/n):'))
        while continue_calc.lower() not in ['y', 'n']:
            print('please enter \'y\' \'n\'')
            continue_calc - (input('Enter more(y/n):'))

        if continue_calc.lower() == 'n':
            break
    num = float(input('Enter another number:'))
    ans *= num
    print(f'Current result: {ans}')
    values_entered += 1
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(division)

    continue_calc = 'y'

    num_1 = float(input('Enter a number:'))
    num_2 = float(input('Enter another number:'))
    while num_2 == 0.0:
        print('please enter a second number > 0')
        num_2 = float(input('Enter another number:'))

    ans = num_1 /num_2
    values_enterd = 2
    print(f'Cureent result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = (input('enter more (y/n):'))
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = (input('Enter more (y/n):'))

        if continue_calc.lower() == 'n':
            break
        num = float(input('Enter another number: '))
        while num == 0.0:
            print ('Please enter a number > 0')
            num = float(input('Enter another number: '))
        ans /= num 
        print(f'Current result: {ans}')
        values_enterd += 1
    return [ans, values_enterd]

def calculator():
    quit = False
    while not quit:
        results = []
        print('simple Calculator in Python!')
        print('Enter \'a\' for additon')
        print('Enter \'s\' for subtraction')
        print('Enter \'m\' for multiplaction')
        print('Enter \'d\' for division')
        print('Enter \'q\' to quit')

        choice = input('Selection:')

        if choice == 'q':
            quit =True
            continue

        if choice == 'a':
            results = addition()
            print('ans = ', results[0], 'total inputs:', results[1])
        elif choice =='s':
            results = subtraction()
            print('ans = ', results[0], 'total inputs:', results[1])
        elif choice == "m":
            results = multiplaction()
            print('ans = ', results[0], 'total inputs:', results[1])
        elif choice == "d":
            results = division()
            print('ans = ', results[0], 'total inputs:', results[1])
        else:
            print('Sorry, invalid charecter')  

if __name__ == '__main__':
    calculator()
