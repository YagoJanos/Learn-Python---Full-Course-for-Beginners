employee_list = open("employees.txt", "a")
# w would overwrite the entire file, but we can also use w to create a new file, we
# just have to put a name of an nonexistent file.

employee_list.write("Toby - Human Resources")

employee_list.write("\nKelly - Customer Service")

employee_list.close()