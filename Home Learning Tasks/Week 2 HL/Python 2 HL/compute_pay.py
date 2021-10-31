def compute_pay():
    hour= int(input("Enter hours worked: "))
    rate= int(input("Enter hourly rate: "))
    salary = hour * rate
    if hour > 10:
        salary = salary * 1.5
        print(f"\nYour salary is £{salary}")
    else:
        salary = salary
        print(f"\nYour salary is £{salary}")
        
compute_pay()

    