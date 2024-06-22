import tkinter as tk

calculate = " "
def add_1(symbol):
    global calculate
    calculate += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculate)

def evaluatec():
    global calculate
    try:
        calculate=str(eval(calculate))
        
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculate)
    except:
        clearbutton()
        text_result.insert(1.0,"Error")
def clearbutton():
    global calculate
    calculate = ""
    text_result.delete(1.0,"end")

root = tk.Tk()
root.geometry("420x400")

text_result = tk.Text(root, height = 2,width=24,font=("Arial",24),bg='light green',fg='black')
text_result.grid(columnspan = 5)

btn1 = tk.Button(root, text ="1",command = lambda: add_1(1),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn1.grid(row =2,column=1)
btn2 = tk.Button(root, text ="2",command = lambda: add_1(2),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn2.grid(row =2,column=2)
btn3 = tk.Button(root, text ="3",command = lambda: add_1(3),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn3.grid(row =2,column=3)
btn4 = tk.Button(root, text ="4",command = lambda: add_1(4),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn4.grid(row =3,column=1)
btn5 = tk.Button(root, text ="5",command = lambda: add_1(5),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn5.grid(row =3,column=2)
btn6 = tk.Button(root, text ="6",command = lambda: add_1(6),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn6.grid(row =3,column=3)
btn7 = tk.Button(root, text ="7",command = lambda: add_1(7),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn7.grid(row =4,column=1)
btn8 = tk.Button(root, text ="8",command = lambda: add_1(8),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn8.grid(row =4,column=2)
btn9 = tk.Button(root, text ="9",command = lambda: add_1(9),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn9.grid(row =4,column=3)
btn0 = tk.Button(root, text ="0",command = lambda: add_1(0),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btn0.grid(row =5,column=2)
btnplus = tk.Button(root, text ="+",command = lambda: add_1("+"),width =8,font = ("Arial",16),fg='black',bg='pink')
btnplus.grid(row =2,column=4)
btnminus = tk.Button(root, text ="-",command = lambda: add_1("-"),width =8,font = ("Arial",16),fg='black',bg='pink')
btnminus.grid(row =3,column=4)
btnmul = tk.Button(root, text ="*",command = lambda: add_1("*"),width =8,font = ("Arial",16),fg='black',bg='pink')
btnmul.grid(row =4,column=4)
btndiv = tk.Button(root, text ="/",command = lambda: add_1("/"),width =8,font = ("Arial",16),fg='black',bg='pink')
btndiv.grid(row =5,column=4)

btnopen = tk.Button(root, text ="(",command = lambda: add_1("("),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btnopen.grid(row =5,column=1)
btnclose = tk.Button(root, text =")",command = lambda: add_1(")"),width =8,font = ("Arial",16),fg='black',bg='skyblue')
btnclose.grid(row =5,column=3)
btnclear = tk.Button(root, text ="AC",command =  clearbutton,width =17,font = ("Arial",16),fg='black',bg='yellow')
btnclear.grid(row =6,column=1,columnspan = 2)
btneq = tk.Button(root, text ="=",command =evaluatec,width =17,font = ("Arial",16),fg='black',bg='yellow')
btneq.grid(row =6,column=3,columnspan = 2)
root.mainloop()
