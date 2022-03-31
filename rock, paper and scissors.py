import random
import time

options = ['rock', 'paper', 'scissors']
point = 0
comppoint =0
game = 0

isint = 0
compatible = 0
command = ''

compatible = 0

def wait(secs):
    time.sleep(secs)

while compatible != 1:
    rounds = input('\033[1;34;40m How many rounds:')
    try:
        int(rounds)
        compatible=1
    except:
        print("\033[1;31;40mMust be a number.")
        continue

for i in range(0,int(rounds)):
        askforchoice = input('\033[1;34;40mChoose rock, paper or scissors:')
        computerhand = (random.choice(options))
        for s in range(1,3):
            print(str(s)+'..', end="")
            time.sleep(1)
        print('3')
        print('\033[1;37;40mComputer rolled {}'.format(computerhand))
        if askforchoice[0] == 'r' and computerhand[0] == 'r':
            print('\033[1;36;40mDraw! No points!')
        elif askforchoice[0]== 'r' and computerhand[0] == 's':
            print('\033[1;32;40mYou Win! (+1 point!)')
            point +=1
        elif askforchoice[0] == 'r' and computerhand[0] == 'p':
            print('\033[1;31;40mComputer wins! (-1 point!)')
            comppoint+=1
        elif  askforchoice[0] == 's' and computerhand[0] == 'r':
            print('\033[1;31;40mComputer wins! (-1 point!)')
            comppoint+= 1
        elif  askforchoice[0] == 's' and computerhand[0] == 's':
            print('Draw! No points!')
        elif  askforchoice[0] == 's' and computerhand[0] == 'p':
            print('\033[1;32;40mYou win! (+1 point!)')
            point += 1
        elif  askforchoice[0] == 'p' and computerhand[0] == 'r':
            print('\033[1;32;40mYou win! (+1 point!)')
            point += 1
        elif  askforchoice[0] == 'p' and computerhand[0] == 's':
            print('\033[1;31;40mComputer wins! (-1 point!)')
            comppoint+= 1
        elif  askforchoice[0] == 'p' and computerhand[0] == 'p':
            print('\033[1;36;40mDRAW! No points')

if comppoint < point:
    wait(2)
    print('*\033[1;33;40m-----------------')
    print('*\033[1;34;40mYou won the game!')
elif point < comppoint:
    wait(2)
    print('----------------------------------')
    print('*\033[1;31;40mYou lost the game!')
else:
    wait(2)
    print('*\033[2;36;40m*DRAW :)')

print('\033[1;37;40mYour total points:{}'.format(point))
print("\033[1;37;40mComputer's total points:{}".format(comppoint))
print('----------------------------------')
