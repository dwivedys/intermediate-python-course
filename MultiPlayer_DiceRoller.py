''' 30th Jan 2021'''
''' A multi-player dice game '''
''' You can choose howevermany players you want to play in the game '''
''' One Edge case when all values are the same still needs to be resolved'''

import random

def find_winner(arr):
    l = len(arr)
    win_val = 0
    for i in range(0, l):
        if arr[i] < win_val:
            continue
        else:
            for j in range(i+1, l):
                if arr[j] > arr[i]:
                    win_pos, win_val = j, arr[j]
                else:
                    win_pos, win_val = i, arr[i]

    print(f'Player {win_pos+1} won by rolling a total of {win_val}')

def main():
    
    # Let's play
    
    num_players = int(input('Enter the number of players: '))

    dice_sum_results = []
    for p in range(0, num_players):
        print(f'Now Playing Player = {p+1}')
        dice_rolls = int(input('How many dice would you like to roll? '))
        dice_size = int(input('How many sides are the dice? '))
        dice_sum = 0
        for i in range(0, dice_rolls):
            roll = random.randint(1,dice_size)
            dice_sum += roll
            if roll == 1:
                print(f'You rolled a {roll}; Critical Fail!')
            elif roll == 6:
                print(f"You rolled a {roll}; Critical Success!")
            else:
                print(f"You rolled a {roll}")
        dice_sum_results.append(dice_sum)
        print(f'You have rolled a total of {dice_sum}')
        
    print(f'The players rolled the following totals respectively: {dice_sum_results}')
        

# Find the winning player
    find_winner(dice_sum_results)

if __name__== "__main__":
    main()