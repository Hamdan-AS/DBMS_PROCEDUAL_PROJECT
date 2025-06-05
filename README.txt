Student Record Management System
Overview
The Student Record Management System allows users to manage student records, including adding new students, viewing existing records, updating student information, and deleting student records. The system is flexible and allows for dynamic fields that can be customized according to user needs.

Features
Dynamic Fields: The program lets users define the fields they want to track for each student.
Add Students: Add student records with user-defined fields.
View Students: View all student records in a tabular format.
Update Students: Update specific student details, such as name, age, etc.
Delete Students: Remove student records from the system by name.
File Storage: The records are saved in a CSV file for easy management and retrieval.
Requirements
Python 3.x
No external libraries are required.
Usage
1. Initial Setup
When the program is first run, it will prompt you to define the fields for each student record.
It will then create two files:
students.csv: Stores the student records.
system.txt: Stores information about the field configuration.
2. Menu Options
After setting up the fields, the program will display a menu with the following options:

1. Add Student:

Allows you to add a new student by entering values for each defined field.
The student's data will be stored in the students.csv file.
2. View Students:

Displays all student records in a table format, showing the fields you defined.
If no students have been added, it will show a message indicating no records are found.
3. Update Student Information:

Prompts you to enter the name of the student you wish to update.
Then, it lets you choose which field to update and enter the new value.
If the student or the field does not exist, an error message will be shown.
4. Delete Student:

Allows you to delete a student record by providing their name.
If the student is found, the record is removed; otherwise, an error message is shown.
5. Exit:

Exits the program.
3. Field Setup Example
When prompted to enter the fields for student records, you can input various attributes such as:

Name
Age
Grade
Address
You can customize the fields to fit your needs (e.g., adding Phone Number, Email, or other attributes relevant to your use case).

4. File Details
students.csv: This file contains student records. Each record corresponds to a student, and fields are separated by commas. Example:

css
Copy code
John Doe, 16, A, 123 Main St.
Jane Smith, 15, B, 456 Elm St.
system.txt: This file stores the configuration of the fields, including the number of fields and their names. Example:

yaml
Copy code
Number of fields: 4
Field: Name, Length: 4
Field: Age, Length: 3
Field: Grade, Length: 5
Field: Address, Length: 13
How to Run the Program
Clone or download the project files.
Run the main.py script in your terminal or IDE.
css
Copy code
python main.py
Follow the on-screen instructions to manage student records.
Example Workflow
Define Fields: You might define fields like Name, Age, Grade, and Address.
Add Students: Add students such as:
John Doe, 16, A, 123 Main St.
Jane Smith, 15, B, 456 Elm St.
View Students: Display the current records.
Update a Student: Update John Doe's address or grade.
Delete a Student: Remove Jane Smith from the records.
Troubleshooting
If the program fails to open or create the files, ensure that you have write permissions in the directory where the program is located.
If the data format seems corrupted, ensure that each record in students.csv matches the number of fields defined.
If you encounter a "Field not found" error, make sure you're using the correct field names when updating or deleting records.
License
This program is free to use and modify under the MIT License.