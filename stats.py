def get_num_words(text):
    split_words = text.split()
    total_words = len(split_words)
    return total_words

def get_num_characters(text):
    lowercase = text.lower()
    char_dict = {}
    for char in lowercase:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_dict(char_dict):
    sorted_list = []
    for key, value in char_dict.items():
        sorted_list.append({'char': key, 'count':value})
    sorted_list.sort(reverse=True, key=lambda item: item['count'])
    return sorted_list