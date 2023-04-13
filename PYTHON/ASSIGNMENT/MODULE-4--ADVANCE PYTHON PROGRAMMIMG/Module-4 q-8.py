#Q-8 Write a python program to find the longest words.
#A-8
# define function
def find_longest_words(text):
    words = text.split()
    # creating empty list
    longest_words = []
    max_length = max(len(word) for word in words)
    for word in words:
        if len(word) == max_length:
            longest_words.append(word)
    return longest_words
text = "hellooo,my name is heny"
longest_words = find_longest_words(text)
print("Longest words: ", longest_words)