def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = appearance(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print()
    print("--- End report ---")

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char" : ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def appearance(text):
    char_count = {}
    for i in text.lower():
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()