from CheetSheets.runtime_timing import timer
'''
 You are given two lists a and b with integers, that also can be negative,
 and a target sum.

 Task:
- find a function that return true if two numbers in the list can be added to build the target sum

Tipps:
- Draw down the problem on paper to solve it
- Think about about different solutions and think about how they differ in runtime if the list would contain 1 Mio. elements

'''


sum = 12

a = [2, 5, 7, 6, 6]
b = [6, 4, 7, 9, 2]

# SOLUTIONS:
# time them at the end with the @timer followed by your solution.
@timer
def do_sthg():
    for i in range(100):
        b = i*i
        print(b)

do_sthg()

