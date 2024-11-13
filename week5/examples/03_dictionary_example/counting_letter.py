sentences = 'we are trying to learn basics python'
shomarande = dict()

for letter in sentences:
    if letter not in shomarande:
        shomarande[letter] = 1
    else:
        shomarande[letter] += 1

# print(f'letter {list(shomarande.keys())} tekrar shode {list(shomarande.values())}')

print(list(shomarande.keys()))

for i in list(shomarande.keys()):
    # print(f'letter {i}: {shomarande[i]} bar tekrar shode')
    print(shomarande[i])

