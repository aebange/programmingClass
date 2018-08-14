

# Classes are created simply be defining them
class Employee:
    # Define the attributes of the Employee class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # Create a method for the Employee class that calls and outputs the attributes of the Employee as a string.
    def user_information(self):
        return '{} {} {} {}'.format(self.first, self.last, self.pay, self.email)


employee_1 = Employee('Big', 'Mike', 20000)
employee_2 = Employee('Duck', 'Pool', 4500)


# Print user information using class method. Parenthesis are required as this is a method and not an attribute.
print(employee_1.user_information())
print(employee_2.user_information())

# Alternatively, this can be done to print
print(Employee.user_information(employee_1))