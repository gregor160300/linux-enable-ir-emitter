from sys import argv

data = ""
for i in range(0, len(argv[1]), 2):
    data += "0x" + argv[1][i:i+2] + ","

print(data[:-1])
