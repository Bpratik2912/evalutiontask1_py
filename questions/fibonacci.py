
from base import assignment
class fibonacci_number(assignment):
    def run(self):
        """to find fibonacci number at position : initial values are 0 and 1 then add this process till given position."""
        a=int(input("enter number to find fibonacci number:"))
        p=1
        q=0
        if(a<0):
            return 'invalid input'
        elif(a==0):
            return q
        elif(a==1):
            return p
        else:
            for i in range(2, a+2):
                sum = p + q
                p = q
                q = sum
                # print(i) 
            return q


# print(fibonacci_number.run(a))


