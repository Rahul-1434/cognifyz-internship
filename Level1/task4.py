def calculator():

    try:
        num1=float(input('Enter First Number: '))
        operator=input('Enter an operator( + , - , * , / , % ): ')
        num2=float(input('Enter Second Number: '))

        if operator=='+':
            result=num1+num2
        elif operator=='-':
            result=num1-num2
        elif operator=='*':
            result=num1*num2
        elif operator=='/':
            if num2==0:
                print('Division by zero is not allowed!')
                return
            else:
                result=num1/num2
        elif operator=='%':
            if num2==0:
                print('Division by zero is not allowed!')
                return
            else:
                result=num1%num2
        else:
            print('Invalid operator!')
            return

        print(f'result: {num1}{operator}{num2}={result}')
    except ValueError:
        print('Please enter a numarical values!')
calculator()