sentence = input("Enter a sentence: ")
words = sentence.split()

print(f"Number of words: {len(words)}")

word_count = {}
for word in words:
    key = word.lower()
    word_count[key] = word_count.get(key, 0) + 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"  {word}: {count}")
