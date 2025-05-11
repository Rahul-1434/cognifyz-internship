def password_strength(password):
    strength=0
    if len(password)>=8:
        strength+=1
    uppercase,lowercase,letter,digits,characters=0,0,0,0,0
    s='!@#$%^&*()<?|":{}[]|/\''
    for i in password:
        if i.isupper() and uppercase==0:
            strength+=1
            uppercase=1
        elif i.islower() and lowercase==0:
            strength+=1
            lowercase=1
        elif i.isdigit() and digits==0:
            strength+=1
            digits=1
        elif i in s and characters==0:
            strength+=1
            characters=1
    if strength==5:
        return 'Very Strong.'
    elif strength==4:
        return 'Strong.'
    elif strength==3:
        return 'Moderate.'
    elif strength==2:
        return 'Week.'
    else:
        return 'Verry Week.'
    
password=input("Enter your  password: ")
check=password_strength(password)
print('Your password strength is: ',check)