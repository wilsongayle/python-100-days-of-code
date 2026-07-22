def format_name(f_name, l_name):
    return  f"{f_name.title()} {l_name.title()}"

formatted_name = format_name("FIRST", "LAST")

print(formatted_name)

def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2400))
print(is_leap_year(1989))