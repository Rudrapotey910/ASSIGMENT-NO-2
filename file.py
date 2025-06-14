#Task 1
x=int(input('enter the number'))
if x%2==0:
    print(f"{x} is an even  number")
else:
    print(f"{x} is an odd number")
#task2
start = 1
end = 50
count = 0
for i in range(start, end + 1):
    count = count + i
print('The sum of numbers from', start, 'to', end, 'is:', count)
