x=int(input("сколько денег? "))
y=int(input("на сколько лет? "))

def bank(x, y):

    if x < 0 or x == 0:
                print("Нельзя так !")
                return
    if y < 0 or y == 0:
           print("Нельзя так !")
    else:
        result = x*0.1 * y
    summa = x + result
    print("Вы получите: ", summa)
bank(x, y)