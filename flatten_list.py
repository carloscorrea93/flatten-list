from typing import Union

def flatten_list(input: list) -> list:
    result: list = []
    if not isinstance(input, list):
        raise TypeError("input_list must be an list")
    if len(input) == 0:
        return input

    element: Union[list, int, str]
    for element in input:
        if isinstance(element, list):
             result.extend(flatten_list(element))
        else:
            result.append(element)
           
    return result
