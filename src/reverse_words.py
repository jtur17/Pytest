# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
def reverse_words(text):
    # Variables
    reverse = []

    # Bucle
    for i in text.split(" "):
        reverse.append(i[::-1])
    return " ".join(reverse)