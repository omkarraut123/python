class salary:
    def __init__(self,pay):
        self.pay=pay

    def getsalary(self):
        return self.pay*12
class employee:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
        self.ob_salary=salary(self.pay)
    def disp(self):
        return (self.ob_salary.getsalary()+self.bonus)

emp=employee(30000,1000)
print(emp.disp())
                    
        