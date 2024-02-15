"""from tkinter import *

app=Tk()
app.title("my first python gui App")
app.geometry("700x300")
app.config(bg="white")

def additon():
    a=10
    b=10
    c=(a+b)
    ibltittle.config(text=c,fg="red")


ibltittle=Label(app,text="Arithmetic operators")
ibltittle.grid(row=0,column=1,padx=40,pady=40)

inputbox=Entry(app,width=60)
inputbox.grid(row=2,column=2)

ibltittle=Label(app,text="Arithmetic Operation")
ibltittle.grid(row=1,column=1,padx=30,pady=30)

inputbox1=Entry(app,width=60)
inputbox1.grid(row=1,column=2)

clickme=Button(app,text="addition",command=additon,)
clickme.grid(row=2,column=8,padx=40,pady=40)

app.mainloop()


from tkinter import *

dows=Tk()

dows.title("opetaors")
dows.geometry("500x500")"""


import tkinter as tk

def on_submit():
    user_input = entry.get()
    result_label.config(text=f"i am: {user_input}")

# Create the main window
window = tk.Tk()
window.title("Input GUI")
window.geometry("1366x768")
window.config(bg="red")

# Create an Entry widget for text input
entry = tk.Entry(window)
entry.pack()

# Create a button to submit the input
submit_button = tk.Button(window, text="Submit", command=on_submit,font="bold",fg="pink")
submit_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")

result_label.pack()

# Run the main loop
window.mainloop()


