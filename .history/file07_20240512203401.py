class Employee:
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        """
        In this step Initializes an Employee object with the given attributes.

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
        """
        Accessor method for the name attribute.

        Returns:
            str: The name of the employee.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Mutator method for the name attribute.

        Args:
            value (str): The new name of the employee.
        """
        self._name = value

    @property
    def job_title(self) -> str:
        """
        Accessor method for the job_title attribute.

        Returns:
            str: The job title of the employee.
        """
        return self._job_title

    @job_title.setter
    def job_title(self, value: str) -> None:
        """
        Mutator method for the job_title attribute.

        Args:
            value (str): The new job title of the employee.
        """
        self._job_title = value

    @property
    def department(self) -> str:
        """
        Accessor method for the department attribute.

        Returns:
            str: The department of the employee.
        """
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        """
        Mutator method for the department attribute.

        Args:
            value (str): The new department of the employee.
        """
        self._department = value

    @property
    def salary(self) -> float:
        """
        Accessor method for the salary attribute.

        Returns:
            float: The salary of the employee.
        """
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """
        Mutator method for the salary attribute.

        Args:
            value (float): The new salary of the employee.
        """
        self._salary = value

    @property
    def hire_year(self) -> int:
        """
        Accessor method for the hire_year attribute.

        Returns:
            int: The year the employee was hired.
        """
        return self._hire_year

    @hire_year.setter
    def hire_year(self, value: int) -> None:
        """
        Mutator method for the hire_year attribute.

        Args:
            value (int): The new hire year of the employee.
        """
        self._hire_year = value

    def __str__(self) -> str:
        """
        Returns a string representation of the Employee.

        Returns:
            str: A formatted string containing employee information.
        """
        return f"Name: {self.name}\nJob Title: {self.job_title}\nDepartment: {self.department}\nSalary: {self.salary}\nHire Year: {self.hire_year}"

    def years_worked(self) -> int:
        """
        Calculates the total years this employee has worked based on the hire year.

        Returns:
            int: Total years worked.
        """
        current_year = 2024  # This year can adjusted this to the current year
        return current_year - self.hire_year

    def total_expense(self) -> float:
        """
        Calculates the total salary expense for this employee, which is the salary multiplied by the years worked.

        Returns:
            float: Total salary expense.
        """
        years_worked = self.years_worked()
        return self.salary * years_worked

    def write_employees(self, filename: str) -> None:
        """
        Writes the employee's information to a text file.

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
