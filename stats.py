def get_word_number(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        return word_count

def get_char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        lower_file_contents = file_contents.lower()
        set_file_contents =  set(lower_file_contents)
        
        dict_char_count = {}
        for set_char in set_file_contents:
            char_count = 0
            for char in lower_file_contents:
                if set_char == char:
                    char_count += 1 
            dict_char_count[set_char] = char_count
        
        return dict_char_count


def list_of_dict(dict):
    list_of_dict = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["letter"]= key
        new_dict["count"] = value
        list_of_dict.append(new_dict)
    return list_of_dict

def sort_on_count(dict):
    return dict['count']
        
    






    