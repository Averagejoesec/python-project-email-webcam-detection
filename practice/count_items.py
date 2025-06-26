# enter a list
nums = input("Enter a list of numbers separated by commas: ").split(', ')

# print(nums)
# enter number you want to count
count_num = input("Enter number you want to count: ")

# count how many times the number appears in the list
num_occurrence = []
for i in nums:
    if i == count_num:
        num_occurrence.append(i)
    else:
        continue

print(len(num_occurrence))