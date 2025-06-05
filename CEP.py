# Function to create the system and data files if they don't exist
def create_files_if_needed(fields):
    try:
        with open('system.txt', 'r') as sys_file:
            pass  # File already exists, do nothing
    except FileNotFoundError:
        with open('system.txt', 'w') as sys_file:
            sys_file.write(f"Number of fields: {len(fields)}\n")
            for field in fields:
                sys_file.write(f"Field: {field}, Length: {len(field)}\n")
        print("System file 'system.txt' created.")

    try:
        with open('students.csv', 'r') as csv_file:
            pass  # File already exists, do nothing
    except FileNotFoundError:
        with open('students.csv', 'w') as csv_file:
            csv_file.write(','.join(fields) + '\n')  # Write the header (fields) as the first row
        print("Data file 'students.csv' created.")


# Function to initialize fields based on user input
def initialize_fields():
    fields = []  # List to store the names of the fields
    num_fields = int(input("Enter the number of fields for each student record: "))
    for i in range(num_fields):
        field_name = input(f"Enter the name of field {i + 1}: ")
        fields.append(field_name)  # Add each field name to the list
    return fields


# Function to add a student record to the database
def add_student(fields):
    student_data = []  # List to store student data
    for field in fields:
        value = input(f"Enter {field}: ")  # Prompt user for input for each field
        student_data.append(value)  # Store the input in the list

    # Write the student data to the CSV file
    with open('students.csv', 'a') as csv_file:
        csv_file.write(','.join(student_data) + '\n')  # Write the data to the CSV file

    print("Student added successfully!")  # Confirmation message


# Function to view all student records
# Function to create the system and data files if they don't exist
def create_files_if_needed(fields):
    try:
        with open('system.txt', 'r') as sys_file:
            pass  # File already exists, do nothing
    except FileNotFoundError:
        with open('system.txt', 'w') as sys_file:
            sys_file.write(f"Number of fields: {len(fields)}\n")
            for field in fields:
                sys_file.write(f"Field: {field}, Length: {len(field)}\n")
        print("System file 'system.txt' created.")

    try:
        with open('students.csv', 'r') as csv_file:
            pass  # File already exists, do nothing
    except FileNotFoundError:
        with open('students.csv', 'w') as csv_file:
            csv_file.write(','.join(fields) + '\n')  # Write the header (fields) as the first row
        print("Data file 'students.csv' created.")


# Function to initialize fields based on user input
def initialize_fields():
    fields = []  # List to store the names of the fields
    num_fields = int(input("Enter the number of fields for each student record: "))
    for i in range(num_fields):
        field_name = input(f"Enter the name of field {i + 1}: ")
        fields.append(field_name)  # Add each field name to the list
    return fields


# Function to add a student record to the database
def add_student(fields):
    student_data = []  # List to store student data
    for field in fields:
        value = input(f"Enter {field}: ")  # Prompt user for input for each field
        student_data.append(value)  # Store the input in the list

    # Write the student data to the CSV file
    with open('students.csv', 'a') as csv_file:
        csv_file.write(','.join(student_data) + '\n')  # Write the data to the CSV file

    print("Student added successfully!")  # Confirmation message


# Function to view all student records
def view_students(fields):
    try:
        with open('students.csv', 'r') as csv_file:
            print("\nStudent Records:")

            # Print the header (fields)
            header = "\t".join(field.ljust(15) for field in fields)
            print(header)
            print("-" * len(header))  # Print a separator line

            # Read all lines in the CSV and print each student's data
            for line in csv_file:
                row = line.strip().split(',')  # Split the CSV data by commas
                print("\t".join(value.ljust(15) for value in row))  # Print each student's data
    except FileNotFoundError:
        print("No records found. Add a student first.")  # Handle missing file case


# Function to update a student's information
def update_student(fields):
    name = input(f"Enter the name of the student to update ({fields[0]}): ")  # Use the first field (assumed unique) for lookup
    field_to_update = input("Enter the field to update: ")  # Field to be updated
    if field_to_update not in fields:
        print("Invalid field name.")  # Validate the field name
        return
    new_value = input(f"Enter new value for {field_to_update}: ")  # Get the new value for the field

    updated = False  # Flag to track if update was successful
    records = []  # List to store updated records

    try:
        with open('students.csv', 'r') as csv_file:
            for line in csv_file:
                row = line.strip().split(',')  # Split the CSV data by commas
                student_data = dict(zip(fields, row))  # Map field names to their values

                if student_data[fields[0]] == name:  # Check if the record matches the student name
                    student_data[field_to_update] = new_value  # Update the specified field
                    updated = True  # Flag to indicate that the update was successful

                # Convert the dictionary back to a list
                records.append(list(student_data.values()))

    except FileNotFoundError:
        print("No records found. Add a student first.")
        return

    # Write the updated records back to the CSV file
    with open('students.csv', 'w') as csv_file:
        csv_file.write(','.join(fields) + '\n')  # Write the header again
        for record in records:
            csv_file.write(','.join(record) + '\n')  # Write all updated records

    if updated:
        print(f"Updated {field_to_update} for {name}.")  # Success message
    else:
        print(f"Student {name} not found.")  # Failure message


