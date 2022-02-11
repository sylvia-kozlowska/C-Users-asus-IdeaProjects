# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
new_text = ""
text = text.casefold()
print(text)
for character in text:
    if character.isalnum() == True:
        new_text = new_text + character
print(new_text)

for character in new_text:
    word_count[character] = word_count.setdefault(character, 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
