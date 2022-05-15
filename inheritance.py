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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Alex', 'Bujor', 5000, 'Golang')
dev_2 = Developer('Florin', 'Bounegru', 5000, 'Javascript')

print(dev_1.email)
print(dev_1.pay)

dev_1.apply_raise()

print(dev_1.pay)


print(dev_1.prog_lang)
print(dev_2.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])

print(mgr_1.email)
print(mgr_1.print_emp())

mgr_1.add_emp(dev_2)

print(mgr_1.print_emp())

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print("Mgr is an instance of Manager and Employeem, but not of Developer")
print(isinstance(mgr_1, Developer))
