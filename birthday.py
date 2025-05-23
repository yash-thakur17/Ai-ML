from datetime import datetime

def is_leap_year(year):
    return (year % 4== 0 and year % 100 != 0 ) or (year % 400 == 0)

birth_input = input("Enter a birthdate (dd/mm/year): ")

birth_date = datetime.strptime(birth_input, "%d/%m/%Y")
current_time = datetime.now()

if is_leap_year(birth_date.year):
    print(f"{birth_date.year} is a leap year")
else:
    print(f"{birth_date.year} is not a leap year")

age_days = (current_time - birth_date).days
age_year = age_days // 365
age_months = age_days // 30
age_hours = age_days * 24
age_seconds = age_days * 24 * 3600

print(f"\nYour age is approximately:")
print(f"{age_year} years")
print(f"{age_months} months")
print(f"{age_days} days")
print(f"{age_hours} hours")
print(f"{age_seconds} seconds")