def is_valid_email(email):
    if email.count('@') != 1:
        return False
    local,domain=email.split('@')

    if not local or not domain or '.' not in domain:
        return False
    domain_split=domain.split('.')
    
    if len(domain_split[-1])<2:
        return False

    allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ123456789._%+-'
    for i in local:
        if i not in allowed_chars:
            return False

    domain_allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTVWXYZ123456789.-'
    for i in domain_split:
        if not i:
            return False
        valid=True
        for j in i:
            if j not in domain_allowed_chars:
                valid=False
                break
        if not valid:
            return False
    return True

email=input("Enter a email address:")
if is_valid_email(email):
    print("It's an valid email address!")
else:
    print("It's an invalid email address!")

