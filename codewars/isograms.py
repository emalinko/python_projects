def is_isogram(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    string = string.lower()
    valid_string = set()
    for x in string:
        if x in alphabet and x not in valid_string:
            valid_string.add(x)
            print(valid_string)
        elif string == ' ':
            print('an empty string is a valid isogram')
            return True
        else:
            print('given string doesn\'t meen reqirements')
            return False
    return True


if __name__ == '__main__':
    is_isogram('Dermatoglyphics')
    # is_isogram('isogram')
    # is_isogram('aba')
    # is_isogram('moOse')