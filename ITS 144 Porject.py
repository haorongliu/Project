from random import randint
match=int(input('How much games do you want to play?(such as \'1\'\'2\'......):'))
player_score=int(0)
AI_score=int(0)
for i in range(match):
    player = input('rock(r), paper(p) or scissors (s)?')
    radom = randint(1,3)
    if player!='r' and player!='p' and player!='s':
        print('Wrong typing, please retry')
    if i!= match and player=='r' or player=='p' or player=='s':
        if radom==1:
            print(player,'vs', 'r')
            if player=='r':
                print('DRAW!')
            elif player=='s':
                print('Computer wins!')
                AI_score+=1
            elif player=='p':
                print('Player wins!')
                player_score+=1
        elif radom==2:
            print(player,'vs', 'p')
            if player=='p':
                print('DRAW!')
            elif player=='r':
                print('Computer wins!')
                AI_score+=1
            elif player=='s':
                print('Player wins!')
                player_score+=1
        elif radom==3:
            print(player,'vs', 's')
            if player=='s':
                print('DRAW!')
            elif player=='p':
                print('Computer wins!')
                AI_score+=1
            elif player=='r':
                print('Player wins!')
                player_score+=1
print('Total score: AI:{}, Player:{}'. format(AI_score, player_score))
print('Thank you for playing')