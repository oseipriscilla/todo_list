tasks =[]

# Define a function to clear the screen
import os
def clear():
    os.system('cls')

#Define a function display Menu
def display_menu():
    print("\nPlease choose from the following options:")
    print("Select: \n\t1. Add tasks")
    print("\t2. View tasks") 
    print("\t3. Update tasks")  
    print("\t4. Delete tasks")  
    print("\t5. Exit")  

# Define a function to add a task
def add_task():
    clear()
    print(f"{bold_blue("ADD A TASK:\n=========")}")
    end_format()
    user_task = input(f"Please Enter your task:\n{bold_green("-->: ")}")
    end_format()
    tasks.append(user_task)
    print("Task added successfully\n")
    input("Press enter to continue ...")
    clear()

# Define a function to view tasks
def view_tasks():
    clear()
    print(f"{bold_blue("PENDING TASKS:\n==============")}")
    end_format()
    if not tasks:
        print("You don't have any tasks in your To-Do List! Please add a task")
    else:
        # display list with numbers
        print("Your tasks are:")
        for count, task in enumerate(tasks, 1):
            print(f"{count}. {sentence_case(task)}")
        print(f"{bold_blue("`````````````````````````````````````````````````````")}")
        end_format()

def exit_program():
    exit(1)

# Define a function update tasks
def update_tasks():
    # Display all available tasks
    if not tasks:
        print("You don't have any task in your To-Do List to update.")
        input("Press enter to continue ...")
        clear()
    else:
        view_tasks()
        input("Press Enter to edit a task ...")
        print(f"\t{bold_blue("\n\tUPDATE TASKS\n\t============")}")
        end_format()
        task_number = int(input(f"\tEnter number corresponding to the task you want to update:\n\t\t{bold_green("-->: ")}"))
        end_format()
        if 1 <= task_number <= len(tasks):
            updated_task = input("\tEnter a replacement for selected task: ")
            tasks[task_number - 1] = updated_task
        else:
            print("You must add a task before performing an update function")
            add_task()

# Define a function to delete tasks
def delete_tasks():
    # Check if there is a task in the To-Do List
    if not tasks:
        print("There are no tasks in your To-Do List. You can only perform this action after adding a task.\n")
        input("Press enter to continue ...")
        clear()
    else:
        # Display the tasks in the To-Do List
        view_tasks()
        print(f"\t{bold_blue("\nDELETE TASKS:\n=============")}")
        end_format()
        delete_type = int(input(f"Choose delete type:\n1. Delete a task\n2. Delete all tasks\n\t{bold_green("-->: ")}"))
        end_format()
        if delete_type == 1:
            clear()
            print(f"{bold_blue("Delete a task:")}")
            end_format()
            view_tasks()
            task_number = int(input(f"Enter a number that corresponds with the task you want to delete.\n\t{bold_green("-->: ")}"))
            end_format()
            if 1 <= task_number <= len(tasks):
                print(f"\"{sentence_case(tasks[task_number - 1])}\" was deleted successfully!")
                tasks.pop(task_number - 1)

            else:
                print("Invalid entry")
        elif delete_type == 2:
            clear()
            print(f"{bold_blue("Delete all tasks:")}")
            end_format()
            # Delete all tasks
            tasks.clear()
            print("All tasks have been deleted successfully!")
        else:
            print("Please enter a valid number")






# Define a function to format sentences in a sentence-case
def sentence_case(sentence):
    words = sentence.split(". ")
    new_sentence = ". ".join([word.capitalize() for word in words])
    return new_sentence

# Define a function to format a text in green and bold
def bold_green(text):
    return(f"\033[m\033[92m{text}")

# Define a function to format a text in blue and bold
def bold_blue(text):
    return(f"\033[m\033[94m{text}")

# Define a function to clear format
def end_format():
    print("\033[0m")
