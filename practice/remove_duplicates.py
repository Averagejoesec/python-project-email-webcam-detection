#convert the input into a list
duplicate_list = input("Enter items separated by commas: ").split(", ")

print(duplicate_list)

# remove any duplicate entries
cleaned_list = []
for i in duplicate_list:
    if i not in cleaned_list:
        cleaned_list.append(i)
    else:
        continue

# print the cleaned list
print(cleaned_list)

# show how many duplicates were removed
removed_items = len(duplicate_list) - len(cleaned_list)
print(f"{removed_items} duplicate(s) were removed.")