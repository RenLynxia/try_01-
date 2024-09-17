import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, task_index):
        try:
            del self.tasks[task_index]
        except IndexError:
            messagebox.showerror("Error", "Invalid task index.")

    def mark_task_as_completed(self, task_index):
        try:
            self.tasks[task_index].mark_as_completed()
        except IndexError:
            messagebox.showerror("Error", "Invalid task index.")

    def display_tasks(self):
        return "\n".join([str(task) for task in self.tasks])


class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.todo_list = ToDoList()

        self.task_description_label = tk.Label(root, text="Task Description:")
        self.task_description_label.pack()

        self.task_description_entry = tk.Entry(root, width=50)
        self.task_description_entry.pack()

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.remove_task_label = tk.Label(root, text="Task Index to Remove:")
        self.remove_task_label.pack()

        self.remove_task_entry = tk.Entry(root, width=10)
        self.remove_task_entry.pack()

        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack()

        self.mark_task_as_completed_label = tk.Label(root, text="Task Index to Mark as Completed:")
        self.mark_task_as_completed_label.pack()

        self.mark_task_as_completed_entry = tk.Entry(root, width=10)
        self.mark_task_as_completed_entry.pack()

        self.mark_task_as_completed_button = tk.Button(root, text="Mark Task as Completed", command=self.mark_task_as_completed)
        self.mark_task_as_completed_button.pack()

        self.display_tasks_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        self.display_tasks_button.pack()

        self.tasks_text = tk.Text(root, height=10, width=50)
        self.tasks_text.pack()

    def add_task(self):
        description = self.task_description_entry.get()
        self.todo_list.add_task(description)
        self.task_description_entry.delete(0, tk.END)

    def remove_task(self):
        task_index = int(self.remove_task_entry.get()) - 1
        self.todo_list.remove_task(task_index)
        self.remove_task_entry.delete(0, tk.END)

    def mark_task_as_completed(self):
        task_index = int(self.mark_task_as_completed_entry.get()) - 1
        self.todo_list.mark_task_as_completed(task_index)
        self.mark_task_as_completed_entry.delete(0, tk.END)

    def display_tasks(self):
        self.tasks_text.delete(1.0, tk.END)
        self.tasks_text.insert(tk.END, self.todo_list.display_tasks())


if __name__ == "__main__":
    root = tk.Tk()
    todo_list_gui = ToDoListGUI(root)
    root.mainloop()
