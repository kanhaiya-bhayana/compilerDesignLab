from re import fullmatch

RE = input("Enter Regular Expression:")
RE = RE.replace('+','|')

while True:
    str = input("Enter String to test:")
    temp = bool(fullmatch(RE,str))
    if temp:
        print("This grammar is regular!")
    else:
        print("You entered the wrong grammar, Please enter valid grammar!")
