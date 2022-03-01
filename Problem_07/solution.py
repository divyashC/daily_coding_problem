# Day 7
# Problem 7
# Date 16 Feb 2022
# Time 8:00 AM

# input -> 111
# output -> 3

def get_output_count(input_value):

    input_string = str(input_value)

    if len(input_string) == 1:
        output_count = 1
    elif len(input_string) == 2:
        output_count = 1 + (0 if input_value > 26 or input_value < 1 else 1)
    else:
        output_count = get_output_count(int(input_string[1:]))
        if (0 if int(input_string[:2]) > 26 or int(input_string[:2]) < 1 else 1):
            output_count += get_output_count(int(input_string[2:]))

    return output_count


print(get_output_count('111'))


# import string
# mapping_number = list(range(1, 27))
# mapping_alphabets = list(string.ascii_lowercase)
