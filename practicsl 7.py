'''practical 7
write a programm to find the no. of occurance of a word
from a input file
and store all the output in a file
'''
import string
counter=0
output=[]
ctn=[]
file=open('C:/Users/AKASH SHARMA/Desktop/prac7.txt')
input=file.read()
words=input.split()
words.sort()
for i in range(len(words)):
    j=1
    chk = words[i]
    if chk!='_':
     for j in range(len(words)):
        ck2=words[j]
        if(chk==ck2):
            counter=counter+1
            words[j]='_'
    output.append(chk)
    ctn.append(counter)
    counter=0
finallist=[]
for i in range(len(words)):
    if output[i]!='_':
        finallist.append(output[i])
        finallist.append(ctn[i])
f=open("output.txt",'w')
n=0
for i in range(0,len(finallist),2):
  f.write(str(finallist[i])+':'+str(finallist[i+1]))
  f.write('\n')
f.close