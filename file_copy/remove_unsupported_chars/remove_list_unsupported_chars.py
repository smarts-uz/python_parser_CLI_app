from file_copy.file_copy_functions import remove_unsupported_chars


def remove_list_unsupported_chars(list:list):
    for index,item in  enumerate(list):
        new_item = remove_unsupported_chars(item)[0]
        list[index] = new_item

    return list
