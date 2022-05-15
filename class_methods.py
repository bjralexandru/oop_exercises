
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


" The scope is to be able to access and modify the class varibles "
emp_1 = Employee('Alex', 'Bujor', 5000)
emp_2 = Employee('Alexandra', 'Popa', 6000)


print(emp_1.fullname())
print(emp_2.email)

print("Before the class_method")
emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)


print("After the class_method")
Employee.set_raise_amt(1.06)
emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)

print("We have a new employee from string")
emp_str_1 = 'Andrei-Turiac-5500'
print(' ')
new_emp_1 = Employee.from_string(emp_str_1)
print("And this is his email:")
print(new_emp_1.email)
