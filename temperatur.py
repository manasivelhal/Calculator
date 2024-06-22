import tkinter as tk
from tkinter import messagebox
from functools import partial

temp = "Celsius"

def store_temp(set_temp):
    global temp_val
    temp_val = set_temp
    
def call_convert(rlabel1, inputn):
    temp = inputn.get()
    
    if temp_val == 'Celsius':
        
        f = float((float(temp)* 9/5)+32)
        rlabel1.config(text ="%.1f Farenheit" % f,font=('Arial',36))
        messagebox.showinfo("Temperature Converter","Successfully converted to Farenheit ")
        
    if temp_val =='Farenheit':
        
        c= float((float(temp)-32)*5/9)
        rlabel1.config(text = "%.1f Celsius" %c,font=('Arial',36))
        messagebox.showinfo("Temperature Converter","Successfully converted to Celsius")
        
    return

root = tk.Tk()

root.geometry("550x250")
root.title('Temperature Converter')

root.grid_columnconfigure(1,weight =1)        
root.grid_rowconfigure(1,weight =1)

inputNumber = tk.StringVar()
var=tk.StringVar()

input_label = tk.Label(root,text = "Enter temperature : ",font = ('Arial',16))
input_entry = tk.Entry(root,textvariable = inputNumber,font=('Arial',16))
input_label.grid(row=1)
input_entry.grid(row=1,column=1)
result_label = tk.Label(root)
result_label.grid(row=4,column =1)

dropDownList = ["Celsius","Farenheit"]
drop_down = tk.OptionMenu(root,var,*dropDownList,command = store_temp)

var.set(dropDownList[0])
drop_down.grid(row =3, column=1)

call_convert = partial(call_convert,result_label,inputNumber)
result_button = tk.Button(root,text="Convert",command = call_convert,font=('Arial',18),bg='light green',fg='black')
result_button.grid(row=7,column=1)

root.mainloop()