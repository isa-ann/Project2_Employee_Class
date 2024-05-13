
from typing import Union

class Employee:
    """
    Represents a single employee in the management system.

    Attributes:
        name (str): The name of the employee.
        job_title (str): The job title of the employee.
        department (str): The department of the employee.
        salary (float): The salary of the employee.
        hire_year (int): The year the employee was hired.
    """

    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        self._name = name
        self._job_title = job_title
        self._department = department
        self._salary = salary
        self._hire_year = hire_year

    def __str__(self) -> str:
        """
        Returns a string representation of the employee.
        """
        return f"Name: {self._name}\nJob Title: {self._job_title}\nDepartment: {self._department}\nSalary: {self._salary}\nHire Year: {self._hire_year}"

    def years_worked(self) -> int:
        """
        Calculates the total years this employee has worked based on the hire year.
        """
        current_year = 2024  # Assuming current year is 2024
        return current_year - self._hire_year

    def total_expense(self) -> float:
        """
        Calculates the total salary expense for this employee, which is the salary multiplied by the years worked.
        """
        return self._salary * self.years_worked()

    def write_employee(self, file_path: str) -> None:
        """
        Writes the employee information to a text file.

        Args:
            file_path (str): The file path where the employee information will be written.
        """
        with open(file_path, 'w') as file:
            file.write(str(self) + '\n')

    # Accessor methods
    def get_name(self) -> str:
        return self._name

    def get_job_title(self) -> str:
        return self._job_title

    def get_department(self) -> str:
        return self._department

    def get_salary(self) -> float:
        return self._salary

    def get_hire_year(self) -> int:
        return self._hire_year

    # Mutator methods
    def set_name(self, name: str) -> None:
        self._name = name

    def set_job_title(self, job_title: str) -> None:
        self._job_title = job_title

    def set_department(self, department: str) -> None:
        self._department = department

    def set_salary(self, salary: float) -> None:
        self._salary = salary

    def set_hire_year(self, hire_year: int) -> None:
        self._hire_year = hire_year


# Create an instance of an employee
employee = Employee("John Doe", "Software Engineer", "Engineering", 60000, 2020)

# Write employee information to a text file
employee.write_employee("employee_info.txt")