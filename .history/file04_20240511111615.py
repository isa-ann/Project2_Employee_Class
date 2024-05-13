class Employee:
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int) -> None:
        """
        Initialize an Employee object with the given attributes.

        Args:
            name (str): The name of the employee.
            job_title (str): The job title of the employee.
            department (str): The department of the employee.
            salary (float): The salary of the employee.
            hire_year (int): The year the employee was hired.
        """
        self._name = name
        self._job_title = job_title
        self._department = department
        self._salary = salary
        self._hire_year = hire_year

    @property
    def name(self) -> str:
        """Get the name of the employee."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the name of the employee."""
        self._name = value

    @property
    def job_title(self) -> str:
        """Get the job title of the employee."""
        return self._job_title

    @job_title.setter
    def job_title(self, value: str) -> None:
        """Set the job title of the employee."""
        self._job_title = value

    @property
    def department(self) -> str:
        """Get the department of the employee."""
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        """Set the department of the employee."""
        self._department = value

    @property
    def salary(self) -> float:
        """Get the salary of the employee."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Set the salary of the employee."""
        self._salary = value

    @property
    def hire_year(self) -> int:
        """Get the hire year of the employee."""
        return self._hire_year

    @hire_year.setter
    def hire_year(self, value: int) -> None:
        """Set the hire year of the employee."""
        self._hire_year = value

    def years_worked(self) -> int:
        """
        Calculate the total years this employee has worked here, based on the hire year.

        Returns:
            int: Total years worked.
        """
        current_year = 2024  # You can adjust this to the current year
        return current_year - self._hire_year

    def total_expense(self) -> float:
        """
        Calculate the total salary expense for this employee, which is the salary multiplied by the years worked.

        Returns:
            float: Total salary expense.
        """
        years_worked = self.years_worked()
        return self._salary * years_worked

    def write_employees(self, filename: str) -> None:
        """
        Write employee information to a text file.

        Args:
            filename (str): The name of the file to write to.
        """
        with open(filename, "a") as file:
            file.write(f"Name: {self._name}\nJob Title: {self._job_title}\nDepartment: {self._department}\nSalary: {self._salary}\nHire Year: {self._hire_year}\n")
            file.write(f"Years worked: {self.years_worked()}\n")
            file.write(f"Total salary expense: ${self.total_expense():,.2f}\n\n")

# Example usage:
if __name__ == "__main__":
    emp1 = Employee("Annie D", "Software Engineer", "Engineering", 80000.0, 2018)
    print(emp1)
    emp1.write_employees("employee_data.txt")
