import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

app = tk.Tk()
app.title("To-Do List")

entry = tk.Entry(app, width=40)
entry.pack()

add_button = tk.Button(app, text="Add Task", command=add_task,width=15, height=2)
add_button.pack()

remove_button = tk.Button(app, text="Remove Task", command=remove_task,width=15, height=2)
remove_button.pack()

task_list = tk.Listbox(app, width=60)
task_list.pack()

app.mainloop()
