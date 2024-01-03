def mergeAlternately(word1: str, word2: str) -> str:
    output_list = []
    min_length = min(len(word1), len(word2))

    for i in range(min_length):
        output_list.append(word1[i])
        output_list.append(word2[i])

    output_list.extend([word1[min_length:], word2[min_length:]])

    return "".join(output_list)


def mergeAlternatelyOther(word1: str, word2: str) -> str:
    res = ""

    word1_len = len(word1)
    word2_len = len(word2)
    max_len = max(word1_len, word2_len)

    for i in range(max_len):
        if i < word1_len:
            res += word1[i]
        if i < word2_len:
            res += word2[i]

    return res


print(mergeAlternatelyOther("abc", "defgi"))
