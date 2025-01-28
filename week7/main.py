with open('test.txt', 'r') as f:
    k = f.read()
with open('file2.txt', 'w') as f: 
    x = "slm slm"
    f.write(k)
    f.write(x)
print('write to file `file2.txt`')
