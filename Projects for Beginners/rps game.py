import random 

rps = ['rock' , 'paper','Scissors']
user_point = 0
com_point = 0

def winning(u,c) :
    if u == 3 :
        print('you win')
        return False
    if c == 3 :
        print('computer wins')
        return False
    else :
        return True

def play(u,c):
    global user_point , com_point
    if u=='rock':
        if c =='paper':
            com_point += 1
            print('one point for comuter')
        elif c == 'Scissors':
            user_point +=1
            print('one point for you')
        else :
            print('no one get a point')
            
    if u=='paper':
        if c =='Scissors':
            com_point += 1
            print('one point for comuter')
        elif c == 'rock':
            user_point +=1
            print('one point for you')
        else :
            print('no one get a point')
            
    if u=='Scissors':
        if c =='rock':
            com_point += 1
            print('one point for comuter')
        elif c == 'paper':
            user_point +=1
            print('one point for you')
        else :
            print('no one get a point')
            
            
while winning(user_point,com_point):
    turn = input('please enter ')
    if turn not in rps :
        print("you cana only play 'rock' , 'paper' and 'Scissors' ")
        turn = input('please enter')
    else :
        c_turn = random.choice(rps)
        print(f'comp choose {c_turn}')
        play(turn,c_turn)
        print(f'your point {user_point}')
        print(f'comp point {com_point}')
    
    
