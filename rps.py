#! /usr/bin/python3

import random

c_choice = random.choice(['rock', 'paper', 'scissors'])
u_choice = input('Do you want rock paper or scissors?')

print('Computer choice:', c_choice )

if c_choice == u_choice:
    print("Matched")
elif u_choice == 'rock' and c_choice =='scissors':
    print('you win')
elif u_choice == 'paper' and c_choice == 'rock':
    print('Computer Won')
elif u_choice == 'scissors' and c_choice == 'scissors':
    print('Computer won')
elif u_choice == 'paper' and c_choice == 'scissors':
    print('You won')
elif u_choice == 'scissors' and c_choice =='paper':
    print('You Won!')
