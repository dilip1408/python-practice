a = int(input(" Enter the first value: "))
b = int(input(" Enter the Second value: "))

try:
    print("Connection is opened")
    print((a/b))

except Exception as  e: #e is just an exception in case if you want to print
    print("-------error--------",e)

finally:
    print("Connection is closed")
