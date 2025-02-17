def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = count_words(text)
        num_characters = count_characters(text)

        print_report(book_path, num_words, num_characters)

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

def print_report(book_path, num_words, num_characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    list_dict = list(num_characters.items())
    list_dict.sort(reverse=True, key=sort_on)

    for char in list_dict:
        character = char[0]
        value = char[1]
        if character.isalpha():
            print(f"The '{character}' character was found {value} times")
    
    print("--- End report ---")            

def sort_on(list_dict):
    return list_dict[1]    

main()