# EmployeePayrollManagementSystem
Companies use payroll management systems to calculate employee salaries, bonuses, deductions, and monthly payslips.
<br>
Requirements:
<br>
Create the following classes:
<br>
1. Employee
- Constructor takes employee_id, name, and department.
- Create a display_info() method.
- Create a calculate_salary() method.
2. FullTimeEmployee (inherits Employee)
- Add monthly_salary.
- Add bonus.
- Override calculate_salary().
- Salary = monthly salary + bonus.
3. PartTimeEmployee (inherits Employee)
- Add hourly_rate and hours_worked.
- Override calculate_salary().
- Salary = hourly rate × hours worked.
4. ContractEmployee (inherits Employee)
- Add contract_amount.
- Add working_days.
- Calculate salary based on the agreed contract amount and completed working days.
5. Payroll
- Store multiple employee objects.
- Create an add_employee() method.
- Create a find_employee() method.
- Create a generate_payslip() method.
- Create a calculate_total_payroll() method.