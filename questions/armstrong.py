# a =125
# print(len(str(a)))
from base import assignment
class armstrong_number(assignment):
    def run(self):
        """to find armstrong number: the armstrong value is like 153 = 1^3 + 5^3 +3^3 = 1+ 125 + 27 = 153"""
        a = int(input("enter a number to find armstrong number:"))
        sum = 0
        b = a
        while(b>0):
            n =len(str(b))
            # print(n)
            for i in range(n):
                rem = b % 10
                # print(rem)
                # print(rem^len(str(a)))
                sum = sum + ((rem)**n)
                # print(sum)
                b = b // 10
                # print(a)
            # return sum
        if (a==sum):
            return 'it is an armstrong number.'
        else:
            return 'it is NOT an armstrong number.'

# print(armstrong_number.run(a))