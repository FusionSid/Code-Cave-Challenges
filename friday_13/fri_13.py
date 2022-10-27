from datetime import datetime

def friday(month: int, year: int) -> bool:
    date = datetime.strptime(f"13 {month} {year}", "%d %m %Y")
    return date.weekday() == 4

month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

print(friday(month, year))