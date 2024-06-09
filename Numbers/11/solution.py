def is_leap_year(year: int):
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 != 0:
                return False
            return True


print("Leap Years : ")
for i in range(2000, 3000):
    if is_leap_year(i):
        print(i, end=", ")
