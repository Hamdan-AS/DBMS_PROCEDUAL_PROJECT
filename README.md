# Student Record Management System

## 📌 Overview
The **Student Record Management System** allows users to manage student records, including:

- Adding new students
- Viewing existing records
- Updating student information
- Deleting student records

The system is flexible and allows for **dynamic fields** that can be customized as per user needs.

---

## ✅ Features

- **Dynamic Fields**: Users define the fields they want to track (e.g., Name, Age, Grade).
- **Add Students**: Add student records with user-defined fields.
- **View Students**: View all student records in a tabular format.
- **Update Students**: Update specific student details.
- **Delete Students**: Remove student records by name.
- **File Storage**: Data is saved in a CSV file for easy access.

---

## ⚙️ Requirements

- Python 3.x  
- No external libraries required

---

## 🚀 Usage

### 1. Initial Setup

When the program is first run:
- It prompts you to define the fields (e.g., Name, Age, etc.)
- Then it creates two files:
  - `students.csv` – stores student records.
  - `system.txt` – stores field configuration.

---

### 2. Menu Options

Upon setup, the menu includes:

#### 1️⃣ Add Student
- Enter values for each defined field.
- Data saved to `students.csv`.

#### 2️⃣ View Students
- Displays all records in tabular format.
- If no records exist, a message is shown.

#### 3️⃣ Update Student Information
- Enter student name → choose field → update value.
- Errors shown if student/field doesn't exist.

#### 4️⃣ Delete Student
- Enter student name to delete.
- If found → deleted. If not → error message.

#### 5️⃣ Exit
- Exits the program.

---

### 3. 🧪 Field Setup Example

When asked to define fields, you can input:

- Name
- Age
- Grade
- Address

Or customize:
- Phone Number
- Email
- Any other relevant fields

---

### 4. 🗂 File Details

#### 📄 `students.csv`
Contains student records in CSV format.  
Example:
John Doe, 16, A, 123 Main St.
Jane Smith, 15, B, 456 Elm St.

#### 📝 `system.txt`
Stores field configuration.
Example:
Number of fields: 4
Field: Name, Length: 4
Field: Age, Length: 3
Field: Grade, Length: 5
Field: Address, Length: 13
