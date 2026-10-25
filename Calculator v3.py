# This is a calclator made entirely in python !
#First i need to ask what command they want to use
def ask():
    a = int(input("""
    Which command do you wish to use? (Type the number in the brackets)
    1. Addition         (1)
    2. Subtraction      (2)
    3. Division         (3)
    4. Multiplication   (4) : """))# This is asking for which function the user wants to use
    if a == 1:#This is for an if statement if the person wants to use addition
        addition()#this is calling the addition command below
    elif a == 2:# This is if the user wants subtraction
        substraction()# This is calling the substraction below
    elif a == 3: # This is if the user wants Division
        division()#This is calling the commmand below
    elif a == 4:# This will tell me if the user wants multiplicatiom
        multiplication()#This is calling the multiplication command below
    else:# This is if the number is not from :1,2,3,4
        ask()# This will ask the starting question again
        

def addition():# This is being called from above and execuing whats below
    num1=int(input("Enter the first number you want to add: "))# This wil give me the first number to add
    num2=int(input("Enter the second number you want to add: "))#This gi[]]es me the second number to add
    print(f"{num1}+{num2}={num1+num2}")# This adds them together in a print statement combining them together
    again=input("Enter if you would want to do the command again (y/n) : ") #This is asking whether the user wants to do the command again or not
    if again == "y":#This is if the user put "y" above
        ask()#This will run the command above again
    elif again == "n":# This is if the user put "n" above
        print("Thank you for using the calculator")#Just a thank you command:)
    else:# This is if anything other than "y" or "n" was typed
        print("Command ending")#This is just to say that the command is ending
        print("Thank you for using the calculator")# Just a thank you command:)
def substraction():#This is being called from above and whats below
    num1=int(input("Enter the number you want to subtract from: "))# This will give me the main number which will get subtracted 
    num2=int(input("Enter the number you want to subtract: "))# This will give me the number which the user wants to subtract
    print(f"{num1}-{num2}={num1-num2}")# Thiss will calculate in a print statement and give an output
    again=input("Enter if you would want to do the command again (y/n) : ") #This is asking whether the user wants to do the command again or not
    if again == "y":#This is if the user put "y" above
        ask()#This will run the command above again
    elif again == "n":# This is if the user put "n" above
        print("Thank you for using the calculator")#Just a thank you command:)
    else:# This is if anything other than "y" or "n" was typed
        print("Command ending")#This is just to say that the command is ending
        print("Thank you for using the calculator")# Just a thank you command:)
def division():# This is being called from above and running the division below
    num1=int(input("Enter the number you want to divide: "))# This asks the user and will give me the users number which the user wants to divide
    num2=int(input("Enter the number you want to divide from the original number: "))# This will give me the number to divide the original number with
    print(f"{num1}÷{num2}={num1/num2}")# This will divide the numbers and give the answer
    again=input("Enter if you would want to do the command again (y/n) : ") #This is asking whether the user wants to do the command again or not
    if again == "y":#This is if the user put "y" above
        ask()#This will run the command above again
    elif again == "n":# This is if the user put "n" above
        print("Thank you for using the calculator")#Just a thank you command:)
    else:# This is if anything other than "y" or "n" was typed
        print("Command ending")#This is just to say that the command is ending
        print("Thank you for using the calculator")# Just a thank you command:)
def multiplication():# This is running whats below
    num1=int(input("Enter the number you want to multiply: "))# This will give me the first number which the user wants to multiply
    num2=int(input("Enter the number you want to multiply: "))# This will give me the second number whic the user wants to multiply
    print(f"{num1}x{num2}={num1*num2}")#This will multiply the numbers together and give a number output
    again=input("Enter if you would want to do the command again (y/n) : ") #This is asking whether the user wants to do the command again or not
    if again == "y":#This is if the user put "y" above
        ask()#This will run the command above again
    elif again == "n":# This is if the user put "n" above
        print("Thank you for using the calculator")#Just a thank you command:)
    else:# This is if anything other than "y" or "n" was typed 
        print("Command ending")#This is just to say that the command is ending
        print("Thank you for using the calculator")# Just a thank you command:)
ask()# This is running the command at the top so the function knows that it has to be executed this is the most important line of code
