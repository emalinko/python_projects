# def comp(array1, array2):
#     array2 = [int(x**0.5) for x in array2]
#     for a, q in zip(sorted(array1), sorted(array2)):
#         if a != q:
#             return False
#     return True

# def comp(array1, array2):
#     if array1 is None or array2 is None: # compare to None with is
#         return False
#     if len(array1) != len(array2):
#         return False
#
#     array1 = sorted(array1)
#     array2 = sorted(array2)
#
#     for idx,num in enumerate(array1):
#         if num*num != array2[idx]:
#             return False  # early return on first mismatch
#     return True
#
#
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
#
#
# if __name__ == '__main__':
#     res = comp(a1, a2)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from itertools import permutations

# def direction_reduction(array):
#     perm_full = list(permutations(['SOUTH', 'NORTH'], 2)) + list(permutations(['WEST', 'EAST'], 2))
#
# def direction_reduction(array):
#     perm_full = [('SOUTH', 'NORTH'), ('NORTH', 'SOUTH'), ('WEST', 'EAST'), ('EAST', 'WEST')]
#     for a, b in zip(array, array[1:]):
#         if (a, b) in perm_full:
#             array.remove(a)
#             array.remove(b)
#             for x, y in zip(array, array[1:]):
#                 if (x, y) in perm_full:
#                     array.remove(x)
#                     array.remove(y)
#
#         # print(result_list)
#     return array
#
#
# if __name__ == '__main__':
#     full = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
#
#     direction_reduction(full)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# def longest_consec(strarr, k):
#     n = len(strarr)
#     if n == 0 or k > n or k <= 0:
#         return ""
#     group_list = [strarr[i:i + 1] + strarr[i + 1:i + k] for i in range(n)]
#     list_strings = [''.join(sublist) for sublist in group_list]
#     result = sorted(list_strings, key=len, reverse=True)[0]
#     return result
#
#
# if __name__ == '__main__':
#     longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# def is_valid_walk(walk):
#     array = []
#     for x in walk:
#         if x == 'e' and 'w' not in array:
#             array.append(x)
#         elif x == 'e' and 'w' in array:
#             array.remove('w')
#         elif x == 'w' and 'e' not in array:
#             array.append(x)
#         elif x == 'w' and 'e' in array:
#             array.remove('e')
#         elif x == 's' and 'n' not in array:
#             array.append(x)
#         elif x == 's' and 'n' in array:
#             array.remove('n')
#         elif x == 'n' and 's' not in array:
#             array.append(x)
#         elif x == 'n' and 's' in array:
#             array.remove('s')
#     if (len(array) == 0) and (len(walk) == 10):
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     import pytest
#
#     assert is_valid_walk(['s', 'e', 'w', 'w', 'n', 'e', 's', 'w', 'n', 'n']) is False
#     assert is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']) is False
#     assert is_valid_walk(['w']) is False
#     assert is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']) is False

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#
# def song_decoder(song):
#     song.replace('WUB', ' ')
#     return " ".join(song.split())
#
# if __name__ == '__main__':
#     song_decoder('AWUBWUBWUBBWUBWUBWUBC')

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import test


# def bouncing_ball(h, bounce, window):
#     h = float(h)
#     b = float(bounce)
#     w = float(window)
#     if h > 0 and 0 < b < 1 and w < h:
#         counter = 0
#         while h > w:
#             counter += 1
#             h *= b
#             if h > w:
#                 counter += 1
#         return print(counter)
#     else:
#         return -1
#
#
# if __name__ == '__main__':
#     bouncing_ball(2, 0.5, 1)
#     bouncing_ball(3, 0.66, 1.5)
#     bouncing_ball(30, 0.66, 1.5)
#     bouncing_ball(30, 0.75, 1.5)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////\

# def binary_array_to_number(q):
#     q.reverse()
#     result = []
#     for x in range(len(q)):
#         if q[x] == 1:
#             result.append(2 ** x)
#     return sum(result)
#
#
# if __name__ == '__main__':
#     binary_array_to_number([0, 0, 0, 1])
#     binary_array_to_number([0, 0, 1, 0])
#     binary_array_to_number([1, 1, 1, 1])
#     binary_array_to_number([0, 1, 1, 0])

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////\
#
# def count_smileys(arr):
#     elements = ((':', ';'), ('-', '~'), (')', 'D'))
#     counter = 0
#     eyes = (':', ';')
#     noses = ('-', '~')
#     lips = (')', 'D')
#     for face in arr:
#         if face[0] in eyes and face[1] in lips:
#             counter += 1
#         elif face[0] in eyes and face[1] in noses and face[2] in lips:
#             counter += 1
#     if counter:
#         return counter
#     else:
#         return 0
#
#
# if __name__ == '__main__':
#     count_smileys([])
#     count_smileys([':D', ':~)', ';~D', ':)'])
#     count_smileys([':)', ':(', ':D', ':O', ':;'])
#     count_smileys([';]', ':[', ';*', ':$', ';-D'])

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////\


def rot13(message):
    a = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    # indexes = [a.index(message.lower()[i]) + 13 for i in [x for x in range(len(message))]]
    result = ''
    for letter in message:
        if letter.lower() in a and letter.isupper():
            result += a[a.index(letter) + 13].upper()
        elif letter in a:
            result += a[a.index(letter) + 13]
        else:
            result += letter

    return result


if __name__ == '__main__':
    rot13("grfg")
    rot13("Grfg")
