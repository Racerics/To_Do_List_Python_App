# Import required libraries
from tkinter import Tk, Frame, Label, Listbox, Button, Entry, END, LEFT, TOP, X, BOTH, GROOVE

# Initialize an empty list for tasks
tasks = []

def add_task():
    """
    This function adds a task to the task list when the "Add Task" button is clicked.
    It gets the task from the task_entry widget, adds it to the tasks list as a dictionary, and inserts it into the task_list widget.
    The inserted task is set to green color to indicate that it has been added successfully.
    Then, the task_entry widget is cleared.
    """
    task = task_entry.get()
    tasks.append({'task': task, 'completed': False})
    task_list.insert(END, task)  # set color to green
    task_list.itemconfigure(END, fg='#008000')
    task_entry.delete(0, END)

def complete_task():
    """
    This function marks the selected task(s) as completed in the tasks list when the "Complete Task" button is clicked.
    It gets the selected task from the task_list widget, marks it as completed in the tasks list, and sets its color to red in the task_list widget.
    """
    selected_tasks = task_list.curselection()
    for task_index in selected_tasks:
        task = tasks[task_index]
        task['completed'] = True
        task_list.itemconfig(task_index, fg='#ff0000')  # set color to red
        task_list.selection_clear(0, END)

def delete_task():
    """
    This function deletes the selected task(s) from the tasks list when the "Delete Task" button is clicked.
    It gets the selected task from the task_list widget, deletes it from the tasks list, and removes it from the task_list widget.
    """
    selected_tasks = task_list.curselection()
    for task_index in reversed(selected_tasks):
        task_list.delete(task_index)
        tasks.pop(task_index)

def show_tasks():
    """
    This function displays the current list of tasks in the task_list widget when the "Show Tasks" button is clicked.
    It first clears the task_list widget and then inserts each task from the tasks list into the widget.
    If a task is completed, a check mark is displayed next to it, otherwise a space is displayed.
    """
    task_list.delete(0, END)
    for i, task in enumerate(tasks):
        status = ' ' if not task['completed'] else '✓'
        task_list.insert(END, f"{i+1}.{task['task']}[{status}]")

# Main Window
root = Tk()
root.title('To-Do List')
root.geometry('600x650')
root.configure(bg='#ffffff')

# Title
title_label = Label(root, text='To-Do List', font=('Arial', 24), bg='#ffffff', fg='#0375b4')
title_label.pack(pady=10)

# Task Entry
task_entry_frame = Frame(root, bg='#ffffff')
task_entry_label = Label(task_entry_frame, text='Add a task:', font=('Arial', 12), bg='#ffffff', fg='#000000')
task_entry_label.pack(side=LEFT, padx=(10,0))
task_entry = Entry(task_entry_frame, width=30, font=('Arial', 12), bd=2, relief=GROOVE)
task_entry.pack(side=LEFT, padx=(10,0), ipady=5, expand=True, fill=X)
task_entry_frame.pack(pady=10, padx=10, fill=X)

# Add Button
add_button = Button(root, text='Add', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=GROOVE, command=add_task)
add_button.pack(side=TOP, padx=10, pady=(0,10), fill=X)

# Complete Button
complete_button = Button(root, text='Complete', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=GROOVE, command=complete_task)
complete_button.pack(side=TOP, padx=10, pady=(0,10), fill=X)

# Delete Button
delete_button = Button(root, text='Delete', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=GROOVE, command=delete_task)
delete_button.pack(side=TOP, padx=10, pady=(0,10), fill=X)

# Task List
task_list_frame = Frame(root, bg='#ffffff')
task_list_label = Label(task_list_frame, text='Tasks:', font=('Arial', 12), bg='#ffffff', fg='#000000')
task_list_label.pack(side=LEFT, padx=(10,0))
task_list = Listbox(task_list_frame, width=40, height=15, font=('Arial', 12), bd=2, relief=GROOVE)
task_list.pack(side=LEFT, padx=(10,0), pady=10, expand=True, fill=BOTH)
task_list_frame.pack(pady=10, padx=10, expand=True, fill=BOTH)

# Calculate the middle coordinates of the window
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
middle_x = int(root.winfo_screenwidth()/2 - window_width/2)
middle_y = int(root.winfo_screenheight()/2 - window_height/2)

# Show Button
show_button = Button(root, text='Show Tasks', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=GROOVE, command=show_tasks)
show_button.place(x=middle_x, y=middle_y)
show_button.pack(padx=(10,0), pady=10)

root.mainloop()