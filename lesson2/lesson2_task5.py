month_to_season = input('введите номер месяца')
a = int(month_to_season)

if a == 1 or a == 2 or a == 12:
    print ("зима")
elif a == 3 or a == 4 or a == 5:
    print("весна")
elif a == 6 or a == 7 or a == 8:
    print("лето")
elif a == 9 or a == 10 or a == 11:
    print("осень")
else:
    print("укажите правильный номер месяца")




