from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from flask_sqlalchemy import SQLAlchemy

import config

# =====================================================
# Flask Configuration
# =====================================================

app = Flask(__name__)

app.config['SECRET_KEY'] = config.SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = (
    config.SQLALCHEMY_DATABASE_URI
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =====================================================
# Employee Model
# =====================================================

class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    department = db.Column(
        db.String(100),
        nullable=False
    )

    salary = db.Column(
        db.Integer,
        nullable=False
    )

    def __repr__(self):
        return f"<Employee {self.name}>"

# =====================================================
# Create Tables
# =====================================================

with app.app_context():
    db.create_all()

# =====================================================
# Login Page
# =====================================================

@app.route("/")
def login():

    return render_template(
        "login.html"
    )

# =====================================================
# Authenticate User
# =====================================================

@app.route(
    "/authenticate",
    methods=["POST"]
)
def authenticate():

    username = request.form.get(
        "username"
    )

    password = request.form.get(
        "password"
    )

    if (
        username == "admin"
        and
        password == "admin"
    ):

        session["user"] = username

        flash(
            "Login Successful",
            "success"
        )

        return redirect(
            url_for(
                "dashboard"
            )
        )

    flash(
        "Invalid Username or Password",
        "danger"
    )

    return redirect(
        url_for(
            "login"
        )
    )

# =====================================================
# Dashboard
# =====================================================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:

        flash(
            "Please Login First",
            "warning"
        )

        return redirect(
            url_for(
                "login"
            )
        )

    employee_count = Employee.query.count()

    total_salary = db.session.query(
        db.func.sum(
            Employee.salary
        )
    ).scalar()

    if total_salary is None:
        total_salary = 0

    return render_template(
        "dashboard.html",
        employee_count=employee_count,
        total_salary=total_salary
    )

# =====================================================
# Add Employee Page
# =====================================================

@app.route("/add")
def add_employee():

    if "user" not in session:

        return redirect(
            url_for(
                "login"
            )
        )

    return render_template(
        "add_employee.html"
    )

# =====================================================
# Save Employee
# =====================================================

@app.route(
    "/save",
    methods=["POST"]
)
def save_employee():

    if "user" not in session:

        return redirect(
            url_for(
                "login"
            )
        )

    name = request.form["name"]

    email = request.form["email"]

    department = request.form[
        "department"
    ]

    salary = request.form[
        "salary"
    ]

    existing_employee = (
        Employee.query.filter_by(
            email=email
        ).first()
    )

    if existing_employee:

        flash(
            "Email Already Exists",
            "danger"
        )

        return redirect(
            url_for(
                "add_employee"
            )
        )

    employee = Employee(
        name=name,
        email=email,
        department=department,
        salary=salary
    )

    db.session.add(employee)

    db.session.commit()

    flash(
        "Employee Added Successfully",
        "success"
    )

    return redirect(
        url_for(
            "employees"
        )
    )

# =====================================================
# Employee List
# =====================================================

@app.route("/employees")
def employees():

    if "user" not in session:

        return redirect(
            url_for(
                "login"
            )
        )

    search = request.args.get(
        "search"
    )

    if search:

        employee_list = (
            Employee.query.filter(
                Employee.name.contains(
                    search
                )
            ).all()
        )

    else:

        employee_list = (
            Employee.query.all()
        )

    return render_template(
        "employees.html",
        employees=employee_list
    )

# =====================================================
# Edit Employee
# =====================================================

@app.route("/edit/<int:id>")
def edit_employee(id):

    if "user" not in session:

        return redirect(
            url_for(
                "login"
            )
        )

    employee = Employee.query.get_or_404(
        id
    )

    return render_template(
        "edit_employee.html",
        employee=employee
    )

# =====================================================
# Update Employee
# =====================================================

@app.route(
    "/update/<int:id>",
    methods=["POST"]
)
def update_employee(id):

    if "user" not in session:

        return redirect(
            url_for(
                "login"
            )
        )

    employee = Employee.query.get_or_404(
        id
    )

    employee.name = request.form[
        "name"
    ]

    employee.email = request.form[
        "email"
    ]

    employee.department = request.form[
        "department"
    ]

    employee.salary = request.form[
        "salary"
    ]

    db.session.commit()

    flash(
        "Employee Updated Successfully",
        "success"
    )

    return redirect(
        url_for(
            "employees"
        )
    )

# =====================================================
# Delete Employee
# =====================================================

@app.route("/delete/<int:id>")
def delete_employee(id):

    if "user" not in session:

        return redirect(
            url_for(
                "login"
            )
        )

    employee = Employee.query.get_or_404(
        id
    )

    db.session.delete(
        employee
    )

    db.session.commit()

    flash(
        "Employee Deleted Successfully",
        "success"
    )

    return redirect(
        url_for(
            "employees"
        )
    )

# =====================================================
# Reports Page
# =====================================================

@app.route("/reports")
def reports():

    if "user" not in session:
        return redirect("/")

    total_employees = Employee.query.count()

    total_salary = db.session.query(
        db.func.sum(Employee.salary)
    ).scalar()

    if total_salary is None:
        total_salary = 0

    average_salary = db.session.query(
        db.func.avg(Employee.salary)
    ).scalar()

    if average_salary is None:
        average_salary = 0

    departments = db.session.query(
        Employee.department
    ).distinct().count()

    return render_template(
        "reports.html",
        total_employees=total_employees,
        total_salary=total_salary,
        average_salary=round(average_salary,2),
        departments=departments
    )

# =====================================================
# Logout
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged Out Successfully",
        "info"
    )

    return redirect(
        url_for(
            "login"
        )
    )

# =====================================================
# Run Application
# =====================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )