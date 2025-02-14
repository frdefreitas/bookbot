def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #count_words(file_contents)
        num_characters = count_characters(file_contents)
        print(num_characters)
        
def count_words(text):
    words = text.split()
    return (len(words))

def count_characters(text):
    lower_text = text.lower()
    characters = {}

    for char in lower_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters

main()