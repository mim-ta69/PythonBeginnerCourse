import csv
import statistics

file_path = r"C:\Users\mos13\OneDrive\Desktop\PythonBeginnerCourse\week8\nomarat.csv"

with open(file_path, "r") as f:
    data = csv.reader(f)
    for nomarat in data:
        int_list = []
        for nomre in nomarat:
            int_nomre = int(nomre)
            int_list.append(int_nomre)
            moaadel = statistics.mean(int_list)
    
    with open("moaadel.txt", "w") as ff:
        ff.write(f"ur average is: {str(moaadel)}")