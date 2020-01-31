import os
path = 'c:\user\desktop\hello'
for i in os.listdir(path):
    print(i)
print('os.path')
os.path.append('c:\user\desktop\hello.exe')
