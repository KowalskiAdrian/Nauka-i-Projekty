num = input("Enter a number: ")
num2 = input("Enter a second number: ")
try:
    num = int(num)
    num2 = int(num2)
    total = num / num2
except ValueError:
    print("Num or num2 was not a valid numbers")
except ZeroDivisionError:
    print("Numbers could not be divided")
except Exception as e:
    print("Exception was caught")
    print(type(e))
    
    
