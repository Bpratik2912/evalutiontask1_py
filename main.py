from questions.fibonacci import fibonacci_number
from questions.primenumber import prime_number
from questions.armstrong import armstrong_number
print("numbers for methods:")
print("1) fibonacci number")
print("2) prime number")
print("3)armstrong number")
a = int(input("enter method number:"))

if a == 1:
    print(fibonacci_number.run(a))
elif a==2:
    print(prime_number.run(a))
elif a==3:
    print(armstrong_number.run(a))
else:
    print("")
