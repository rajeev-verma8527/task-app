import os
import sys

tasks = []  # list to store and manage uncompleted tasks
# list of tuples -> [ (p,task),... ]
args = None
task_path = None  # task text file path
completed_path = None  # competed text file path



def help():
    t = """Usage :
    task.py add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list
    task.py ls                   # Show incomplete priority list items sorted by priority in ascending order
    task.py del INDEX            # Delete the incomplete item with the given index
    task.py done INDEX           # Mark the incomplete item with the given index as complete
    task.py help                 # Show usage
    task.py report               # Statistics"""
    print(t)


def import_tasks():
    # read from task.txt and store in global "tasks" list
    with open(task_path, 'r') as file:
        for line in file.readlines():
            temp = line.split(maxsplit=1)
            tasks.append((int(temp[0]), temp[1].strip()))


def save_tasks():
    # updates task.txt from global "tasks" list
    with open(task_path, 'w') as file:
        for t in tasks:
            file.write(" ".join(map(str, t)) + "\n")


def check_files():
    # create files if does not exists
    if not os.path.exists(task_path):
        open(task_path, "w").close()
    if not os.path.exists(completed_path):
        open(completed_path, "w").close()


def add(priority, task):
    # store (p,task) tuple in 'tasks' list; sort by priority and save
    tasks.append((priority, task))
    tasks.sort(key=lambda x: x[0])
    save_tasks()
    print(f"Added task: \"{task}\" with priority {priority}")


def ls():
    if len(tasks) == 0:
        print("There are no pending tasks!")
        return
    for index, t in enumerate(tasks, start=1):
        print(f"{index}. {t[1]} [{t[0]}]")


def report():
    print(f"Pending : {len(tasks)}")
    ls()

    with open(completed_path, 'r') as file:
        completed = file.readlines().copy()

    print(f"\nCompleted : {len(completed)}")
    for index, t in enumerate(completed, start=1):
        print(f"{index}. {t.strip()}")


def delete(position):
    index = position - 1
    if index not in range(len(tasks)):
        print(f"Error: task with index #{position} does not exist. Nothing deleted.")
        return

    del tasks[index]
    save_tasks()
    print(f"Deleted task #{position}")


def done(position):
    # remove from global "tasks" list; update task.txt and completed.txt
    index = position - 1
    if index not in range(len(tasks)):
        print(f"Error: no incomplete item with index #{position} exists.")
        return
    task_name = tasks.pop(index)[1]
    save_tasks()

    with open(completed_path, "a") as file:
        file.write(task_name + "\n")

    print("Marked item as done.")


def main():
    if len(args) == 0:
        help()
    elif args[0] == "help":
        help()
    elif args[0] == 'ls':
        ls()
    elif args[0] == "report":
        report()
    elif args[0] == 'del':
        if len(args) != 2:
            print("Error: Missing NUMBER for deleting tasks.")
            return
        delete(int(args[1]))

    elif args[0] == "done":
        if len(args) != 2:
            print("Error: Missing NUMBER for marking tasks as done.")
            return
        done(int(args[1]))
    elif args[0] == 'add':
        if len(args) < 3:
            print("Error: Missing tasks string. Nothing added!")
            return
        try:
            add(int(args[1]), " ".join(args[2:]))
        except:
            print("Error: Incorrect Input")
    else:
        print("Invalid input.")
        help()
        
if __name__ == "__main__":
    args = sys.argv[1:]
    task_path = os.path.join(os.getcwd(), "task.txt")
    completed_path = os.path.join(os.getcwd(), "completed.txt")
    check_files()
    import_tasks()    
    main()