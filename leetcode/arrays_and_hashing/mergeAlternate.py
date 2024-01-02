def mergeAlternately(word1: str, word2: str) -> str:
    output_list = []
    min_length = min(len(word1), len(word2))

    for i in range(min_length):
        output_list.append(word1[i])
        output_list.append(word2[i])

    output_list.extend([word1[min_length:], word2[min_length:]])

    return "".join(output_list)
