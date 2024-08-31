def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars = get_char_freqs(text)
    sorted_chars = sorted(chars.items(), key=lambda char_freq: char_freq[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for char_tuple in sorted_chars:
        if char_tuple[0].isalpha():
            print(f"The '{char_tuple[0]}' character was found {char_tuple[1]} times")
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

main()