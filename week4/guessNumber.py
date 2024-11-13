# # -----1.2 easy-----
# import random
# pc_number = random.randint(1,99) 
# hadse_karbar = int(input('lotfan hads bezanid: '))

# talash = 0
# while True:
#     if hadse_karbar > pc_number:
#         print('pc: my number is smaller than yours')
#         hadse_karbar = int(input('lotfan hads bezanid: '))
#         talash = talash + 1

#     elif hadse_karbar < pc_number:
#         print('pc: my number is bigger than yours')
#         hadse_karbar = int(input('lotfan hads bezanid: '))
#         talash = talash + 1

#     elif hadse_karbar == pc_number:
#         print(f'congratulation ur guess was TRUE :) with {talash} try')
#         break
# print('END')






# # -----1.2 hard-----
# import random
# low = 1
# high = 99
# talash = 0
# print('------------------------------------\nplz chose a number between 1 - 99 in ur mind')
# sayOk = input('OK? ')

# while True:
#     guess = random.randint(low,high)
#     print(guess) 
#     choise = input(f'chose one of these: \n K = kochektar \n B = bozorgtar \n S = sameNumber:').lower()
#     talash = talash + 1

#     if choise == 's':
#         print(f'ur number is {guess} \n talash ha: {talash}')
#         print('END')
#         break
#     elif choise == 'k':
#         high = guess - 1
#     elif choise == 'b':
#         low = guess + 1


    
        


