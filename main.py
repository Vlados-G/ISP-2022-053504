import re
import argparse


def configure_parser():
    parser = argparse.ArgumentParser(description="Count ")
    parser.add_argument("--n", help="n help")
    parser.add_argument("--k", help="k help")
    parser.add_argument("-string", help="text help", nargs="+")
    return parser


def words_amount(word_list: list):
    words_count = {}
    for word in word_list:
        if words_count.__contains__(word):
            continue
        words_count[word] = word_list.count(word)
    return words_count


def average_words_amount(word_list, words_count):
    average_count = len(word_list) / len(words_count)
    return average_count


def median_value(word_list):
    word = len(word_list)
    med = int(word / 2 + 0.5)
    return med


def top_n_anagramms(n, k, string, word_list):
    result = {}

    def anagramms(word):
        word_len = len(word)

        for i in range(word_len):
            if i + n > word_len:
                break

            a_gramm = word[i:i + n]
            result.update({a_gramm: string.count(a_gramm)})

    for word in word_list:
        anagramms(word)

    while len(result) > k:
        result_keys = list(result.keys())
        min_key = result_keys[0]

        for key in result_keys[1:]:
            if result[key] < result[min_key]:
                min_key = key

        result.pop(min_key)

    return result


def main(k, n, string):
    # k = input("Введите k: ")
    # n = input("Введите n: ")
    if k == '':
        k = 10
    if n == '':
        n = 4
    k = int(k)
    n = int(n)
    # string = input("Введите текст: ")
    string = re.sub('[.,&!\n]', '', string)
    word_list = string.split()

    amount = words_amount(word_list)
    print("Количество слов: " + str(amount))

    average_amount = average_words_amount(word_list, amount)
    print("Среднее количество слов: " + str(average_amount))

    median_amount = median_value(word_list)
    print("Медиан: " + str(median_amount))

    top_ngramm = top_n_anagramms(n, k, string, word_list)
    print("Топ-k n-грамм: " + str(top_ngramm))


if __name__ == '__main__':
    args = configure_parser().parse_args()
    main(args.n, args.k, " ".join(args.string))
