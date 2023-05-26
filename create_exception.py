class InvaildAgeException(Exception):
    #"raised when the input value is less them 18"
    pass
num = int(input("enter the age of person:"))
if num<18:
    raise InvaildAgeException
else:
    print('Eligible to vote:')
    