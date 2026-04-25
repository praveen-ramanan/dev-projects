import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

def mark_complete():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = True

        # Update display
        listbox.delete(index)
        listbox.insert(index, tasks[index]["task"] + " ✔")

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