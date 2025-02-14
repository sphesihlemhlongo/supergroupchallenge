def find_duplicates(outcomes):
    seen = set()
    duplicates = []
    for num in outcomes:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Test Cases
print(find_duplicates([0, 3, 2, 1, 3, 2]))  # [2, 3]
print(find_duplicates([7,1,5,4,3,4,6,0,9,5,8,2]))  # [4, 5]
print(find_duplicates([0, 1, 2, 3, 4, 5, 5, 0]))  # [0, 5]

# Test for:
print(find_duplicates([123456, 234567, 123347, 456789, 567890, 678901, 789012, 890123, 901234, 
                       112233, 223344, 334455, 789012, 222234, 123347]))  # Output?
