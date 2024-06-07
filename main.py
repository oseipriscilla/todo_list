print ("\nTO-Do List  Application")
print("`````````````````````````")
from program import *
# get user choice 

while True:
#invocation of the menu 
    display_menu()
# accepting user option 
    user_option = int(input(bold_green("-->: ")))
    end_format()
    #check if the user is 1 
    if user_option == 1:
       add_task()
    elif user_option == 2:
        view_tasks() 
    elif user_option == 3:
        update_tasks()
    elif user_option == 4:
        delete_tasks()
    elif user_option == 5:
        exit_program() 
    else:
        print("Invalid option, Kindly Choose from option 1 - 5")


