def find_it(array):
    for i in array:
        count = array.count(i)
        if not (count % 2) == 0:
            return i
    return None
