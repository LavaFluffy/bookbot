def get_num_words(string):
    words = string.split()
    return len(words)

def get_character_summary(string):
    summary_dict = {}
    for character in string:
        lower_char = character.lower()
        if lower_char not in summary_dict:
            summary_dict[lower_char] = 1
        else:
            summary_dict[lower_char] += 1
    return summary_dict

def sort_on(items):
    return items["num"]

def sort_char_summary(char_sum):
    char_list = []
    for key in char_sum:
        char_list.append({"char":key, "num":char_sum[key]})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
