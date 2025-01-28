import csv
import statistics

with open("test2.txt", "r") as f:
    datas = csv.reader(f)
    for data in datas:
        average_list = []
        for number in data:
            average_list.append(int(number))
        result = statistics.mean(average_list)
        print(result)
        
        with open("result.txt", "w") as ff:
            
            ff.write(f'ur average is: {str(result)}')