def fibonacci(n):
    if n<=0:
        print("Please enter a positive number!")
        return 
    elif n==1:
        return [0]
    else:
        sequence=[0,1]
        for i in range(2,n):
            sequence.append(sequence[-1]+sequence[-2])
        return sequence

n=int(input('Enter the number of Terms: '))
seq=fibonacci(n)
print("The fibonacci sequence is:",seq)