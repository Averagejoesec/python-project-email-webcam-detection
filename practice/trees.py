trees = ['oak', 'pine', 'maple', 'oak', 'birch', 'pine', 'oak']

oak_count = 0
pine_count = 0
maple_count = 0
birch_count = 0
for i in trees:
    if i == 'oak':
        oak_count += 1
    elif i == 'pine':
        pine_count += 1
    elif i == 'maple':
        maple_count += 1
    elif i == 'birch':
        birch_count +=1

print(f"oak: {oak_count}\npine: {pine_count}\nmaple: {maple_count}\nbirch: {birch_count}")