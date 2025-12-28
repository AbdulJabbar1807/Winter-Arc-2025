nums = [10,20,30,40,50]

for num in nums:
    print(num)

temps = [30,32,35,40,42,28,25]
total = 0
count = 0
for temp in temps:
    total = temp + total
    count += 1

average = total/count
print(f'Average tempreature is {average}')

