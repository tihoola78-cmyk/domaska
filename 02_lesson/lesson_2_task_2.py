def is_year_leap(year):
    """Функция проверяет, является ли год високосным"""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")