# 1 countdown
def countdown(x):
    arr = []
    while x>=0:
        arr.append(x)
        x-=1
    return arr

print(countdown(5))

# 2 Print and return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2])) 


# 3 First plus length
def first_plus_length(x):
    sum = x[0]+len(x)
    return sum

print(first_plus_length([2,3,4,5,6,7,10]))

# 4 Values greater than second
def values_greater_than_second(list):
    if len(list) < 2:
        return False 
    arr = []  
    for x in range (0,len(list)):
        if list[x]>list[1]:
            arr.append(list[x])
    print(arr)
    return(len(arr))
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5]))

# 5 This Length, That value
def length_and_value(a,b):
    arr=[]
    for x in range (0,a):
        arr.append(b)
    return arr
print(length_and_value(4,7))
print(length_and_value(6,2))
