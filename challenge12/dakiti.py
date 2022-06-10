import re

def dakiti(input_str: str) -> str:
    words = input_str.strip().split(" ")
    new_words = [""]*len(words)
    for word in words:
        try:
            number = int((re.findall('[0-9]+', word)[0]))
            new_words[number-1] = word.replace(str(number), "")
        except IndexError:
            continue
    return " ".join(new_words)

# text = "worl2d hell1o "
text = input("Enter the text: ")
print(dakiti(text))