def get_word_count(text):
    words = text.split()
    total_words = len(words)
    # print(f'Found {total_words} total words')
    return (f'Found {total_words} total words')

def get_character_count(text) -> dict[str,int]:
    character_dic = {}
    character_count = 1
    text = text.lower()
    for character in text:
        if character not in character_dic:
            character_dic[character] = character_count
        else:
            character_dic[character] = character_dic[character] + 1
    # print(character_dic)
    return character_dic

def sort_on(element:tuple[str,int]) -> int:
    return element[1]


def chars_dict_to_sorted_list(character_dic) -> list[tuple[str,int]]:
    new_characters_count_list = []
    for character in character_dic:
        new_tuple = character , character_dic[character]
        new_characters_count_list.append(new_tuple)
    new_characters_count_sorted_list = sorted(new_characters_count_list, reverse=True, key=sort_on)
    # print(new_characters_count_sorted_list)
    return new_characters_count_sorted_list
