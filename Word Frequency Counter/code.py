import string  # Import string module for punctuation handling

def word_frequency_counter(text):
    # Step 1: Convert text to lowercase
    text = text.lower()

    # Step 2: Remove punctuation (replace with empty string)
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Step 3: Split text into words (by spaces)
    words = text.split()

    # Step 4: Create an empty dictionary to store word counts
    frequency = {}

    # Step 5: Count each word using a loop
    for word in words:
        if word in frequency:       # If word already in dictionary
            frequency[word] += 1    # Increase count by 1
        else:
            frequency[word] = 1     # Otherwise, add word with count = 1

    # Step 6: Print word frequencies
    for word, count in frequency.items():
        print(f"{word}: {count}")

# Example text
sample_text = "Hello world! Hello Python. Python is great, and Python is fun."

# Run the word frequency counter
word_frequency_counter(sample_text)

# EXAMPLE WALK THROUGH
"""""
Hello world! Hello Python. Python is great, and Python is fun.
hello: 2
world: 1
python: 3
is: 2
great: 1
and: 1
fun: 1
"""
