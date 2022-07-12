sample = input("Enter the word: ").lower()
vowels = ['a','e','i','o','u']
list1 = []
for sam in sample:
    if sam in vowels:
        list1.append(sam)
print(f"Total Count of vowels is {len(list1)}")