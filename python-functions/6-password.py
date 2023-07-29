def validate_password(password):
    space=[' ']
    if len(password)<8:
        return(False)
    if not any(char.isdigit() for char in password):
        return(False)
    if not any(char.isupper() for char in password):
        return(False)
    if not any(char.islower() for char in password):
        return(False)
    for i in range(password):
        if i==space:
            return(False)
    return(True)