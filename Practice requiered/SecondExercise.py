
from functools import reduce




def findOddNumber():
    odd = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    findOddNumbers = filter(lambda x: x % 2 != 0, odd)

    newList = list(findOddNumbers)

    additionResult = reduce(lambda a,b: a + b,newList)

    print(f'The odd list is: {newList} and its summation is: {additionResult}')
    
findOddNumber()
