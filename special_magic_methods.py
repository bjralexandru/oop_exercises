
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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last,
                                                   self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Alex', 'Bujor', 5000)
emp_2 = Employee('Florin', 'Bounegru', 5000)


print(len('test'))
print('test'.__len__())
print(len(emp_1))
# print(emp_1 + emp_2)
# print(repr(emp_1))
# print(str(emp_1))