# Function to delete a student record by name
def delete_student(fields):
    name = input(f"Enter the name of the student to delete ({fields[0]}): ")  # Use the first field for lookup
    deleted = False  # Flag to track if deletion was successful
    records = []  # List to store remaining records

    try:
        with open('students.csv', 'r') as csv_file:
            for line in csv_file:
                row = line.strip().split(',')  # Split the CSV data by commas
                student_data = dict(zip(fields, row))  # Map field names to their values

                if student_data[fields[0]] != name:  # Skip the record to be deleted
                    records.append(list(student_data.values()))  # Add remaining records to the list
                else:
                    deleted = True  # Mark as deleted

    except FileNotFoundError:
        print("No records found. Add a student first.")
        return

    # Write the remaining records back to the CSV file
    with open('students.csv', 'w') as csv_file:
        csv_file.write(','.join(fields) + '\n')  # Write the header again
        for record in records:
            csv_file.write(','.join(record) + '\n')  # Write all remaining records

    if deleted:
        print(f"Student {name} deleted successfully.")  # Success message
    else:
        print(f"Student {name} not found.")  # Failure message


# Main menu function
def main():
    fields = initialize_fields()  # Initialize fields based on user input
    create_files_if_needed(fields)  # Call the function to create the system and data files if they don't exist

    while True:
        # Display menu options
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student(fields)  # Add a new student
        elif choice == '2':
            view_students(fields)  # View all student records
        elif choice == '3':
            update_student(fields)  # Update a student's record
        elif choice == '4':
            delete_student(fields)  # Delete a student's record
        elif choice == '5':
            print("Exiting program.")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


main()
# Function to update a student's information
def update_student(fields):
    name = input(f"Enter the name of the student to update ({fields[0]}): ")  # Use the first field (assumed unique) for lookup
    field_to_update = input("Enter the field to update: ")  # Field to be updated
    if field_to_update not in fields:
        print("Invalid field name.")  # Validate the field name
        return
    new_value = input(f"Enter new value for {field_to_update}: ")  # Get the new value for the field

    updated = False  # Flag to track if update was successful
    records = []  # List to store updated records

    try:
        with open('students.csv', 'r') as csv_file:
            for line in csv_file:
                row = line.strip().split(',')  # Split the CSV data by commas
                student_data = dict(zip(fields, row))  # Map field names to their values

                if student_data[fields[0]] == name:  # Check if the record matches the student name
                    student_data[field_to_update] = new_value  # Update the specified field
                    updated = True  # Flag to indicate that the update was successful

                # Convert the dictionary back to a list
                records.append(list(student_data.values()))

    except FileNotFoundError:
        print("No records found. Add a student first.")
        return

    # Write the updated records back to the CSV file
    with open('students.csv', 'w') as csv_file:
        csv_file.write(','.join(fields) + '\n')  # Write the header again
        for record in records:
            csv_file.write(','.join(record) + '\n')  # Write all updated records

    if updated:
        print(f"Updated {field_to_update} for {name}.")  # Success message
    else:
        print(f"Student {name} not found.")  # Failure message


# Function to delete a student record by name
def delete_student(fields):
    name = input(f"Enter the name of the student to delete ({fields[0]}): ")  # Use the first field for lookup
    deleted = False  # Flag to track if deletion was successful
    records = []  # List to store remaining records

    try:
        with open('students.csv', 'r') as csv_file:
            for line in csv_file:
                row = line.strip().split(',')  # Split the CSV data by commas
                student_data = dict(zip(fields, row))  # Map field names to their values

                if student_data[fields[0]] != name:  # Skip the record to be deleted
                    records.append(list(student_data.values()))  # Add remaining records to the list
                else:
                    deleted = True  # Mark as deleted

    except FileNotFoundError:
        print("No records found. Add a student first.")
        return

    # Write the remaining records back to the CSV file
    with open('students.csv', 'w') as csv_file:
        csv_file.write(','.join(fields) + '\n')  # Write the header again
        for record in records:
            csv_file.write(','.join(record) + '\n')  # Write all remaining records

    if deleted:
        print(f"Student {name} deleted successfully.")  # Success message
    else:
        print(f"Student {name} not found.")  # Failure message


# Main menu function
def main():
    fields = initialize_fields()  # Initialize fields based on user input
    create_files_if_needed(fields)  # Call the function to create the system and data files if they don't exist

    while True:
        # Display menu options
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student(fields)  # Add a new student
        elif choice == '2':
            view_students(fields)  # View all student records
        elif choice == '3':
            update_student(fields)  # Update a student's record
        elif choice == '4':
            delete_student(fields)  # Delete a student's record
        elif choice == '5':
            print("Exiting program.")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


main()