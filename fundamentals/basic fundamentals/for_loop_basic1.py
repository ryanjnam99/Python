for i in range(151):
    print(i)

for i in range(5,1001):
    if i%5 == 0:
        print(i)

for i in range(1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

total_sum = 0
sum = 0
for i in range(500001):
    if i%2 != 0:
        sum=sum+i
print(sum)

i = 2022
while i>=0:
    i-=4
    if i>0:
        print(i)

lowNum=5
highNum=278
mult=8
for i in range(lowNum,highNum+1):
    if i%mult == 0:
        print(i)



