def list_to_bool_tuple(a_list):
    boolean_value = []  
    for item in a_list:
        try:
            item = int(item)
        except ValueError:
            pass  

        boolean_value.append(bool(item))

    return tuple(boolean_value)