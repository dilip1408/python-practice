# file_object=open("C:\\Users\dvoruga\Downloads\FileHandling.txt",'r+')
# print("file content before writing:")
# print(file_object.read())
# file_object.write('\n python is fun')
# print("file content AFTER writing:")
# file_object.seek(0)
# print(file_object.read())
# file_object.close()

file = open("C:/Users/dvoruga/Downloads/914010033742983.txt","r")

dict1 = dict()
for line in file:
    line = line.strip().lower().split(" ")
    # print(words)
    for word in line:
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1
print(dict1)

#Fiboacci Practice-----
previous = 0
current = 1

for _ in range(5):
    next = previous + current
    previous, current = current, next
    print(next)
#Fiboacci Practice END-----

a = [1,2,3,4,5,6]
x = len(a)
print(x)

sum = 10
lis = []
for i in range(x):
    for j in range(i+1):
        if(a[i] + a[j] == sum):
            print(a[i] , a[j],"=",sum)