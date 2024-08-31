def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars = get_char_freqs(text)
    dict_list = dict_to_list(chars)
    dict_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for dict in dict_list:
        char = list(dict.keys())[0]
        if char.isalpha():
            freq = dict[char]
            print(f"The '{char}' character was found {freq} times")
    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_freqs(text):
    text = text.lower()
    char_freqs = {}
    for i in range(len(text)):
        if text[i] not in char_freqs:
            char_freqs[text[i]] = 1
        else:
            char_freqs[text[i]] += 1
    return char_freqs

def dict_to_list(chars):
    dict_list = []
    for k, v in chars.items():
        small_dict = {}
        small_dict[k] = v
        dict_list.append(small_dict)
    return dict_list

def sort_on(dict):
    return list(dict.values())[0] 

main()