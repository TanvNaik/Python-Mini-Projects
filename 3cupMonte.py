from random import shuffle

def shuffled(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=''
    while guess not in [0,1,2]:
        guess=int(input('Pick a number 0,1 or 2:'))
    return guess

def check(mylist,guess):
    if mylist[guess]=='O':
        print('Correct guess!')
    else:
        print('You lose!')

mylist=[' ','O',' ']
newlist=shuffled(mylist)
index=player_guess()
check(newlist,index)

