dic = open('words.txt', 'rb')
alpha = [     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
            , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

            , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
            , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'

            , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
            , '.', '&', '-', ',', "'", "/", "!"]

def dictionary():
    D = dic.read().split('\n')
    return D


# dd = dictionary()
# index_dic = []
# for word in dd:
#     index_word = []
#     for a in word.lower():
#         index_word.append(alpha.index(a))
#     index_dic.append(index_word)
#
# for j, k in zip (dd, index_dic):
#     print "WORD: {:15s}  -   INDECIES: {}".format(j,k)

