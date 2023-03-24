import tkinter as tk

class ToDoList(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # initialize the tk attribute
        if master is None:
            self.master = tk.Tk()
        else:
            self.master = master
        self.master.title('To-Do List')
        self.master.geometry('600x650')
        self.master.configure(bg='#ffffff')
        
        # Title
        self.title_label = tk.Label(self.master, text='To-Do List', font=('Arial', 24), bg='#ffffff', fg='#0375b4')
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_entry_frame = tk.Frame(self.master, bg='#ffffff')
        self.task_entry_label = tk.Label(self.task_entry_frame, text='Add a task:', font=('Arial', 12), bg='#ffffff', fg='#000000')
        self.task_entry_label.pack(side=tk.LEFT, padx=(10,0))
        self.task_entry = tk.Entry(self.task_entry_frame, width=30, font=('Arial', 12), bd=2, relief=tk.GROOVE)
        self.task_entry.pack(side=tk.LEFT, padx=(10,0), ipady=5, expand=True, fill=tk.X)
        self.task_entry_frame.pack(pady=10, padx=10, fill=tk.X)

        # Add Button
        self.add_button = tk.Button(self.master, text='Add', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=tk.GROOVE, command=self.add_task)
        self.add_button.pack(side=tk.TOP, padx=10, pady=(0,10), fill=tk.X)

        # Complete Button
        self.complete_button = tk.Button(self.master, text='Complete', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=tk.GROOVE, command=self.complete_task)
        self.complete_button.pack(side=tk.TOP, padx=10, pady=(0,10), fill=tk.X)

        # Delete Button
        self.delete_button = tk.Button(self.master, text='Delete', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=tk.GROOVE, command=self.delete_task)
        self.delete_button.pack(side=tk.TOP, padx=10, pady=(0,10), fill=tk.X)

        # Task List
        self.task_list_frame = tk.Frame(self.master, bg='#ffffff')
        self.task_list_label = tk.Label(self.task_list_frame, text='Tasks:', font=('Arial', 12), bg='#ffffff', fg='#000000')
        self.task_list_label.pack(side=tk.LEFT, padx=(10,0))
        self.task_list = tk.Listbox(self.task_list_frame, width=40, height=15, font=('Arial', 12), bd=2, relief=tk.GROOVE)
        self.task_list.pack(side=tk.LEFT, padx=(10,0), pady=10, expand=True, fill=tk.BOTH)
        self.task_list_frame.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        # Show Button
        self.show_button = tk.Button(self.master, text='Show Tasks', font=('Arial', 12), bg='#0375b4', fg='#ffffff', bd=2, relief=tk.GROOVE, command=self.show_tasks)
        self.show_button.pack(padx=(10,0), pady=10)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append({'task': task, 'completed': False})
        self.task_list.insert(tk.END, task)  # set color to green
        self.task_list.itemconfigure(tk.END, fg='#008000')
        self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_tasks = self.task_list.curselection()
        for task_index in selected_tasks:
            task = self.tasks[task_index]
            task['completed'] = True
            self.task_list.itemconfig(task_index, fg='#ff0000')  # set color to red
            self.task_list.selection_clear(0, tk.END)

    def delete_task(self):
        selected_tasks = self.task_list.curselection()
        for task_index in reversed(selected_tasks):
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)

    def show_tasks(self):
        self.task_list.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = ' ' if not task['completed'] else '✓'
            self.task_list.insert(tk.END, f"{i+1}.{task['task']}[{status}]")

app = ToDoList()
app.master.title('To Do List App')
app.mainloop()