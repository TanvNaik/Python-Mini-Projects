def display_game(gamelist):
    print('Here is the current list')
    print(gamelist)

def postion_choice():
    choice='Wrong'
    while choice.isdigit()==False or choice not in ['0','1','2'] :
        choice=input('Pick a position (0,1,2): ')
        if choice.isdigit():
            pass
        else:
            print('Invalid choice')
    return int(choice)

def replacement_choice(gamelist,position):
    user_placement=input('Enter string to replace at position')
    gamelist[position]=user_placement
    return gamelist

def gameon_choice():
    choice='Wrong'
    while choice not in ['y','n']:
        choice=input('Keep playing?(y or n): ')
        if choice not in ['y','n']:
            print('Please choose y or n')

    if choice=='y':
        return True
    else:
        return False

gamelist=[0,1,2]
gameon=True
while gameon:
    display_game(gamelist)
    position=postion_choice()
    gamelist=replacement_choice(gamelist,position)
    display_game(gamelist)
    gameon=gameon_choice()
