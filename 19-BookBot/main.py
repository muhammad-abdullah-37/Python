import sys
from stats import get_word_count
from stats import get_character_count
from stats import chars_dict_to_sorted_list

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(path:str) -> str:
    with open(path,'r', encoding="utf-8-sig") as file:
        file_content = file.read()
        # print(file_content)
    return file_content


def print_report(book_path,word_count,character_sorted_list):
    print('============ BOOKBOT ============')
    print('Analyzing book found at '+book_path+'...')
    print('----------- Word Count ----------')
    print(word_count)
    print('--------- Character Count -------')
    for i in range(0,len(character_sorted_list)-1,1):
        if character_sorted_list[i][0].isalpha() == True:
            print(f'{character_sorted_list[i][0]}: {character_sorted_list[i][1]}')
    print('============= END ===============')



def main():
    print_report(sys.argv[1],get_word_count(get_book_text(sys.argv[1])), chars_dict_to_sorted_list(get_character_count(get_book_text(sys.argv[1]))))
main()
