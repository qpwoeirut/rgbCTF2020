from collections import Counter

with open("11.txt", 'r') as f:
    text = f.read()

text = text.replace(' ', '')  # remove spaces

letter_counter = Counter(text)

print(letter_counter)