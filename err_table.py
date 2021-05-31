import random

def rohan(n):
    wrong=random.randint(0,10)
    table=[i*n for i in range(1,11)]
    table[wrong]=table[wrong]+random.randint(0,10)
    return table

def isCorrect(table,n):
    rohan(num)
    for i in range(1,11):
        if(table[i-1]!=(n*(i))):
            return (i-1)
    return None

if __name__=="__main__":
    print("enter the no. for which you want the table:")
    num = int(input())
    mytable=rohan(num)
    print(mytable)
    wrongindex= isCorrect(mytable,num)
    print(f"error occured at index {wrongindex}")
