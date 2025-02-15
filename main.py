def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_characters = count_characters(text)
        print(num_characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
    words = text.split()
    return len(words)

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