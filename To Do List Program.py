import time
import json
import os
from termcolor import colored as cl
from pyfiglet import figlet_format as ff 

# Deleting Screen

def delete_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")

# Deleting Line                                                                                   

def delete_line():
    print("\033[F", end="")
    print("\033[K", end="")
    
# To Do List App

delete_screen()
middle_T = ("\t\t\t\t\t\t\t\t\t\t")
middle_N = ("\n\n\n\n\n\n\n\n")
Tasks = {}
title_messege = ("\t\tMAIN MENU\n") # First Messege That Appears To The User

class ToDo:
    
    # Creating Tasks
    
    def __init__(self, name, marked=cl("UnDone", color = "red")):
        self.name = name
        self.marked = marked
        
def save_tasks():
    
    # Saving Tasks everytime the user choose 'Save And Exit'
    
    '''Save Tasks'''
    with open('tasks.json', 'w') as file:
        json.dump(Tasks, file)

def load_tasks():
    
    # Load the saved data everytime the user opens the program
    
    '''Load Tasks'''
    global Tasks
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            Tasks = json.load(file)
            
def add_task():
    '''Add Tasks To The To Do List'''
    delete_screen()
    
    # Adding Tasks
    
    while True:
        Add_Task = input("Enter Task (or Press 'Enter' to go back): ").title()
        
        # If User pressed enter and didn't add a task
        
        if not Add_Task:
            delete_screen()
            break
            
        # Adding The Task That The User Added    
            
        else:    
            task = ToDo(Add_Task,marked=cl("UnDone", color = "red"))
            Tasks[task.name] = {'Name': task.name,
                                'Marked': task.marked}
            new_task = input("Do You Want To Add Another Task? (y/n): ").lower()
            if new_task == "y" or new_task == "yes":
                delete_screen()
            else:
                delete_screen()
                print ("\nTasks Added Successfully..\n")
                time.sleep(1)
                delete_screen()
                break

def mark_task():
    '''Mark Tasks'''
    delete_screen()
    
    # If user chose 'Mark Tasks' and there is no tasks
    
    if Tasks == {}:
        print ('No Tasks Yet...')
        input ("\nPress 'Enter' to go back to the main menu.. ")
        delete_screen()
    else:
        while True:
            
            # Showing Tasks to make it easy for the user to mark tasks
            
            x = 0
            for key in Tasks: 
                x += 1   
                print (f"{x}. {Tasks[key]["Name"]} ({Tasks[key]['Marked']})")
                print ("=" * 25)
            MarkTask = input("\nEnter Task To Complete (or press 'Enter' to go back): ").title()
            
            # If the user chose 'Mark Tasks' accedintely and don't want to mark any thing he can go back   
            
            if not MarkTask:
                delete_screen()
                break  
            
            # If he chose a task to mark
                      
            elif MarkTask in Tasks:
                Tasks[MarkTask]['Marked'] = cl("Done", color = "green")
                Another_Mark_Task = input("Do You Want To Complete Another Task? (y/n): ").lower()
                if Another_Mark_Task == "y" or Another_Mark_Task == "yes":
                    delete_screen()
                else:
                    delete_screen()
                    break   
                
            # If the task he chose doesn't exist    
                         
            else:
                input ("\nInvalid Input. Press 'Enter' to try again ")
                delete_screen()
                
def view_tasks():
    '''View All Tasks'''
    
    # If there is no tasks this messege appear at top
    
    if Tasks == {}:
        print ('\nNo Tasks Yet...')
        
    # Showing all the tasks at the top   
        
    else:
        x = 0
        for key in Tasks: 
            x += 1   
            print (f"{x}. {Tasks[key]["Name"]} ({Tasks[key]['Marked']})")
            print ("=" * 25)
    
def remove_task():
    '''Remove a Task'''
    delete_screen()
    
    # If user chose remove a task and there is no tasks 
    
    if Tasks == {}:
        print ('No Tasks Yet...')
        input ("\nPress 'Enter' to go back to the main menu.. ")
        delete_screen()
    else:
        while True:
            
            # If User finished deleting all tasks and want to delete another one
            
            if Tasks == {}:
                print ('No Tasks to remove...')
                input ("\nPress 'Enter' to go back to the main menu.. ")
                delete_screen()
                break
            
            # Deleting tasks If they Exist            
            
            else:
                view_tasks()
                Task_To_Remove = input("\nEnter the task name to remove (or Press 'Enter' to go back): ").title()
                
                # If the user chose 'Remove a Task' accedintely and don't want to remove any thing he can go back
                
                if not Task_To_Remove:
                    delete_screen()
                    break
                elif Task_To_Remove in Tasks:
                    del Tasks[Task_To_Remove] 
                    new_task = input("Do You Want To Delete Another Task? (y/n): ").lower()
                    if new_task == "y" or new_task == "yes":
                        delete_screen()
                    else:
                        print ("\nTasks Removed successfully...\n")
                        time.sleep(1)
                        delete_screen()
                        break
                else:
                    input ("\nInvaild Task. Press 'Enter' to try again ")
                    delete_screen()
            
def remove_all_tasks():
    '''Removing All Tasks'''
    delete_screen()
    
    # If User chose remove all tasks and there is no tasks 
    
    if Tasks == {}:
        print ('No Tasks To Remove...')
        input ("\nPress 'Enter' to go back to the main menu.. ")
        
    # Deleting all tasks If they exist
    
    else:
        if input("Are You Sure You Want To Delete All Tasks? (y/n): ").lower() == "y":  
            Tasks.clear()
            print ('\nTasks Deleted Successfully...')
            time.sleep(1)
        else: 
            input ("\nPress 'Enter' to go back to the main menu.. ")
    delete_screen()
    
def Exiting():
    '''Exiting And Saving'''
    save_tasks()
    delete_screen()
    color = "white"
    seconds = 7
    print (middle_N)
    
    for x in range(seconds):
        if seconds == 3:
            color ="light_red"
        print(f"{middle_T}Exiting Program..", cl(f"({seconds:02})",color))
        time.sleep(1)
        seconds -= 1
        delete_line()
    delete_screen()
    print (middle_N)
    print (f"{middle_T}** Exited **")
    print (middle_N)
    
load_tasks()

def showing_logo():
    print (cl(ff("To Do List"),color = "light_blue"))
    time.sleep(3)
    delete_screen()
    
showing_logo()
while True:
    # Showing the user the program in a beautiful way

    print (title_messege) 
    view_tasks()
    input ("\nSee Options..")
    delete_line()
    delete_line()
    print (cl("\n1. Add a Task",color = "blue"))
    time.sleep(0.05) 
    print (cl("2. Mark a Task", color = "green"))
    time.sleep(0.05)
    print (cl("3. Remove a Task", color = "red"))
    time.sleep(0.05)
    print (cl("4. Delete All Tasks", color = "red"))
    time.sleep(0.05)
    print (cl("5. Save and Exit", color = "yellow"))
    choice = input("\nEnter your choice (or Press 'Enter' to hide options): ")
    if choice:
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            remove_all_tasks()  
        elif choice == "5":
            Exiting()
            break
        else:
            input ("\nInvalid Input. Press 'Enter' to go back.. ")
            delete_screen()
    else:  
        delete_screen()
print ("test")
