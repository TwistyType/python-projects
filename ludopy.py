import random

playerList = ['A', 'B', 'C', 'D']
totalCount = {}

# populating initial values of totalCount
for player in playerList:
    totalCount[player] = 0

roundNumber = 1
while  True:
    winner = 0
    print('--------- Round', roundNumber, '---------')
    for player in playerList:
        currentPlayer = player
        while True:
            runAgain = 0
            input('Please roll the dice for player ' + player)
            rolledVal = random.randint(1,6)
            print('Rolled value for player '+ player + ' is', rolledVal)
            totalCount[player] = totalCount[player] + rolledVal
            for pl in totalCount:
                if pl != currentPlayer:
                    if totalCount[pl] == totalCount[currentPlayer]:
                        choice = input('Will you like to kill player ' + pl + ' (y/n)? --> ')
                        if choice == 'y' or choice == 'Y':
                            totalCount[pl] = 0
                            print('Player ' + pl + "'s new value is 0")
                            runAgain = 1
            if rolledVal != 6 and runAgain == 0:
                break
        
        print('Player ' + player + "'s total is", totalCount[player])
        print('\n')
    print('After round', roundNumber, 'counts are', totalCount)
    for pl in totalCount:
        if totalCount[pl] > 20:
            print('Player ' + pl + ' has won the game!')
            winner = 1
    if winner == 1:
        break
    roundNumber += 1 
    print('\n')