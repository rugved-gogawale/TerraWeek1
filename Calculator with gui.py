

# This is a calclator made entirely in python !
#First i need to ask what command they want to use
import math

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
    sub.title("Subtraction")
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
def submul(mul1,mul2,Resultsmul):#This is the function where the calculations for multiplication will happen
    fmul1=float(mul1.get())#This is where the users input one will be turned into a float 
    fmul2=float(mul2.get())#This is where the users second input will  be a float
    finalmul=fmul1*fmul2#This is where the main calculation will happen and it will get turned into a variable
    Resultsmul.config(text=(f"Result of {fmul1} x {fmul2} = {finalmul}"))#this is where the result label will change to display the answer of the calculatiom
def multiplication():
    mul=tk.Tk()#Makes a new window for multiplication
    mul.title("Multiplication")#gives the window a title at the top
    mul.configure(background="green")#This changes the background of the window to green 
    mul.minsize(200, 200)#This sets the minimum size of the window
    mul.maxsize(500, 500)#This sets the maximum size of the window
    mul.geometry("300x300+50+350")#This sets the size of the window and where it will spawn in on the screen
    labelnum1mul=tk.Label(mul,text="Enter number 1")#this creates a label above the first entry box to tell the user to input the fist number
    labelnum1mul.pack()#this places the label on the screen
    mul1=tk.Entry(mul,width=30)#This creates the first entry box for the user to input  the fist number
    mul1.pack()#This places the first entry box on the screen
    labelnum2mul=tk.Label(mul, text="Enter number 2")#This creates a label above the second entry box
    labelnum2mul.pack()#This places the label on the screen above the entry box
    mul2=tk.Entry(mul,width=30)#This makes the entry box for the second input
    mul2.pack()#This places the second entry box on the screen
    Resultsmul=tk.Label(mul,text="Results will appear here")#This makes a label which will get changed due to .config in submul
    Resultsmul.pack()#This places the label on the window
    sumbitmul=tk.Button(
        mul,
        text="Submit",
        bg="green",
        width=25,
        command=lambda : submul(mul1,mul2,Resultsmul)
    )#This makes the buttomn to run the submul comman
    sumbitmul.pack()
def subdiv(div1,div2,Resultsdiv):#This is the function where the calculations for division will happen
    fdiv1=float(div1.get())#This is where the users input one will be turned into a float
    fdiv2=float(div2.get())#This is where the users input 2 wil be turned into a float
    finaldiv = fdiv1/fdiv2#This is where the calculation happens and it gets stored in finaldiv
    Resultsdiv.config(text=(f"Result of {fdiv1}/ {fdiv2} = {finaldiv}"))#This gets gets the result label to change and show the answer
def division ():#This is where the window for division is created from the button below
    div=tk.Tk()#Makes a new window for division 
    div.title("Division")#So the divsion window has a title at the top
    div.configure(background="blue")#This makes the background of the window blue
    div.minsize(200, 200)#This sets the minimum size of the window of divsion to 200,200
    div.maxsize(500, 500)#This sets the maximum size of the window of division to 500,500
    div.geometry("300x300+350+350")#This sets the coordinates of the window and where it will spawn in 
    labelnum1div=tk.Label(div, text="Enter number 1")#This is a label above the first entry box to tell the user to input the first number
    labelnum1div.pack()#the label is put on the window
    div1=tk.Entry(div, width=30)#This makes the entry box
    div1.pack()#This puts the entrybox below the enter number label
    labelnum2div=tk.Label(div, text="Enter number 2")#This makes a label to tell the user to type the second number
    labelnum2div.pack()#This places the label on the window
    div2=tk.Entry(div, width=30)#This makes the entry box for second number
    div2.pack()#This places the entry box below the label
    Resultsdiv=tk.Label(div, text="Results will appear here")#This makes the label which will display results later
    Resultsdiv.pack()#This places the label on the screen
    submitdiv=tk.Button(
        div,
        text="Submit",
        bg="blue",
        width=25,
        command= lambda : subdiv(div1,div2,Resultsdiv))#This makes the button for division and runs the subdiv function
    submitdiv.pack()#This places the submit button on the screen
def subsqr(sqr1,Resultssqr):
    f1sqr=float(sqr1.get())
    f2sqr=math.sqrt(f1sqr)
    Resultssqr.config(text=(f"Result of {f1sqr}'s square root is {f2sqr}"))
def squareroot():
    square=tk.Tk()
    square.title("Square Root")
    square.configure(background="orange")
    square.minsize(200, 200)
    square.maxsize(500,500) 
    square.geometry("300x300+650+50")
    labelnum1sqr=tk.Label(square, text="Enter number for square root")
    labelnum1sqr.pack()
    square1=tk.Entry(square, width=30)
    square1.pack()
    Resultssqr=tk.Label(square, text="Results will appear here")
    Resultssqr.pack()
    submitsquare= tk.Button(
        square,
        text="Submit",
        bg="orange",
        width=25, 
        command= lambda : subsqr(square1, Resultssqr)
    )
    submitsquare.pack()
def subsq(sq1,sq2,Resultssq):
    fsq1=float(sq1.get())
    fsq2=float(sq2.get())
    finalsq=fsq1**fsq2
    Resultssq.config(text=(f"Result of {fsq1} to the power of {fsq2} is {finalsq}"))
def squaress():
    ssquare=tk.Tk()
    ssquare.title("Squares")
    ssquare.configure(background="purple")
    ssquare.minsize(200, 200)
    ssquare.maxsize(500,500)
    ssquare.geometry("300x300+650+350")
    sq1l=tk.Label(ssquare, text="Type the number")
    sq1l.pack()
    sq1=tk.Entry(ssquare, width=30)
    sq1.pack()
    sq2l=tk.Label(ssquare, text="Type the power")
    sq2l.pack()
    sq2=tk.Entry(ssquare, width=30)
    sq2.pack()
    Resultssq=tk.Label(ssquare, text="Results will appear here")
    Resultssq.pack()
    submitsq=tk.Button(
        ssquare,
        text="Submit",
        bg="purple",
        width=25,
        command= lambda : subsq(sq1, sq2, Resultssq)
    )
    submitsq.pack()
root = tk.Tk()#creates window
root.title("Main Calculator Hub")#This gives title at the top
root.geometry("300x200+50+50")#This gives the space taken on the screen and where it spawns in 
label = tk.Label(root, text="Calculator fully in python !")# This gives text to label
label.pack()#This places the label inside the window 
addbutton = tk.Button(root, text="Addition",bg="Yellow", width=25, command=addition)# This creates the button widget and gives it text and makes the button colour yellow the last command makes the application close after the button is pressed 
addbutton.pack()# this places the button in the window that we placed above so it fits inside the window and when its pressed the window that got placed earlier will dissapear
subbutton= tk.Button(root, text="Subtraction", bg="Red", width=25, command=subtraction)#This creates the button for subtraction and when its pressed it will run the command of subtraction
subbutton.pack()#This places button on the screen
mulbutton=tk.Button(root, text="Multiplication",bg="Green", width=25, command=multiplication)#This creates the button for the Multiplication
mulbutton.pack()#This places button on the window
divbutton=tk.Button(root, text="Division", bg="Blue", width=25, command=division)#This creates the button for the division window to be made
divbutton.pack()#This places button on the main "root" window
sqrbutton=tk.Button(root,text="Square Root", bg="Orange", width=25, command=squareroot)
sqrbutton.pack()
sqqbutton=tk.Button(root,text="Square", bg="Purple", width=25, command=squaress)
sqqbutton.pack()
root.mainloop()

