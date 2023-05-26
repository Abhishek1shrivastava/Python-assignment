try:
    numerator =int(input("enter the numerator:"))
    denominator =int(input("enter the denominator:"))
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0:")
    
finally:
    print("this is finally block.")