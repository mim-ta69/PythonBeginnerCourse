input_numbers = '3+2+1+2+3+1+3+1+1+1'

x = input_numbers.split('+')
y = sorted(x, key=int, reverse=False)

print(y)