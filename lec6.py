'''
Sean Carley Lecture 6
IA 241
'''
for num in [1,2,3]:
    print(num+1)

for c in 'this is lec6':
    print(c)
    
for c in 'this is lec6'.split():
    print(c)

for i in range(1,5,2):
    print(i)

for i in range(1,5):
    print(i)

num_list = [123,434,43243, 23432,4324]

possible_max_num = num_list[0]

for num in num_list:
    if num > possible_max_num:
        possible_max_num = num

print(possible_max_num)
