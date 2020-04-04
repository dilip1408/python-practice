# nums = [1,2,3]
# print(dir(nums))
# i_nums = iter(nums)
# print(dir(i_nums))
# print(type(i_nums))
# print(i_nums)
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         # print(self.start)
#         if self.start >= self.end:
#             raise StopIteration
#         current = self.start
#         self.start += 1
#         return current
# nums = MyRange(1, 10)
# for i in nums:
#     print(i)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

#Acheving the __next__() functionality through generators
# def my_range():
#     print("Hello")
#     start = 1
#     end = 5
#     print(start, end)
#
#     current = start
#     while current < end:
#         yield current
#         current += 1
#
# # nums = my_range(1, 10)
# print(my_range())
# for num in nums:
#     print(num)

# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))


# print(dir())

# l = [1,2,3]
# ll = l.__iter__()
# print(type(ll))
# print(dir(ll))
# print(next(ll))