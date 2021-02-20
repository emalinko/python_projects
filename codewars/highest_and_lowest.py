def high_and_low(string):
    string_list = string.split()
    ints = [int(item) for item in string_list]
    result = []
    max_element = max(ints)
    min_element = min(ints)
    result.append(max_element)
    result.append(min_element)
    result = [str(item) for item in result]
    result = ' '.join(result)
    print(result)
    return result


if __name__ == '__main__':
    high_and_low("1 2 3 4 5")
    high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
    high_and_low("1 9 3 4 -5")

