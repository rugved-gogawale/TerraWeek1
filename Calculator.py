# This is a calclator made entirely in python !
#First i need to ask what command they want to use
a = int(input("""
Which command do you wish to use? (Type the number in the brackets)
1. Addition         (1)
2. Subtraction      (2)
3. Division         (3)
4. Multiplication   (4) : """))

if a == 1:#This is for an if statement if the person wants to use addition
    num1=int(input("Enter the first number you want to add: "))# This wil give me the first number to add
    num2=int(input("Enter the second number you want to add: "))#This gives me the second number to add
    print(f"{num1}+{num2}={num1+num2}")# This adds them together in a print statement combining them together
elif a == 2:# This is if the user wants subtraction
    num1=int(input("Enter the number you want to subtract from: "))# This will give me the main number which will get subtracted 
    num2=int(input("Enter the number you want to subtract: "))# This will give me the number which the user wants to subtract
    print(f"{num1}-{num2}={num1-num2}")# Thiss will calculate in a print statement and give an output
elif a == 3: # This is if the user wants Division
    num1=int(input("Enter the number you want to divide: "))# This asks the user and will give me the users number which the user wants to divide
    num2=int(input("Enter the number you want to divide from the original number: "))# This will give me the number to divide the original number with
    print(f"{num1}÷{num2}={num1/num2}")# This will divide the numbers and give the answer
elif a == 4:# This will tell me if the user wants multiplicatiom
    num1=int(input("Enter the number you want to multiply: "))# This will give me the first number which the user wants to multiply
    num2=int(input("Enter the number you want to multiply: "))# This will give me the second number whic the user wants to multiply
    print(f"{num1}x{num2}={num1*num2}")#This will multiply the numbers together and give a number output
else:
    print("Error please try restarting the program")#Just incase the user types another number