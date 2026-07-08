# make a real life calculator 

import tkinter as tk

window = tk.Tk()

window.title("calculator")

window.geometry("400x400")

entry = tk.Entry(window)

entry.grid(row=0,column=4)


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


buttonadd = tk.Button(window,text = "+",command=lambda:click("+"),width=7,height=3)

buttonadd.grid(row=1 , column=1)



buttonsub = tk.Button(window,text = "-",command=lambda:click("-"),width=7,height=3)

buttonsub.grid(row=1 ,column=2)



buttonmult = tk.Button(window,text = "*",command=lambda:click("*"),width=7,height=3)

buttonmult.grid(row= 1, column=3)
    
buttondiv = tk.Button(window,text = "/",command=lambda:click("/"),width=7,height=3)

buttondiv.grid(row=2 , column=4)

buttoneq = tk.Button(window,text = "=",command=equal,width=7,height=3)

buttoneq.grid(row=4 , column=4)

buttoncl = tk.Button(window,text = "c",command=clear,width=7,height=3)

buttoncl.grid(row=3 , column=4)

button0 = tk.Button(window,text = "0",command=lambda:click("0"),width=7,height=3)

button0.grid(row=5 , column=2)

button1 = tk.Button(window,text = "1",command=lambda:click("1"),width=7,height=3)

button1.grid(row=2 , column=1)

button2 = tk.Button(window,text = "2",command=lambda:click("2"),width=7,height=3)

button2.grid(row=2 , column=2)

button3 = tk.Button(window,text = "3",command=lambda:click("3"),width=7,height=3)

button3.grid(row=2 , column=3)

button4 = tk.Button(window,text = "4",command=lambda:click("4"),width=7,height=3)

button4.grid(row=3 , column=1)

button5 = tk.Button(window,text = "5",command=lambda:click("5"),width=7,height=3)

button5.grid(row=3 , column=2)

button6 = tk.Button(window,text = "6",command=lambda:click("6"),width=7,height=3)

button6.grid(row=3 , column=3)

button7 = tk.Button(window,text = "7",command=lambda:click("7"),width=7,height=3)

button7.grid(row=4 , column=1)

button8 = tk.Button(window,text = "8",command=lambda:click("8"),width=7,height=3)

button8.grid(row=4 , column=2)

button9 = tk.Button(window,text = "9",command=lambda:click("9"),width=7,height=3)

button9.grid(row=4 , column=3)









window.mainloop()
