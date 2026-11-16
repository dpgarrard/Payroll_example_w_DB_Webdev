Payroll Management Web Application

A lightweight, full-stack Python web application built using the **Bottle** micro-framework and **SQLite**. This application manages employee payroll records, calculates regular versus overtime gross pay based on weekly hours worked, and allows users to filter department reports and update employee hours via an interactive web interface.

---

## Key Technical Highlights

* **Automated Overtime & Gross Pay Calculation:** Automatically computes employee compensation upon generating department reports, applying a standard wage rate for up to 40 hours and a 1.5x overtime multiplier for any hours worked beyond 40.
* **Relational Database Integration & Joins:** Executes multi-table `JOIN` queries across `employees` and `pay_data` tables using parameterized inputs (`?` placeholders) to secure database operations against SQL injection.
* **RESTful Form Processing:** Maps separate `GET` and `POST` request handlers via Bottle decorators (`@route`) to cleanly separate template form rendering from submission logic.
* **Dynamic Action Confirmation:** Redirects users to confirmation views displaying updated employee and department details upon successful database commits.

---

## Tech Stack

* **Language:** Python 3
* **Web Framework:** [Bottle](https://bottlepy.org/) (`bottle`)
* **Database:** SQLite (`sqlite3`)
* **Templating:** Bottle SimpleTemplate Engine (`.tpl` views)

---

## API Routes & Endpoints

| Endpoint | Methods | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Renders the home/landing page view (`index`). |
| `/department` | `GET`, `POST` | Renders the department selection form (`GET`) or queries payroll data, calculates overtime, and displays employee pay tables (`POST`). |
| `/update_pay` | `GET`, `POST` | Renders the hours update form (`GET`) or updates `pay_data` hours for a specific `emp_id` and returns a confirmation page (`POST`). |

---

## Getting Started

### 1. Prerequisites

Ensure you have **Python 3.x** installed, then install the `bottle` framework:

bash
pip install bottle
2. Project Structure
Verify that your workspace includes your script file, your SQLite database (payroll.db), and your Bottle template files inside a /views directory:

Plaintext
├── pythonprogram6.py
├── payroll.db
└── views/
    ├── index.tpl
    ├── dept_form.tpl
    ├── show_department.tpl
    ├── edit_emp_hrs.tpl
    ├── did_it_work.tpl
    └── message.tpl
3. Database Schema Setup
The application connects to a SQLite database named payroll.db which requires two relational tables (employees and pay_data). You can set them up with the following schema:

SQL
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pay_data (
    emp_id INTEGER,
    wage REAL NOT NULL,
    hrs_worked REAL NOT NULL,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);
4. Running the Web Server
Start the local server on port 8083:

Bash
python pythonprogram6.py
Open your browser and navigate to http://localhost:8083.
