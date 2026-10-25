

# This is a calclator made entirely in python !
#First i need to ask what command they want to use
import tkinter as tk#This is the library for gui in python called tkinter
def subadd(number1,number2, finish):
    
  
    fnumber1=float(number1.get())#This gets the users input from th euser and then gets saved into the variable of number 1
    fnumber2=float(number2.get())#This gets the users inper so the user fill fill inthe line for the second number and then gets saves into the variable of number 2 
    final=fnumber1+fnumber2# this adds the 2 numbers from the user and adds them to the variable "a" 
    finish.config(text=(f"Result of {fnumber1} + {fnumber2} is {final}"))#This changes the phrase which used to be above the submit button to give the answer in the phrase
def addition():# This is being called from above and execuing whats below

    add = tk.Tk()#This creates a new window

    # Setting some window properties
    add.title("Add")#This gives the window that has been created a title at the top
    add.configure(background="yellow")#This changes the background of the window to yellow
    add.minsize(200, 200)# This sets the minimum height and width
    add.maxsize(500, 500)#This sets the maximum height and with
    add.geometry("300x300+50+50")#This gives the size when the window and it igives the coordinates where the window will get created
    labelenternumber1=tk.Label(add, text="Enter number 1", bg="White")#This is text to tell the user to input the number here
    labelenternumber1.pack()#This just places it on the screen
    number1=tk.Entry(add,width=30)#This makes a text box which the user can type in the number
    number1.pack()#This just packs it on the screen
    labelenternumber2=tk.Label(add, text="Enter number 2", bg="White")#This is text to type the second number for the userto input below
    labelenternumber2.pack()#This just places it on the screen
    number2 =tk.Entry(add,width=30)#This gives the second entry box so the user can input the second number
    number2.pack()#This gives the second number entry box to be placed
    finish=tk.Label(add,text="Result; will appear here...")#This is a label wwhichwill be changed due to the .config above
    finish.pack ()# This just places the result label
    
    submitbutton = tk.Button(
        add, 
        text="Submit",
        bg="Yellow", 
        width=25, 
        command=lambda : subadd(number1,number2,finish))#This is the result button so when its pressed it wil run the funtion subadd
    submitbutton.pack()#This just places on the window
def subsub(sub1,sub2,Resultsub):#This is from when this command is called from the button below
    fsub1=float(sub1.get())#this turns the users input into a float
    fsub2=float(sub2.get())#This turns the users input into a float
    finalsub=fsub1-fsub2#This does the calculation and saves it in a variable
    Resultsub.config(text=(f"Result of {fsub1} - {fsub2} = {finalsub}"))#This  changes the result label to display the answers
def subtraction():
    sub =tk.Tk()#This makes the new gui window for substraction
    sub.configure(background="red")#This gives the background colour red just like the colour of the button in the first menu
    sub.minsize(200,200)#This sets some parameters for the window so it can only be turned into a minimum size of 200by 200
    sub.maxsize(500,500)#This sets the maximum parameters for the window so it can only be a maximum of 500 by 500
    sub.geometry("300x300+350+50")#This sets the size and where it starts on the screen
    labelenternumber1sub=tk.Label(sub, text="Enter number 1", bg="White")#This  just is a label above the first entry box to type in the code
    labelenternumber1sub.pack()#This just places on the screen 
    sub1=tk.Entry(sub,width=30)#This just makes the entry box with a width of 30
    sub1.pack()#This just makes the entry box 1 appear on the screen 
    labelenternumber2sub=tk.Label(sub, text="Enter number 2", bg="White")#this just makes the label above the second entry box 
    labelenternumber2sub.pack()# this places the label on the screen
    sub2=tk.Entry(sub,width=30)#This makes the second entry box
    sub2.pack()#This places entry box on the screen
    Resultsub=tk.Label(sub, text="Result will appear here ")#This makes a result labelwhich will get changed later by .config
    Resultsub.pack()#This places the button on the screen
    submitsub= tk.Button(
        sub,
        text="Submit",
        bg="Red",
        width=25,
        command=lambda : subsub(sub1,sub2,Resultsub)
    )#This sets therules for the button so when its pressed it will run the subsub command and the button will be a red colour
    submitsub.pack()#This places the button on the screen
def multiplication():
    mul=tk.Tk()#Makes a new window for multiplication
    mul.title("Multiplication")#gives the window a title at the top
    mul.configure(background="green")
    mul.minsize(200, 200)
    mul.maxsize(500, 500)
    mul.geometry("300x300+50+350")
    labelnum1mul=tk.Label(mul,text="Enter number 1")
    labelnum1mul.pack()
    mul1=tk.Entry(mul,width=30)
    mul1.pack()
    labelnum2mul=tk.label(mul, text="Enter number 2")
    labelnum2mul.pack()
    mul2=tk.Entry(mul,width=30)
    mul2.pack()
    Resultsmul=tk.Label(mul,text="Results will appear here")
    Resultsmul.pack()
    sumbitmul=tk.Button(
        mul,
        text="Submit"
        bg="green"
        width=25
        command=lambda : submul(mul1,mul2,Resultsmul)
    )

     







root = tk.Tk()#creates window
root.title("Main Calculator Hub")#This gives title at the top
root.geometry("300x150+50+50")#This gives the space taken on the screen and where it spawns in 
label = tk.Label(root, text="Calculator fully in python !")# This gives text to label
label.pack()#This places the label inside the window 
addbutton = tk.Button(root, text="Addition",bg="Yellow", width=25, command=addition)# This creates the button widget and gives it text and makes the button colour yellow the last command makes the application close after the button is pressed 
addbutton.pack()# this places the button in the window that we placed above so it fits inside the window and when its pressed the window that got placed earlier will dissapear
subbutton= tk.Button(root, text="Subtraction", bg="Red", width=25, command=subtraction)#This creates the button for subtraction and when its pressed it will run the command of subtraction
subbutton.pack()#This places button on the screen
root.mainloop()

