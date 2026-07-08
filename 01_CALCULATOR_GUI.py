# make a real life calculator 

import tkinter as tk

window = tk.Tk()

window.title("calculator")

window.geometry("400x400")

entry = tk.Entry(window)

entry.grid(row=0,column=4)

# button.pack()   you can't use both grid and pack

def click(value):
    entry.insert(tk.END,value)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END,"error")


button1 = tk.Button(window,text = "+",command=lambda:click("+"),width=7,height=3)

button1.grid(row=1 , column=1)



button2 = tk.Button(window,text = "-",command=lambda:click("-"),width=7,height=3)

button2.grid(row=1 ,column=2)



button3 = tk.Button(window,text = "*",command=lambda:click("*"),width=7,height=3)

button3.grid(row= 1, column=3)
    
button4 = tk.Button(window,text = "/",command=lambda:click("/"),width=7,height=3)

button4.grid(row=2 , column=4)

button5 = tk.Button(window,text = "=",command=equal,width=7,height=3)

button5.grid(row=4 , column=4)

button6 = tk.Button(window,text = "c",command=clear,width=7,height=3)

button6.grid(row=3 , column=4)

button7 = tk.Button(window,text = "0",command=lambda:click("0"),width=7,height=3)

button7.grid(row=5 , column=2)

button8 = tk.Button(window,text = "1",command=lambda:click("1"),width=7,height=3)

button8.grid(row=2 , column=1)

button9 = tk.Button(window,text = "2",command=lambda:click("2"),width=7,height=3)

button9.grid(row=2 , column=2)

button10 = tk.Button(window,text = "3",command=lambda:click("3"),width=7,height=3)

button10.grid(row=2 , column=3)

button11 = tk.Button(window,text = "4",command=lambda:click("4"),width=7,height=3)

button11.grid(row=3 , column=1)

button12 = tk.Button(window,text = "5",command=lambda:click("5"),width=7,height=3)

button12.grid(row=3 , column=2)

button13 = tk.Button(window,text = "6",command=lambda:click("6"),width=7,height=3)

button13.grid(row=3 , column=3)

button14 = tk.Button(window,text = "7",command=lambda:click("7"),width=7,height=3)

button14.grid(row=4 , column=1)

button15 = tk.Button(window,text = "8",command=lambda:click("8"),width=7,height=3)

button15.grid(row=4 , column=2)

button16 = tk.Button(window,text = "9",command=lambda:click("9"),width=7,height=3)

button16.grid(row=4 , column=3)









window.mainloop()