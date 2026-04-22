import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")

# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

# List to display tasks
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=20)

root.mainloop()