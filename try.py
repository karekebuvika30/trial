from sys import stdin, stdout
from collections import Counter
name = stdin.readline().strip()
stdout.write("Hello!"+name+"\n")
arr = [1,2,3,3,4,5,5,5,6,7,8,9,0]
countDict = Counter(arr)
for k, v in countDict.items():
    stdout.write(str(k)+" "+str(v)+"\n")
