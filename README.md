## Command-line to-do app.

### Requirement:
Python 3.x.x

### Specification:

1. Runs in the console
    `python task.py`

2. The app reads and writes to a task.txt file.

    The application opens the files task.txt and completed.txt from where the app is run, and not where the app is located.

    Each task occupies a single line in this file. Each line in the file is in this format :

   ```
   p task
   ```
   
   where `p` is the priority ( priority will be a number) and `task` is the task description.

   > Priority denotes how important a task is, if it is a high priority task, it should be completed earlier. Priority is denoted using an integer, the lower the number, the higher the priority.

   Here is an example file that has 2 items.

   ```
   1 Buy milk
   2 Complete the project
   ```


3. Completed task are writted to a completed.txt file. Each task occupies a single line in this file. Each line in the file should be in this format :

   ```
   task
   ```

   where task is the task description.

   Here is an example file that has 2 items.

   ```
   Buy milk
   Complete the project
   ```


4. Priority can be any integer _greater than_ or _equal to_ 0. 0 being the highest priority

5. If two task have the same priority, the task that was added first is displayed first.

6. The files always are in sorted order of the priority, ie, the task with the highest priority should be first item in the file.

### Usage:


#### 1. Help-

Executing the command without any arguments, or with a single argument help prints the CLI usage.

```
task.py help
Usage :-
task.py add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
task.py ls                   # Show incomplete priority list items sorted by priority in ascending order
task.py del INDEX            # Delete the incomplete item with the given index
task.py done INDEX           # Mark the incomplete item with the given index as complete
task.py help                 # Show usage
task.py report               # Statistics
```

#### 2. List all pending items-

Use the ls command to see all the items that are not yet complete, in ascending order of priority.

Every item should be printed on a new line. with the following format

```
[index] [task] [priority]
```

Example:

```
 task.py ls
1. change light bulb [2]
2. water the plants [5]
```

index starts from 1, this is used to identify a particular task to complete or delete it.

#### 3. Add a new item-

Use the add command. The text of the task should be enclosed within double quotes (otherwise only the first word is considered as the item text, and the remaining words are treated as different arguments).

```
 task.py add 5 "the thing i need to do"
Added task: "the thing i need to do" with priority 5
```

#### 4. Delete an item-

Use the del command to remove an item by its index.

```
 task.py del 3
Deleted item with index 3
```

Attempting to delete a non-existent item should display an error message.

```
 task.py del 5
Error: item with index 5 does not exist. Nothing deleted.
```

#### 5. Mark a task as completed-

Use the done command to mark an item as completed by its index.

```
 task.py done 1
Marked item as done.
```

Attempting to mark a non-existed item as completed will display an error message.

```
 task.py done 5
Error: no incomplete item with index 5 exists.
```

#### 6. Generate a report-

Show the number of complete and incomplete items in the list. and the complete and incomplete items grouped together.

```
 task.py report
Pending : 2
1. this is a pending task [1]
2. this is a pending task with priority [4]

Completed : 3
1. completed task
2. another completed task
3. yet another completed task
```
