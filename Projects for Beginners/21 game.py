import random

print('please start, you can say up to 3 sequence numbers in each turn, remmember whom said the number 21, loose the game')

def checkpoint(lt,st):
    for i in st :
        if i in lt :
            print('this numbers already played')
            return False
    for i in range(len(st)-1):
        if st[i+1]-st[i] != 1 :
            print('numbers must follow the sequence')
            return False
    try :
      if lt[-1] - st[0] != -1 :
        print('you have to follow the sequense of numbers')
        return False
    except IndexError:
        if st[0] != 1 :
            print('you should start with number 1 in your fist turn')
            return False 
    if len(st) > 3:
        print('you can only enter up to 3 numbers in each turn')
        return False
    if len(st)< 1 :
        print('you have to enter at least one numbers')
        return False
    if 21 in st:
        print('you loose')
        print(lt + st)
        return False
    
    return True 
numbers = []
while len(numbers)<21 :
    try :
        nums = list(map(int, input().split()))
    except ValueError :
        print('you can only enter integer numbers')
        nums = list(map(int, input().split()))
    if checkpoint(numbers,nums):
            numbers.extend(nums)
            q = random.randint(1,3)
            for i in range(q):
                numbers.append(numbers[-1]+1)
                if 21 in numbers:
                    print('you win')
                    print(numbers)
                    break
            else :
                 print(numbers)
        
    

    