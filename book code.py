#read text file
# convert string to ascii
# convert decimal(ascii) to binary

from pathlib import Path

file = open("textfile.txt", "r")

'''for words in file:
    print(words, end="")
    
'''
#print(file.read())

#reading and converting to ascii##################################################
arr = []

#for i in file.read():
    #print(i,end="")
    
#print("\n")
file.close()

file = open("textfile.txt", "r")

for i in file.read():
    #print(ord(i),end=" ")
    arr.append(ord(i))
    
file.close()

print("\n")
#print(arr)

#reading and converting to ascii END ##############################################

#maybe use an array to compare the final decimal and array of the book


#create final decimal##############################################################
dec = ""
file = open("textfile.txt", "r")

for i in file.read():
    dec = dec + str(ord(i))
    
    
file.close()

#print("\n")
#print(dec)


#comparing final decimal and array#################################################
#using count for comparing 
count = 0
#print(arr)
for i in arr:
    #print(i,end=" ")
    for j in range(1,len(str(i))+1):
        
        count = count + 1
print("\n")
print(count)
print(dec)

if (count == len(dec)):
    print("same size")
    

'''for i in arr:
    for j in range(1,len(str(i)+1)):
        print(i,j,end=" ")
'''
