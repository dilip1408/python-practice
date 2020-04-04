# union of two lists
mylist1 = [1,2,3,4,5]
mylist2 = [4,5,6,7,8]

def union(mylist1,mylist2):
    return set(mylist1+mylist2)

if __name__ == "__main__":
    print("In main")
print(union(mylist1,mylist2))
