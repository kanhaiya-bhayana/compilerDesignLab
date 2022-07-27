from random import choices, randint
from re import fullmatch

RE = input("Enter Regular Expression:")
RE = RE.replace('+','|')

lst = ['a','b']
found = 0
while found<10:
    k = randint(1,5)
    s = ''.join(choices(lst, k=k))
    if bool(fullmatch(RE,s)):
        print(s)
        found +=1
    # print(s)
    
