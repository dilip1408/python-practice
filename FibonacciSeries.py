#
# def fib(n):
#     if(n<=0):
#         print("Invalid Input")
#     else:
#         a=0
#         b=1
#         # print(a)
#         # print(b)
#
#         for i in range(1,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)
#
# #-------------------Fibonacci ---------------------
# a = 0
# b = 1
#
# for _ in range(5):
#     c = a + b
#     a = b
#     b = c
#     print(c)

#
# print(__name__)
#
# class Computer:
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
#         print('In init')
#
#     def config(self):
#         print("In config method", self.cpu,self.ram)


# comp1 = Computer('i5',16)
# #For understanding
# ##Computer.config(comp1)
#
# comp1.config()
# #comp1.config('Intel',1)
#
# a=5
# a.bit_length()

# #---------------Palindrome-------------- by converting number into string as reverse string-----------
# string = "101"
# b = list(range(100,200))
# print(b)
#
# for num in b:
#     str_rev = ''.join(reversed(str(num)))
#     if str(num) == str_rev:
#         print(str, str_rev)
#         print(str, ":This is palindrome")
#     else:
#         # print(num, str_rev)
#         # print(num, "is not a palindrome")
#         pass
#
#
#
# #
# # str_rev = ''.join(reversed(str))
# #
# # if str == str_rev:
# #     print(str,str_rev)
# #     print(str, ":This is palindrome")
# # else:
# #     print(str, str_rev)
# #     print(str, "is not a palindrome")
#---------------Palindrome-------------- without converting number into string as reverse string-----------

