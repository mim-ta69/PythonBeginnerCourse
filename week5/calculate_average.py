numbers = [1,5]
def calculate_average(a):
    count = 0
    i = len(numbers)
    for num in numbers:
        count = (count + num)
        
    return int(count/i)

print(calculate_average(numbers))
