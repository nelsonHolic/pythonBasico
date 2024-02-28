"""
go example


// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func main() {
    var a int
    a = 1
    var b *int
    b = &a
    fmt.Printf("Hello, %d\n", &a)
    fmt.Printf("Hello, %d\n", b)
    a = 3

    fmt.Printf("Hello, %d\n", a)
    fmt.Printf("Hello, %d\n", *b)
}

output:

Hello, 824633794600
Hello, 824633794600
Hello, 3
Hello, 3

Program exited.
"""


def modify_dicts(my_dict: dict) -> None:
    # se pasa por referencia
    my_dict['my_modified_key'] = "I was modified"
    my_dict['my_internal_dict']['my_modified_key'] = "I was modified"


def modify_my_list(my_list: list) -> None:
    my_list[3] = "3"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("--------------------- mutabilidad de dictionario ------------------------------")
    dictionary = {'key1': "value 1", 'my_internal_dict': {'key2': "my value 2"}}
    dictionary_ref = dictionary
    dictionary_copy = dictionary.copy()
    modify_dicts(dictionary_copy)
    print("My original dict", dictionary)
    print("My copy", dictionary_copy)

    print("--------------------- inmutabilidad de strings ------------------------------")

    my_string = "hola juan y carlos"
    print(my_string[4])
    print(my_string[:4])
    print(my_string[12:])
    my_string2 = my_string[:3] + "3" + my_string[4:]
    print(my_string2)

    print("--------------------- mutabilidad de listas ------------------------------")

    my_list_string = ["h", "o", "l", "a", " ", "j", "u", "a", "n", " ", "y", " ", "c", "a", "r", "l", "o", "s"]
    print(my_list_string)
    print(my_list_string[2])
    print(my_list_string[:4])
    print(my_list_string[12:])
    modify_my_list(my_list_string.copy())
    print(my_list_string)

    print("--------------------- strings como listas ------------------------------")

    my_string_2 = "hola juan y carlos"
    my_list_string_2 = list(my_string_2)
    my_list_string_2[3] = "3"
    my_string_2 = "".join(my_list_string_2)
    print(my_list_string_2)
    print(my_string_2)
    my_list_string_2[3] = "3"
    my_string_2 = "".join(my_list_string_2)

    print("--------------------- inmutabilidad de tuplas ------------------------------")

    my_tuple = ("h", "o", "l", "a")
    print(type(my_tuple))
    print(my_tuple)
    print(tuple(my_list_string_2))
    my_single_tuple = "h",

    print(type(my_single_tuple))
    print(my_single_tuple)

    my_tuple_dict = {'key1': "val1"},
    print(type(my_tuple_dict))
    print(my_tuple_dict)
    my_tuple_dict[0]['key1'] = "I changed"
    print(my_tuple_dict)

    my_tuple_key = "my_key1", "my_key2",

    my_dict_tuple = {my_tuple_key: "my value"}
    print(my_dict_tuple)
