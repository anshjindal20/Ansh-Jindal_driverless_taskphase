n = int(input("Enter the number of strings: "))
strings = [input(f"Enter string {i+1}: ") for i in range(n)]

letter_counts = {}
for text in strings:
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

print(letter_counts)
