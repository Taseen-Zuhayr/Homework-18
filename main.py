try:
    e = int(input("Enter how old are you : "))
    if e%2==0:
        print("The age is even.")
    else:
        print("The age is odd.")
except:
    print("Enter number",SyntaxError)