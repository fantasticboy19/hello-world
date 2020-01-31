import sys
path = 'c:\user\desktop\hello'
for i in os.listdir(path):
    print(i)
#sys.path is a list!
print('sys.path')
os.path.append('c:\user\desktop\hello.exe')

class baseNet(nn.Module){
        def __init__(self):
            self.con = nn.conv2d(20,3,10)
            self.relu = nn.Relu(10,5)

        def forwards(self,x):
            output = self.con(x)
            return self.relu(output)
            }
