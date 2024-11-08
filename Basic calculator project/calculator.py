print("This is my new calculator")
print("Here is my all oparations")
print("1.  Addition")
print("2.  Subtraction")
print("3.  Multiplication")
print("4.  Division")

option = int(input("Enter your choice 1/2/3/4 : "))

if option == 1:
    n1 = int(input("Enter your 1st number: "))
    n2 = int(input("Enter your 2nd number: "))
    n3 = n1 + n2
    print("Addition is : " + str(n3))

elif option == 2:
    n1 = int(input("Enter your 1st number: "))
    n2 = int(input("Enter your 2nd number: "))
    n3 = n1 - n2
    print("Addition is : " + str(n3))

elif option == 3:
    n1 = int(input("Enter your 1st number: "))
    n2 = int(input("Enter your 2nd number: "))
    n3 = n1 * n2
    print("Addition is : " + str(n3))

elif option == 4:
    n1 = int(input("Enter your 1st number: "))
    n2 = int(input("Enter your 2nd number: "))
    n3 = n1 / n2
    print("Addition is : " + str(n3))