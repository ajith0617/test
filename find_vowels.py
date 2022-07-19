word = input("Enter the word: ").lower()
vowels = ['a','e','i','o','u']
total = 0
for letter in word:
    if letter in vowels:
        total += 1

print(f"Total vowels in the word is : {total}")
