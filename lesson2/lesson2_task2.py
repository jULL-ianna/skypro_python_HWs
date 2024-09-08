#is_year_leap = 2020
is_year_leap = input('какой год интересует?')
year = int(is_year_leap)
yearf = year % 4
if (yearf % 4 ==0):
    print('високосный год')
else:
    print('невисокосный год')