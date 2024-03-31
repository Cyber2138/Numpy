class myth:
    def __init__(self) -> None:
        print('Welcome to be here: ')

    def series(self,a ):
        a = input('Enter the number that you want to create the series of: ')
        for i in range(int(a)):
            print(i)
        
    def sum(self, x, y):
        sum = x + y
        print(f"The sum of the two numbers are: {sum}")

x = myth()
x.series(500)

x.sum(5,12)

def sqrt(a):
    return a*a
print(sqrt(2))

sq = lambda x: x*x
print(sq(5))