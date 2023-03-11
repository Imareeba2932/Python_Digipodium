def calculate_da(basic_salary):
    if basic_salary<10000:
        return basic_salary*0.15
    elif basic_salary<25000:
        return basic_salary*0.175
    else:
        return basic_salary*0.112
def calc_salary(basic_salary,da):
    total=basic_salary+da
    epf=total*.20
    return total-epf
#usage
bs=int(input('Enter your basic salary:'))
da=calculate_da(bs)
salary=calc_salary(bs,da)
print(f'your salary is: {salary}')