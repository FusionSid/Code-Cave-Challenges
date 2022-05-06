import re

# phrase = "That's the password: 'PASSWORD 123'!, cried the Special Agent.\nSo I fled"
phrase = input("Enter a string: ")

print(f"Original Phrase: {phrase}")

new_phrase = re.split(" |\\n|\\t", phrase)
new_phrase = [i.lower() for i in new_phrase]
new_phrase = [
    re.sub("\*|\?|\^|\$|\(|\)|\[|\]|\{|\}|\||\.|!|'|\"|:|,", "", i) for i in new_phrase
]

print(f"New Phrase (with space inserted as sep): {' '.join(new_phrase)}")

word_count = {}

for word in new_phrase:
    if word in word_count:
        word_count[word] += 1
        continue
    word_count[word] = 1

for key, value in word_count.items():
    print(f"{key}: {value}")
