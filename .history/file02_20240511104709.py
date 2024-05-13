class Employee:
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        """
        Initialize an Employee object with the given attributes.

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

    def __str__(self) -> str:
        """
        Return a string representation of the Employee.

        Returns:
            str: A formatted string containing employee information.
        """
        return f"Employee: {self.name}, Job Title: {self.job_title}, Department: {self.department}"

    def years_worked(self) -> int:
        """
        Calculate the total years this employee has worked here, based on the hire year.

        Returns:
            int: Total years worked.
        """
        current_year = 2024  # You can adjust this to the current year
        return current_year - self.hire_year

    def total_expense(self) -> float:
        """
        Calculate the total salary expense for this employee, which is the salary multiplied by the years worked.

        Returns:
            float: Total salary expense.
        """
        years_worked = self.years_worked()
        return self.salary * years_worked

    def write_employees(self, filename: str) -> None:
        """
        Write employee information to a text file.

        Args:
            filename (str): The name of the file to write to.
        """
        with open(filename, "a") as file:
            file.write(f"{self.name}, {self.job_title}, {self.department}, {self.salary}, {self.hire_year}\n")

# Prompt the user for input
name = input("Enter employee name: ")
job_title = input("Enter job title: ")
department = input("Enter department: ")
salary = float(input("Enter salary: "))
hire_year = int(input("Enter hire year: "))

# Create an Employee object
emp1 = Employee(name, job_title, department, salary, hire_year)
print(emp1)
print(f"Years worked: {emp1.years_worked()}")
print(f"Total salary expense: ${emp1.total_expense():,.2f}")
emp1.write_employees("employee_data.txt")
