
"""An employee payroll management system using Python OOP."""


class Employee:
    """Represent a general employee."""

    def __init__(self, employee_id, name, department):
        """Initialize employee information."""
        self.employee_id = employee_id
        self.name = name
        self.department = department

    def calculate_salary(self):
        """Calculate employee salary."""
        raise NotImplementedError("Subclasses must implement calculate_salary().")

    def display_info(self):
        """Display employee information."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")


class FullTimeEmployee(Employee):
    """Represent a full-time employee."""

    def __init__(self, employee_id, name, department,
                 monthly_salary, bonus):
        """Initialize a full-time employee."""
        super().__init__(employee_id, name, department)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        """Calculate full-time employee salary."""
        return self.monthly_salary + self.bonus


class PartTimeEmployee(Employee):
    """Represent a part-time employee."""

    def __init__(self, employee_id, name, department,
                 hourly_rate, hours_worked):
        """Initialize a part-time employee."""
        super().__init__(employee_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Calculate part-time employee salary."""
        return self.hourly_rate * self.hours_worked


class ContractEmployee(Employee):
    """Represent a contract employee."""

    def __init__(self, employee_id, name, department,
                 contract_amount, working_days, completed_days):
        """Initialize a contract employee."""
        super().__init__(employee_id, name, department)
        self.contract_amount = contract_amount
        self.working_days = working_days
        self.completed_days = completed_days

    def calculate_salary(self):
        """Calculate salary based on completed contract days."""
        if self.working_days <= 0:
            return 0

        return (self.contract_amount / self.working_days) * self.completed_days


class Payroll:
    """Manage employee records and payroll calculations."""

    def __init__(self):
        """Initialize the payroll system."""
        self.employees = []

    def add_employee(self, employee):
        """Add an employee to the payroll."""
        if self.find_employee(employee.employee_id):
            print("Employee ID already exists!")
            return

        self.employees.append(employee)
        print("Employee added successfully!")

    def find_employee(self, employee_id):
        """Find an employee by ID."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def generate_payslip(self, employee_id):
        """Generate an employee payslip."""
        employee = self.find_employee(employee_id)

        if employee is None:
            print("Employee not found!")
            return

        print("\n===== EMPLOYEE PAYSLIP =====")
        employee.display_info()
        print(f"Employee Type: {employee.__class__.__name__}")
        print(f"Total Salary: {employee.calculate_salary():.2f}")
        print("============================")

    def display_all_employees(self):
        """Display all employee records."""
        if not self.employees:
            print("No employees registered.")
            return

        for employee in self.employees:
            print("\n--------------------")
            employee.display_info()
            print(f"Salary: {employee.calculate_salary():.2f}")

    def calculate_total_payroll(self):
        """Calculate total salary of all employees."""
        total = sum(
            employee.calculate_salary()
            for employee in self.employees
        )

        print(f"Total Company Payroll: {total:.2f}")


def main():
    """Run the employee payroll management system."""

    payroll = Payroll()

    while True:
        print("\n===== ABC COMPANY PAYROLL =====")
        print("1. Add Full-Time Employee")
        print("2. Add Part-Time Employee")
        print("3. Add Contract Employee")
        print("4. Generate Payslip")
        print("5. Display All Employees")
        print("6. Calculate Total Payroll")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice in (1, 2, 3):
                employee_id = input("Employee ID: ")
                name = input("Employee name: ")
                department = input("Department: ")

                if choice == 1:
                    salary = float(input("Monthly salary: "))
                    bonus = float(input("Bonus: "))

                    employee = FullTimeEmployee(
                        employee_id, name, department, salary, bonus
                    )

                elif choice == 2:
                    rate = float(input("Hourly rate: "))
                    hours = float(input("Hours worked: "))

                    employee = PartTimeEmployee(
                        employee_id, name, department, rate, hours
                    )

                else:
                    amount = float(input("Contract amount: "))
                    days = int(input("Total working days: "))
                    completed = int(input("Completed working days: "))

                    if days <= 0 or completed < 0 or completed > days:
                        print("Invalid contract working days!")
                        continue

                    employee = ContractEmployee(
                        employee_id, name, department,
                        amount, days, completed
                    )

                payroll.add_employee(employee)

            elif choice == 4:
                employee_id = input("Enter employee ID: ")
                payroll.generate_payslip(employee_id)

            elif choice == 5:
                payroll.display_all_employees()

            elif choice == 6:
                payroll.calculate_total_payroll()

            elif choice == 7:
                print("Exiting payroll system. Goodbye!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter valid numeric information.")


if __name__ == "__main__":
    main()