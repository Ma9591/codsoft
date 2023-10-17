import tkinter as tk

app = tk.Tk()
app.title("Simple Calculator")

entry = tk.Entry(app, width=50)
entry.grid(row=0, column=0, columnspan=6)




def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    if button_text == '=':
        button = tk.Button(app, text=button_text, command=calculate,width=8, height=2)
    elif button_text == 'C':
        button = tk.Button(app, text=button_text, command=clear,width=8, height=2)
    else:
        button = tk.Button(app, text=button_text, command=lambda text=button_text: button_click(text),width=8, height=2)



    button.grid(row=row, column=col, padx=1, pady=1)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()