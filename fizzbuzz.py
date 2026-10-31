sayi = int(input("Bir ədəd daxil et: "))
if sayi % 3 == 0 and sayi % 5 == 0:
    print("FizzBuzz")
elif sayi % 3 == 0:
    print("Fizz")
elif sayi % 5 == 0:
    print("Buzz")
else:
    print(sayi)    