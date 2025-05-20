import sys

from stats import num_words, num_characters, pretty_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
bookpath = sys.argv[1]

book_text = get_book_text(bookpath)
character_count = num_characters(book_text)
word_count = num_words(book_text)
sorted_characters = pretty_report(character_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {bookpath}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char_dict in sorted_characters:
    print(f"{char_dict['char']}: {char_dict['num']}")
print("============= END ===============")
