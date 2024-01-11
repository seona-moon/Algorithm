data = input()
numbers = [int(digit) for digit in data]
sum = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < 2 or sum == 0:
        sum += numbers[i]
    else:
        sum *= numbers[i]

print(sum)
