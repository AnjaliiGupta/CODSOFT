#--------------------------------------------GUI-based to do list application--------------------------
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List ")


#defining the function to add tasks to the list  
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


# defining the function to delete a task from the list 
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


# defining the function to update the list  
def update_task():
    try:
        task_index = listbox_tasks.curselection()
        if task_index:
            new_task = entry_task.get()
            if new_task:
              listbox_tasks.delete(task_index)
              listbox_tasks.insert(task_index, new_task)
              entry_task.delete(0, tkinter.END)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks")


# function to close the application  
def quit_app():
   root.quit()



#layout of the application
# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()


#  place the list box in the application
listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50, bg="pink")
listbox_tasks.pack(side=tkinter.LEFT)


# adding scrollbar in the application
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50,)
entry_task.pack()


# adding buttons to the application 
button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task,  bg="powderblue")
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task,  bg="powderblue")
button_delete_task.pack()

button_update_task = tkinter.Button(root, text="Update task", width=48, command=update_task,  bg="powderblue")
button_update_task.pack()

button_quit_app = tkinter.Button(root, text="Quit app", width=48, command=quit_app,  bg="powderblue")
button_quit_app.pack()

root.mainloop()