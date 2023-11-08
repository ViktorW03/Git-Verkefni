def main():
    string_list = []
    string_list = input().split(',')
    
    int_tuple = list_to_int_tuple(string_list)
    print(int_tuple)

def list_to_int_tuple(search_list):
    result_list = []
    for item in search_list:
        try:
            int_value = int(item)
            result_list.append(int_value)
        except ValueError:
            pass
    return tuple(result_list)



if __name__ == "__main__":
    main()

