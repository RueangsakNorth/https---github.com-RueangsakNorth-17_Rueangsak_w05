# # คำนวณภาษี
# salary = 15000
# tax = 0.07
# ot_time = 10
# ot_rate = 100
# gross_salary = salary + (ot_time * ot_rate)
# tax = gross_salary * tax
# net_pay = gross_salary - tax
# print(f"{net_pay} บาท")

def calurate_salary(salary, ot_time, ot_rate, tax_rate):
    gross_salary = salary + (ot_time * ot_rate)
    tax = gross_salary * tax_rate
    net_pay = gross_salary - tax
    return net_pay,tax_rate,gross_salary
emp_1=calurate_salary(15000, 10, 100, 0.07)
emp_2=calurate_salary(20000, 5, 150, 0.07)
emp_3=calurate_salary(25000, 8, 200, 0.07)
print(f"Employee 1: Net Pay: {emp_1[0]} Tax: {emp_1[1]} Gross Salary: {emp_1[2]}")