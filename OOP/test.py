# n = int(input())
#
# for i in range(0,n+1):
#     print(i)
#
# n = int(input())
#
# for i in range(0,n+1):
#     print(100+i)
#
# n = int(input())
#
# for i in range(n,-1,-1):
#     print(i)
#
# n = int(input())
#
# for i in range(0,n+1,2):
#     print(i)
#

# get input
print('Input number: ', end='')
num = int(input())

sum = 0
for num in range(num, 0):
    num = num / 10
    print(num)

print(f'Sum of digits of {num} = {sum}')


#
#
#
# if


numbers = [1, 2, 3, 4, 5]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(f"{numbers[i]} is greater than {numbers[i - 1]}")
    else:
        print(f"{numbers[i]} is not greater than {numbers[i - 1]}")




