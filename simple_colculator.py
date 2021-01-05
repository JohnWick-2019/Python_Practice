
def answer_user():
    answer = input('Do you wont continue? (y / n)\n')

    if answer == 'y' or answer == 'Y':
        return True
    else:
        return False


print('This is a simple colculator programm\n')
print('\t\tHelp:\n')
print('\tPress "+"to addition')
print('\tPress "-" to subtraction')
print('\tPress "*" to multiplication')
print('\tPress "/" to division\n')

flag = True

while flag:

    first_number = float(input('Enter first number: '))
    simbol = input('What you wont to do? ')
    second_number = float(input('Enter second number: '))
    print()    
    
    if simbol == '+':
        print(first_number + second_number)

        user_answer = answer_user()

        if user_answer:
            continue
        else:
            flag = False
        
    if simbol == '-':
        print(first_number - second_number)
        
        user_answer = answer_user()

        if user_answer:
            continue
        else:
            flag = False

    if simbol == '*':
        print(first_number * second_number)
        
        user_answer = answer_user()

        if user_answer:
            continue
        else:
            flag = False

    if simbol == '/':
        if second_number != 0:
            print(first_number / second_number)

            user_answer = answer_user()

            if user_answer:
                continue
            else:
                flag = False

        else:
            print('Division by zero!!!')

            user_answer = answer_user()

            if user_answer:
                continue
            else:
                flag = False

print('The end!')
    