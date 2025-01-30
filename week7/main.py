# context manager --> with
file_path = r"C:\Users\mos13\OneDrive\Desktop\PythonBeginnerCourse\week7\hello.txt"




with open(file_path, "r") as f:
    data = f.read()

    with open("school.txt", "w") as file2:
        file2.write(data)
