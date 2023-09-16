'''This script represents a "Smart Calculator" implemented using the tkinter GUI library.
The calculator is designed to understand and compute basic arithmetic operations expressed
in natural language. Users can enter expressions like "add 5 and 3" or "HCF of 12 and 15",
and the calculator will interpret and compute the result. Supported operations include addition,
subtraction, multiplication, division, modulus, Least Common Multiple (LCM), and Highest Common Factor (HCF).
The user interface also provides buttons for easy access to commonly used functionalities
and displays the result in a clear and readable manner.
'''

from tkinter import *
import tkinter.messagebox as tmsg

# Function to perform addition
def add(x,y):
    return x + y

# Function to perform subtraction
def sub(x,y):
    return x - y

# Function to perform multiplication
def mul(x,y):
    return x * y

# Function to perform division
def div(x,y):
    return x / y

# Function to perform modulus
def mod(x,y):
    return x % y

# Function to compute LCM
def lcm(x,y):
    l = max(x,y)
    while l <= x*y:
        if l % x == 0 and l % y == 0:
            return l
        l+=1

# Function to compute HCF
def hcf(x,y):
    h = min(x,y)
    while h >= 1:
        if x % h == 0 and y % h == 0:
            return h
        h-=1

# Dictionary of supported operations
operations = {'ADD':add, 'PLUS':add, 'SUM':add, 'ADDITION':add,
              'SUB':sub, 'MINUS':sub, 'SUBTRACT':sub,
              'LCM':lcm, 'HCF':hcf, 'PRODUCT':mul,
              'MULTIPLY':mul, 'MULTIPLICATION':mul, 'DIVISION':div,
              'MOD':mod, 'REMAINDER':mod, 'MODULUS':mod}

# Extract numbers from the text
def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

# Enhanced Error Handling with more descriptive messages
def compute():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations:
            try:
                l = extract_from_text(text)
                if len(l) != 2:
                    list.delete(0, END)
                    list.insert(END, 'Error: Please input two numbers.')
                    return
                r = operations[word.upper()](l[0], l[1])
                list.delete(0, END)
                list.insert(END, r)
            except:
                list.delete(0, END)
                list.insert(END, 'Error: Invalid Input. Try "add 5 and 3".')
            finally:
                return
    list.delete(0, END)
    list.insert(END, 'Error: Operation Not Recognized. Try "add 5 and 3".')

# Initializing the tkinter window
root = Tk()
root.geometry('400x600')
root.title('Smart Calculator')

# GUI Components with Placeholder Text
l1 = Label(root, text="I am a smart calculator", width=20, padx=3)
l1.place(x=122, y=10)
l2 = Label(root, text="My name is ChatGPT", padx=3)
l2.place(x=150, y=40)
l3 = Label(root, text="What can I help you with?", padx=3)
l3.place(x=130, y=70)

textin = StringVar(value="Try typing 'add 5 and 3'")  # Placeholder Text
e1 = Entry(root, width=25, font=('calibri', 16), textvar=textin)
e1.place(x=100, y=110)

# To clear the placeholder text when the user clicks on the entry
def clear_placeholder(event):
    if textin.get() == "Try typing 'add 5 and 3'":
        textin.set('')
        e1.config(fg='black')

# Resetting the placeholder text if user didn't type anything
def reset_placeholder(event):
    if textin.get() == '':
        textin.set("Try typing 'add 5 and 3'")
        e1.config(fg='grey')

e1.bind("<FocusIn>", clear_placeholder)
e1.bind("<FocusOut>", reset_placeholder)
e1.config(fg='grey')

b1 = Button(root, text="Result", command=compute)
b1.place(x=190, y=160)

list = Listbox(root, width=20, height=3, font=('calibri', 16))
list.place(x=130, y=220)

def show_instructions():
    """Show a popup window with instructions."""
    instructions = """
    Supported Operations:
    - Add: 'add 5 and 3', '5 plus 3', 'sum of 5 and 3'
    - Subtract: 'subtract 7 from 10', '7 minus 10'
    - Multiply: '5 multiplied by 3', 'product of 5 and 3'
    - Divide: '8 divided by 2', 'division of 8 by 2'
    - Modulus: '8 mod 2', '8 remainder 2'
    - LCM: 'LCM of 4 and 6'
    - HCF: 'HCF of 4 and 6'

    Note: Ensure you provide two numbers for operations.
    """
    tmsg.showinfo("Instructions", instructions)

b2 = Button(root, text="Help", command=show_instructions)
b2.place(x=110, y=160)

root.mainloop()
