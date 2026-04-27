import tkinter as tk

tasks = []

def refresh_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        display = t["task"] + (" ✔" if t["done"] else "")
        listbox.insert(tk.END, display)

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        entry.delete(0, tk.END)
        refresh_listbox()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        refresh_listbox()

def mark_complete():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True
        refresh_listbox()

root = tk.Tk()
root.title("Task Manager")
root.geometry("400x500")

# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

complete_btn = tk.Button(root, text="Mark Complete", command=mark_complete)
complete_btn.pack(pady=5)

# Task display
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=20)

root.mainloop()