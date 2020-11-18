# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# STarczynski, 11.16.2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "C:\\_PythonClass\\Assignment05\\ToDoList.txt"
dataFile = None  # Variable that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

dataFile = open(objFile, "r")
for row in dataFile:
    strData = row.split(":")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()} #unpacking the data to form dictionary rows
    lstTable.append(dicRow) #appending dictionary rows to a table
dataFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task" + " | " + "Priority") #header
        for dicRow in lstTable:
            print(dicRow["Task"] + ": " + dicRow["Priority"]) #printing the values of the dictionary row keys
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a task: ")
        strPriority = input("Enter the priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority} #adding new user input values to the dicRow keys
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input("Enter the task you wish to remove: ").lower().strip()
        i=0
        for dicRow in lstTable:
            if strRemove in dicRow["Task"]:
                print("Task deleted.")
                lstTable.remove(dicRow)
                i+=1
            elif i == 0:
                print("Task not found.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        dataFile = open(objFile, "w")
        for dicRow in lstTable:
            dataFile.write(dicRow["Task"] + ":" + dicRow["Priority"] + "\n")
        dataFile.close()
        print ("Data saved.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print ("Program ended.")
        print("Good luck with your tasks!")
        break  # and Exit the program
