"""
pascals.py

Print out n lines of pascal's triangle
Each number in a line of the triangle is the sum of the two numbers above it, where n=1 is 1
The first 4 rows are:
0:    1               {1}
1:   1 1          {0+1, 1+0}
2:  1 2 1       {0+1, 1+1, 1+0}
3: 1 3 3 1   {0+1, 1+2, 2+1, 1+0}
"""

class Pascals:

    def __init__(self, n):
        self.size = n
        self.triangle = []
        for x in range(n):
            self.triangle.append(self.buildLine(x))
        self.maxWidth = len(self.rowToStr(self.triangle[-1]))

    def rowToStr(self, row):
        return ' '.join(map(str, row))

    def buildLine(self, n):
        # build a line of the triangle
        line = []
        for x in range(n+1):
            line.append(nChooseK(n, x))
        return line
    
    def print(self):
        for row in self.triangle:
            string = self.rowToStr(row)
            rowWidth = len(string)
            #string += " ("+str(rowWidth)+")"

            if rowWidth < self.maxWidth:
                numSpaces = int((self.maxWidth - rowWidth)/2)
                print(" " * numSpaces + string)
            else:
                print(string)


def nChooseK(n, k):
    # {n, k} = [n(n-1)(n-2)...(n-k+1)] / k! = n! / k!(n-k)!     
    return int(factorial(n) / (factorial(k) * factorial(n-k)))


def factorial(k):
    # return k!
    if k <= 1:
        return 1
    else:
        return k * factorial(k-1)


def main():
    """ the main function """
    num = int(input('Display which row of Pascal\'s Triangle? '))
    p = Pascals(num)
    p.print()


if __name__ == '__main__':
    main()