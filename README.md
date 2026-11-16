Employee Payroll Management System-

Project Overview:

This project is a web-based Employee Payroll Management System developed using Python, Bottle, and SQLite. The application allows users to retrieve employee payroll information by department, calculate employee wages based on hours worked, and update employee work hours through a web interface.
The project demonstrates practical experience with backend web development, relational database management, SQL queries, Python programming logic, and handling user-submitted form data.

Technologies Used:

•	Python: Application logic, routing, payroll calculations, and database interaction.
•	Bottle: Lightweight Python web framework used to create application routes and render HTML templates.
•	SQLite3: Relational database used to store and retrieve employee and payroll information.
•	SQL: Used to query employee records, join database tables, and update payroll information.
•	HTML Templates: Used to provide forms and display employee payroll information through the web interface.

Application Features.

1. Home Page>
The application uses a default home route (/) that displays the main landing page through a Bottle HTML template.

2. Department Payroll Lookup>
The department route (/department) allows users to select a department and retrieve associated employee payroll records.

The application:

•	Accepts department selections through an HTML form.
•	Connects to the SQLite payroll database.
•	Uses an SQL JOIN to retrieve employee and payroll information from the employees and pay_data tables.
•	Filters employee records based on the selected department.
•	Retrieves employee IDs, names, hourly wages, and hours worked.
•	Calculates employee gross pay.
•	Displays the results in a formatted table.

3. Payroll Calculation>

The application includes conditional logic to calculate regular and overtime wages.
Regular Pay:

Employees working 40 hours or less receive their standard hourly wage.
Overtime Pay:

Employees working more than 40 hours receive time-and-a-half for hours exceeding 40.

The calculation follows this logic:
•	Regular hours are paid at the standard hourly rate.
•	Overtime hours are calculated at 1.5 times the standard hourly rate.
•	Total gross pay combines regular earnings and overtime earnings.

4. Employee Hours Update>
The update route (/update_pay) allows users to modify an employee's recorded work hours.

The application:

•	Accepts an employee ID and updated hours through an HTML form.
•	Connects to the SQLite database.
•	Executes an SQL UPDATE statement to modify the employee's recorded hours.
•	Commits the changes to the database.
•	Retrieves the employee's information to confirm the update.
•	Displays a confirmation page containing the employee ID, name, and department.

Database Structure.

The application uses an SQLite database named payroll.db.
It references two relational database tables:

employees-
•	emp_id – Employee identification number.
•	emp_name – Employee name.
•	department – Employee department.

pay_data-
•	emp_id – Employee identification number used to associate payroll records with employees.
•	wage – Employee hourly wage.
•	hrs_worked – Recorded employee work hours.

The application uses SQL queries to retrieve, join, and update information across these tables.

Application Routes-

Route ~ Method ~ Purpose.

/ ~	GET ~	Displays the home page.
/department ~	GET / POST ~	Displays department form and retrieves payroll information.
/update_pay ~	GET / POST ~	Displays employee hours form and updates payroll records.

How to Run the Application-

Prerequisites>
•	Python installed.
•	Bottle framework installed.
•	SQLite database configured with the required tables and records.
•	Required HTML templates available to the application.

<<Installation>>

Install Bottle using pip:
pip install bottle.
SQLite3 is included with standard Python installations.
Running the Application-
Navigate to the project directory and execute:
python pythonprogram6.py
The Bottle application starts on port 8083.
Open a web browser and navigate to:
http://localhost:8083/

<< Skills Demonstrated >>

This project demonstrates the following technical skills:
•	Python application development.
•	Backend web application development.
•	Bottle framework and HTTP routing.
•	Relational database management.
•	SQLite database connectivity.
•	SQL SELECT, JOIN, and UPDATE statements.
•	Processing user-submitted form information.
•	Python conditional statements and calculations.
•	Data retrieval and manipulation.
•	Employee payroll and overtime calculations.
•	Dynamic data presentation through HTML templates.
•	Application logic and database integration.

Project Purpose

This project was developed to demonstrate the practical application of Python programming and database management concepts. It combines backend development, SQL database operations, user input processing, and business logic to create a functional employee payroll management application. Everything associated with the database is purely fictional.
It represents hands-on experience building an application that interacts with a relational database, processes employee information, performs calculations, and updates stored records through a web-based interface.
