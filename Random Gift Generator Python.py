from tkinter import *
import random

root = Tk()
root.title("What Gift Will You Get?")
root.geometry("400x400")
root.configure(background="pink")

label1 = Label(root, text = "Chocolate, Xbox S, Squishmallow, $1, Gift Card")
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
label2 = Label(root, text = "Gift Number: ")
label2.place(relx=0.5, rely=0.7, anchor=CENTER)
label3 = Label(root, text="Your Gift Will Be: ")
label3.place(relx=0.5, rely=0.8, anchor=CENTER)
list1 = ['Chocolate', 'Xbox S', 'Squishmallow', '$1', 'Gift Card']
print(list1)

def gift():
    random1 = random.randint(0, 4)
    label2["text"] += str(random1)
    print(random1)
    random_no1 = list1[random1]
    print(random_no1)
    label3["text"] += str(random_no1)
    
    
btn1 = Button(root, text="What Gift Will You Get? ", command = gift)
btn1.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()

