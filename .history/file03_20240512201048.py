class Employee:
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):    # Here we initialize an Employee object with the given attributes.
        """
        Args:
            name (str): The name of the employee.
            job_title (str): The job title of the employee.
            department (str): The department of the employee.
            salary (float): The salary of the employee.
            hire_year (int): The year the employee was hired.
        """
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    def __str__(self) -> str:  # This will return a string representation of the Employee.
      
        return f"Name: {self.name}\nJob Title: {self.job_title}\nDepartment: {self.department}\nSalary: {self.salary}\nHire Year: {self.hire_year}"  # This will return a formatted string containing employee information.

    def years_worked(self) -> int: # This will calculate the total years this employee has worked here, based on the hire year and the current year

        current_year = 2024  # This year can adjusted this to the current year
        return current_year - self.hire_year

    def total_expense(self) -> float: # This will calculate the total salary expense for this employee, which is the salary multiplied by the years worked.

        years_worked = self.years_worked()
        return self.salary * years_worked

    def write_employees(self, filename: str) -> None: # This will Write the employee's information along with years worked and total salary expense to a text file specified by the filename parameter.
        """
        This will write the employee's information to a text file.

        Args:
            filename (str): The name of the file to write to.
        """
        with open(filename, "a") as file:
            file.write(f"Name: {self.name}\nJob Title: {self.job_title}\nDepartment: {self.department}\nSalary: {self.salary}\nHire Year: {self.hire_year}\n")
            file.write(f"Years worked: {self.years_worked()}\n")
            file.write(f"Total salary expense: ${self.total_expense():,.2f}\n\n")

# This block will prompt the user for input
name = input("Enter employee name: ")
job_title = input("Enter job title: ")
department = input("Enter department: ")
salary = float(input("Enter salary: "))
hire_year = int(input("Enter hire year: "))

# This block will create an Employee object
emp1 = Employee(name, job_title, department, salary, hire_year)
print(emp1)
emp1.write_employees("employee_data.txt")
