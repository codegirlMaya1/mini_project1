print(" Welcome to the To-Do List App!")
print("""MENU:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit """ )
task_list = []
# Task 1: Write a function that lets the user add tasks to a to-do-list.
def add_to_list(item):
    task_list.append(item)
    print(f"{item} was added your task list!")
    print(f"You have {len(task_list)} items on your list.")
#Task 2: Include a feature to remove tasks from the to-do-list.
def  remove_item():
    task_list.pop()
print(f"{remove_item} was removed from task list!")
print(f"You have {len(task_list)} tasks on you to-do-list!")
print(f"Enter/Type a new tasks to add to your To-Do-List below")

    
#Task 3: Add a function that prints out the entire list in a formatted way.
# Function to print all out all tasks currently on the to
def see_list():
    print("Current task on my To-Do_List: ")
    for item in task_list:
        print(item)


# Main loop for user interaction
while True:
    new_task = input("> ")

    # If the user inputs 'QUIT', breaks the loop
    if new_task == "5":
        break
    
        

    elif new_task== "4":
        remove_item()
        print ("The last task you added was removed from your to-do-list")
        continue
    
    elif new_task== "3":
        remove_item()
        print ("The last task you added was marked as COMPLETED and removed from your to-do-list")
        continue
    # If the user inputs 'See List',  will show the list
    elif new_task == "2":
        see_list()
        continue
    # Otherwise, will add the tasks to the to-do-list individually
    add_to_list(new_task)
    try:
        ValueError
    except:
        ValueError
    finally:
        see_list()

# Display the final shopping list
see_list()

