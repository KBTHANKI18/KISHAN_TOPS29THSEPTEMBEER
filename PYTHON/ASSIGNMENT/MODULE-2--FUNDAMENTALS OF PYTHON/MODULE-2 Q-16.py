# Write a Python program to count the occurrences of each word in a given sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
