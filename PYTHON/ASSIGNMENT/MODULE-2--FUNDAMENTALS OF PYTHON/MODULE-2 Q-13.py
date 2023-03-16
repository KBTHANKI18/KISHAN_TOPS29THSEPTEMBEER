# Write a Python program to count the number of characters (character frequency) in a string
string = input("Enter a string: ")
frequency = {}
for character in string:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1
print("Character frequency:")
for character, count in frequency.items():
    print(f"{character}: {count}")
