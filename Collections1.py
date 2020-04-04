courses = ['History','Math','physics','Compsci']
nums = [1,2,4,5,3]

##courses.sort(reverse=True)
##nums.sort(reverse=True)
##sorted_courses=sorted(courses)
##
##print(courses)
##print(sorted_courses)
##print(sum(nums))

course_str=' - '.join(courses)
new_list=course_str.split(' - ')

print(course_str)
print(new_list)


