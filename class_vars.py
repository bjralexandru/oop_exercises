
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + '_' + last + '@company.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay *  self.raise_amount)


emp_1 = Employee('Alex','Bujor', 5000)
emp_2 = Employee('Alexandra', 'Popa', 6000)


print(emp_1.fullname())
print(emp_2.email)


emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)

