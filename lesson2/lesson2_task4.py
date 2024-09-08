fizz_buzz = int(input('введите число'))
for i in range(1, fizz_buzz):
    if i%3==0 and i%5==0:
            print('FizzBuzz')
    elif i%3==0:
            print('Fizz')
    elif i%5==0:
            print('Buzz')
    
    else:
        print(i)