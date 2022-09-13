# ------------------------------------------------------------------------ #
# Title: Main
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Stephanie Tarczynski, 12/14/2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
lstTable = []
# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

while (True):
    # Show user a menu of option
    Eio.print_menu_items()
    # Get user's menu option choice
    choice = Eio.input_menu_options()
    # Show user current data in the list of employee objects
    if choice.strip() == '1':
        Eio.print_current_list_items(lstTable)
        continue
    # Let user add data to the list of employee objects
    elif choice.strip() == '2':
        emp = Eio.input_employee_data()
        lstTable.append(emp)
        continue
    # let user save current data to file
    elif choice.strip() == '3':
        Fp.save_data_to_file("EmployeeData.txt", lstTable)
        print("Data saved.")
    # Let user exit program
    elif choice.strip() == '4':
        print("Exiting program.")
        break
    else:
        print ("Invalid Selection.")
        continue

